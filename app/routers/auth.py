from app import schemas, database, utils
from fastapi import HTTPException, APIRouter



router = APIRouter(tags=["Authentication"])

@router.post("/login")
async def login_user(user: schemas.UserLogin):
    user_collection = database.get_user_collection()
    
    # Find the user by email
    db_user = user_collection.find_one({"email": user.email})
    
    if not db_user or not utils.verify(user.password, db_user["password"]):
        raise HTTPException(status_code=400, detail="Invalid email or password")
    
    return {"message": "Login successful", "user_id": str(db_user["_id"])}
