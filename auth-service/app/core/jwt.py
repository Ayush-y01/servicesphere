from datetime import datetime, timedelta
from jose import jwt

SECRET_KEY = "CHANGE_ME_IN_PROD"
ALGORITHM = "HS256"

ACCESS_TOKEN_EXPIRE_MINUTES = 30
REFRESH_TOKEN_EXPIRE_DAYS = 7

def create_access_token(data:dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp":expire, "type":"refresh"})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def create_refresh_token(data:dict):
    to_encode = data.copy()
    expire = datetime.utcnow() +timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS)
    to_encode.update({ "exp":expire, "type":"refresh" })
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)