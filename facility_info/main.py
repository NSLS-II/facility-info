from fastapi import Depends, FastAPI, Header, HTTPException

from .routers import users, experiments, proposals, facilities, instruments, resources, safs

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

app.include_router(facilities.router,
    prefix='/facilities',
    tags=['facilities'],
    responses={404: {"description": "Not found"}}
)

app.include_router(instruments.router,
    prefix='/instruments',
    tags=['instruments'],
    responses={404: {"description": "Not found"}}
)

app.include_router(resources.router,
    prefix='/resources',
    tags=['resources'],
    responses={404: {"description": "Not found"}}
)

app.include_router(safs.router,
    prefix='/safs',
    tags=['safs'],
    responses={404: {"description": "Not found"}}
)

