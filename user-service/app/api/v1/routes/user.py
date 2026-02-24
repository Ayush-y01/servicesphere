from fastapi import APIRouter, Depends
from app.core.security import get_current_user
from app.core.security import require_roles

router = APIRouter()

@router.get("/me")
def get_me(current_user=Depends(get_current_user)):
    return {
        "message":"User Profile fetched",
        "user": current_user
    }

@router.get("/profile")
def user_profile(
    current_user = Depends(require_roles(["user","admin"]))
):
    return {
        "message":"User profile",
        "user_id":current_user.sub,
        "role":current_user.role
    }