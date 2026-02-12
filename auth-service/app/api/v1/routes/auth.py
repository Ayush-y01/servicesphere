from fastapi import APIRouter,Depends
from app.schemas.auth import LoginRequest
from app.services.auth_service import AuthService

router = APIRouter()

@router.post("/login")
async def login(
    data: LoginRequest,
    service: AuthService = Depends()
):
    return await service.login(data)