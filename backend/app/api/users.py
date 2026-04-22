from fastapi import APIRouter, HTTPException
from app.models.schemas import User
from app.core.auth import get_password_hash, verify_password, create_access_token
from app.core.db import db

router = APIRouter()

@router.post("/register")
async def register(user: User):
    user_exists = await db.find_one("users", {"email": user.email})
    if user_exists:
        raise HTTPException(status_code=400, detail="User already exists")
    user_dict = user.dict(by_alias=True)
    user_dict["password"] = get_password_hash(user.password)
    created_user = await db.insert_one("users", user_dict)
    token = create_access_token(data={"id": str(created_user["_id"])})
    return {"_id": str(created_user["_id"]), "username": created_user["username"], "email": created_user["email"], "token": token}

@router.post("/login")
async def login(credentials: dict):
    user = await db.find_one("users", {"email": credentials["email"]})
    if user and verify_password(credentials["password"], user["password"]):
        token = create_access_token(data={"id": str(user["_id"])})
        return {"_id": str(user["_id"]), "username": user["username"], "email": user["email"], "token": token}
    raise HTTPException(status_code=401, detail="Invalid credentials")
