from fastapi import Depends, FastAPI, Header, HTTPException

from .routers import users, experiments, proposals

app = FastAPI(
    title="UserInformation HTTP Server",
    description="The HTTP API server for the UserInformation project",
    version="0.0.1",
)

app.include_router(experiments.router,
    prefix='/experiments',
    tags=['experiments'],
    responses={404: {"description": "Not found"}}
)

app.include_router(users.router,
    prefix='/users',
    tags=['users'],
    responses={404: {"description": "Not found"}}
)

app.include_router(proposals.router,
    prefix='/proposals',
    tags=['proposals'],
    responses={404: {"description": "Not found"}}
)

