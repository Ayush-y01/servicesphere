from fastapi import FastAPI
from app.api.v1.router import api_router
from app.core.database import engine
from app.models import user

user.Base.metadata.create_all(bind=engine)

app  = FastAPI(title="Auth Service")

app.include_router(api_router)


@app.get("/health")
async def health_check():
    return {
        "service":"auth-service",
        "status":"running"
    }