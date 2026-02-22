from fastapi import FastAPI
from app.api.v1.router import api_router
from app.core.database import engine
from app.models import user
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)

logger = logging.getLogger(__name__)

user.Base.metadata.create_all(bind=engine)

app  = FastAPI(
    title="Auth Service",
    root_path="/auth"
    )

app.include_router(api_router)


@app.get("/health")
async def health_check():
    return {
        "service":"auth-service",
        "status":"running"
    }

@app.on_event("startup")
def startup_event():
    logger.info("Auth Service Started Successfully")

