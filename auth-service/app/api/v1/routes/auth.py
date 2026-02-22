from fastapi import APIRouter,Depends
from app.schemas.auth import LoginRequest
from app.services.auth_service import AuthService
from sqlalchemy.orm import session

from app.dependencies.db import get_db
from app.schemas.auth import LoginRequest
from app.services.auth_service import AuthService

from app.dependencies.auth import get_current_user

from jose import jwt, JWTError
from app.core.jwt import SECRET_KEY, ALGORITHM, create_access_token

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


@router.post("/refresh")
async def refresh_token(refresh_token:str):
    try:
        payload = jwt.decode(refresh_token, SECRET_KEY, algorithms=[ALGORITHM])
        if payload.get("type") != "refresh":
            return {"error":"Invalid refresh token"}
        
        user_id = payload.get("sub")

        return {
            "access_token": create_access_token({"sub":user_id}),
            "token_type":"bearer"
        }
    except JWTError:
        return {"error":"Invalid or expired refresh token"}
    
from app.dependencies.roles import require_role

@router.get("/admin-only")
async def admin_dashboard(
    user=Depends(require_role("admin"))
):
    return {
        "message":"welcome Admin",
        "user_id": user["user_id"]
    }

@router.get("/verify-token")
def verify_token(current_user = Depends(get_current_user)):
    """
    Used by API Gateway (NGINX)
    If token is valid → 200
    If invalid → 401 (handled inside get_current_user)
    """
    return{
        "status":"valid",
        "user": current_user
    }