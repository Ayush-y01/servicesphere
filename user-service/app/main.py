from fastapi import FastAPI
from app.api.v1.router import api_router
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)

logger = logging.getLogger(__name__)

app = FastAPI(
    title="User Service",
    root_path="/users"
    )

app.include_router(api_router, prefix="/api/v1")

@app.get("/health")
def health():
    return {"status":"user-service up"}

@app.on_event("startup")
def startup_event():
    logger.info("User Service Started Successfully")