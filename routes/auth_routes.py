from fastapi import FastAPI, APIRouter, HTTPException
from models.user import User , LoginRequest
from utils.getValue import *
from config.database import db
from utils.hash_pass import *

router = APIRouter(prefix='/auth')

    
@router.post("/register")
async def register(user: User):

    getuser = get_single_value(db.user.find_one({"email": user.email}))

    if getuser:
        raise HTTPException(status_code=400, detail="User already registered")
    
    haspass = get_password_hash(user.password)
    print("has>>", haspass)

    db.user.insert_one(user)

    return {"success": False, "msg": "User registered successfully"}


@router.post('/login')
async def login_user(user: LoginRequest):
    getuser = get_single_value(db.users.find_one({"email": user.email}))
    print("getuser",getuser)

    if not getuser:
        raise HTTPException(status_code=404, detail="User not found")
    
    if getuser["password"] != user.password:
        raise HTTPException(status_code=400, detail="Incorrect password")
    
    return {"success": True, "msg": "User logged in successfully", "data": getuser}
