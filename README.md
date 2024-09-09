
# User Management and Data Integration API - Remotebricks Python Internship Assignment

## Objective

Develop a set of APIs for user registration, login, linking an ID, and implementing joins and chain delete functionality using Python and MongoDB.

## Requirements

### Framework and Libraries

- **FastAPI**: Web framework for building APIs.
- **PyMongo**: Library for interacting with MongoDB.

### API Endpoints

1. **Registration API**
   - **Endpoint**: `http://localhost:8000/users/register`
   - **Method**: `POST`
   - **Request Body**:
     ```json
     {
         "username": "sandesh bhujbal",
          "email": "sandesh@gmail.com",
          "password": "sandesh"
     }
     ```
   - **Response**:
     ```json
     {
      "message": "User registered successfully",
      "user_id": "66c9551c996fee15a88a28e4"
     }
     ```

2. **Login API**
   - **Endpoint**: `http://localhost:8000/login`
   - **Method**: `POST`
   - **Request Body**:
     ```json
     {
      "email": "sandesh@gmail.com",
      "password": "sandesh"
     }
     ```
   - **Response**:
     ```json
     {
        "message": "Login successful",
        "user_id": "66c9551c996fee15a88a28e4"
     }
     ```

3. **Link ID API**
   - **Endpoint**: `http://localhost:8000/users/link_id`
   - **Method**: `POST`
   - **Request Body**:
     ```json
     {
        "user_id": "66c9551c996fee15a88a28e4",
        "linked_id": "123e4567-e89b-12d3-a456-426614174000"
     }
     ```
   - **Response**:
     ```json
     {
       "message": "ID linked successfully",
       "linked_id": "123e4567-e89b-12d3-a456-426614174000"
     }
     ```

4. **Add User Details**
   - **Endpoint**: `http://localhost:8000/users/add_details`
   - **Method**: `POST`
   - **Request Body**:
     ```json
     {
       "user_id": "66c9551c996fee15a88a28e4",
      "address": "Pune, India",
      "phone": "+1234567890",
      "preferences": {
         "newsletter": true,
         "notifications": false
       }
     }
     ```
   - **Response**:
     ```json
     {
       "message": "Details added/updated successfully"
     }
     ```

5. **Get User with Details**
   - **Endpoint**: `http://localhost:8000/users/user_with_details/66c9551c996fee15a88a28e4`
   - **Method**: `GET`
   - **Response**:
     ```json
     {
     "user": {
        "_id": "66c9551c996fee15a88a28e4",
        "username": "sandesh bhujbal",
        "email": "sandesh@gmail.com",
        "password": "$2b$12$MC0v2olCE9VkElTkrnYWF.VziMU8hN.p/snX1TV.8LStnNx/QJ2Ja",
        "linked_id": "123e4567-e89b-12d3-a456-426614174000"
     },
     "details": {
        "_id": "66c9575a47d95a87f4559206",
        "user_id": "66c9551c996fee15a88a28e4",
        "address": "Pune, India",
        "phone": "+1234567890",
        "preferences": {
            "newsletter": true,
            "notifications": false
        }
       }
     }
     ```

6. **Delete User**
   - **Endpoint**: `http://localhost:8000/users/delete_user/66c954f2996fee15a88a28e3`
   - **Method**: `DELETE`
   - **Response**:
     ```json
     {
       "message": "User and associated data deleted successfully"
     }
     ```

## Instructions

1. **Setup FASTAPI and PyMongo**
   - Create a new FastAPI application.
   - Configure PyMongo to connect to your MongoDB instance.

2. **Registration API**
   - Create an endpoint to register new users with username, email, and password.
   - Ensure that passwords are securely hashed before storing them in the database.

3. **Login API**
   - Create an endpoint to log in users by verifying their credentials (email and password).
   - Implement appropriate error handling.

4. **Linking ID API**
   - Create an endpoint to link an ID to a user's account.
   - Ensure the ID is securely stored and associated with the correct user.

5. **Joins**
   - Implement functionality to join data from multiple collections.

6. **Chain Delete**
   - Implement functionality to delete a user and all associated data across collections.
