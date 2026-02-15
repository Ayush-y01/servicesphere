from fastapi import Depends, HTTPException, status
from app.dependencies.auth import get_current_user

def require_role(require_role:str):
    def role_checker(user=Depends(get_current_user)):
        if user["role"] != require_role:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Access denied"
            )
        return user
    return role_checker