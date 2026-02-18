from fastapi import APIRouter, Depends
from app.core.security import require_roles

router = APIRouter()

@router.get("/dashboard")
def admin_dashboard(
    current_user = Depends(require_roles(["admin"]))
):
    return {
        "message":"Welcome Admin",
        "admin_id":current_user.sub
    }