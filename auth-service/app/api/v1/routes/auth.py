from fastapi import APIRouter,Depends
from app.schemas.auth import LoginRequest
from app.services.auth_service import AuthService
from sqlalchemy.orm import session

from app.dependencies.db import get_db
from app.schemas.auth import LoginRequest
from app.services.auth_service import AuthService

from app.dependencies.auth import get_current_user

router = APIRouter()

@router.post("/create_user")
async def create_user(
    data:LoginRequest,
    db: session = Depends(get_db),
    service: AuthService = Depends()
):
    user = await service.create_user(data.email, data.password, db)
    return {"id":user.id, "email":user.email}

@router.post("/login")
async def login(
    data: LoginRequest,
    db:session = Depends(get_db),
    service: AuthService = Depends()
):
    return await service.login(data,db)

@router.get("/me")
async def me(user_id: str = Depends(get_current_user)):
    return {"user_id":user_id}