from sqlalchemy.orm import session
from app.models.user import User
from app.core.security import hash_password
from app.core.jwt import create_access_token, create_refresh_token
from app.core.security import verify_password
from app.core.roles import UserRole

class AuthService:

    async def create_user(self, email:str, password:str, db:session, role: UserRole = UserRole.USER):
        user = User(
            email=email,
            password=hash_password(password),
            role=role.value
        )
        db.add(user)
        db.commit()
        db.refresh(user)
        return user


    async def login(self, data, db:session):
        user = db.query(User).filter(User.email == data.email).first()

        if not user or not verify_password(data.password, user.password):
            return {"error": "Invalid credentials"}
        # Yahin future me:
        # - DB check
        # - password verify
        # - JWT generate
        payload = {
            "sub": str(user.id),
            "role": user.role
        }
        return {
            "access_token": create_access_token(payload),
            "refresh_token": create_refresh_token(payload),
            "token_type": "bearer"
        }