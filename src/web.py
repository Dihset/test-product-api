from fastapi import FastAPI

from src.api.v1.router import api_router as api_router_v1


def web_app_factory():
    app = FastAPI()

    api_v1 = FastAPI()
    api_v1.include_router(api_router_v1)

    app.mount("/api/v1", api_v1)
    return app
