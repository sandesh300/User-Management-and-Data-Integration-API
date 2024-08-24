from app import schemas, database, utils
from fastapi import HTTPException, Depends, APIRouter
from bson.objectid import ObjectId
import uuid


router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.post("/register")
async def register_user(user: schemas.User):
    user_collection = database.get_user_collection()
    
    # Check if the user already exists
    if user_collection.find_one({"email": user.email}):
        raise HTTPException(status_code=400, detail="Email already registered")
    
    # Hash the password
    hashed_password = utils.hash(user.password)
    
    # Insert the new user into the database
    user_data = {
        "username": user.username,
        "email": user.email,
        "password": hashed_password,
    }
    result = user_collection.insert_one(user_data)
    
    return {"message": "User registered successfully", "user_id": str(result.inserted_id)}

@router.post("/link_id")
async def link_id(link_data: schemas.LinkID):
    user_collection = database.get_user_collection()
    
    # Find the user by ID
    if not ObjectId.is_valid(link_data.user_id):
        raise HTTPException(status_code=400, detail="Invalid user ID")
    
    user = user_collection.find_one({"_id": ObjectId(link_data.user_id)})
    
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Generate a linked_id if not provided
    if not link_data.linked_id:
        link_data.linked_id = str(uuid.uuid4())
    
    # Update the user document with the linked ID
    user_collection.update_one(
        {"_id": ObjectId(link_data.user_id)},
        {"$set": {"linked_id": link_data.linked_id}}
    )
    
    return {"message": "ID linked successfully", "linked_id": link_data.linked_id}

@router.post("/add_details")
async def add_details(details: schemas.UserDetails):
    details_collection = database.get_details_collection()
    
    # Ensure the user ID is valid
    if not ObjectId.is_valid(details.user_id):
        raise HTTPException(status_code=400, detail="Invalid user ID")
    
    # Insert or update the details in the details collection
    details_data = {
        "user_id": details.user_id,
        "address": details.address,
        "phone": details.phone,
        "preferences": details.preferences
    }
    details_collection.update_one(
        {"user_id": details.user_id},
        {"$set": details_data},
        upsert=True
    )
    return {"message": "Details added/updated successfully"}

@router.get("/user_with_details/{user_id}")
async def get_user_with_details(user_id: str):
    if not ObjectId.is_valid(user_id):
        raise HTTPException(status_code=400, detail="Invalid user ID")
    
    user_collection = database.get_user_collection()
    user = user_collection.find_one({"_id": ObjectId(user_id)})
    
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Join with details collection
    details_collection = database.get_details_collection()
    user_details = details_collection.find_one({"user_id": user_id})

    if user_details:
        user_details["_id"] = str(user_details["_id"])
        user_details["user_id"] = str(user_details["user_id"])

    user["_id"] = str(user["_id"])
    if "linked_id" in user:
        user["linked_id"] = str(user["linked_id"])
    
    return {"user": user, "details": user_details}

@router.delete("/delete_user/{user_id}")
async def delete_user(user_id: str):
    if not ObjectId.is_valid(user_id):
        raise HTTPException(status_code=400, detail="Invalid user ID")
    
    user_collection = database.get_user_collection()
    details_collection = database.get_details_collection()
    
    # Delete the user
    result = user_collection.delete_one({"_id": ObjectId(user_id)})
    
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Delete associated details
    details_collection.delete_many({"user_id": user_id})
    
    return {"message": "User and associated data deleted successfully"}
