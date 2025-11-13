from fastapi import FastAPI 
from app.api.router import api_router 
from app.core.config import settings 


def create_app() -> FastAPI:
    app = FastAPI(
        title = 'InsightLoop',
        version="0.0.1",
        description="Backend API for InsightAPI GenAI Conversational Insight Engine."
    )

    app.include_router(api_router, prefix="/api/v1")
    return app 


app = create_app()