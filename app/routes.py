from fastapi import APIRouter, HTTPException
from .models import UserModel, UserResponse
from .database import get_database
from bson import ObjectId
from bson.errors import InvalidId

router = APIRouter()

@router.get("/")
async def root():
    return {"message": "Hello, World!"}

@router.post("/users/", response_model=UserResponse)
async def create_user(user: UserModel):
    db = await get_database()
    user_dict = user.model_dump()
    result = await db.users.insert_one(user_dict)
    
    created_user = await db.users.find_one({"_id": result.inserted_id})
    return UserResponse(
        id=str(created_user["_id"]),
        name=created_user["name"],
        email=created_user["email"],
        created_at=created_user["created_at"]
    )

@router.get("/users/{user_id}", response_model=UserResponse)
async def get_user(user_id: str):
    db = await get_database()
    try:
        user = await db.users.find_one({"_id": ObjectId(user_id)})
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")
        
        return UserResponse(
            id=str(user["_id"]),
            name=user["name"],
            email=user["email"],
            created_at=user["created_at"]
        )
    except InvalidId:
        raise HTTPException(status_code=400, detail="Invalid user ID format")