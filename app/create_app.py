from fastapi import FastAPI

from app.api.v1.routes import router as v1_router


def create_app() -> FastAPI:
    app = FastAPI(
        title="FastAPI Template",
        version="1.0.0",
        description="Template API with authentication and authorization examples",
    )
    app.include_router(v1_router, prefix="/v1", tags=["v1"])
    return app
