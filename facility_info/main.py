from fastapi import Depends, FastAPI, Header, HTTPException

from .routers import user_info, experiments

app = FastAPI(
    title="UserInformation HTTP Server",
    description="The HTTP API server for the UserInformation project",
    version="0.0.1",
)

app.include_router(user_info.router,
    prefix='/user_info',
    tags=["user_info"],
    responses={404: {"description": "Not found"}}
)
app.include_router(experiments.router,
    prefix='/experiments',
    tags=['experiments'],
    responses={404: {"description": "Not found"}}
)
