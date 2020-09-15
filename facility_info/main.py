from fastapi import Depends, FastAPI, Header, HTTPException

from .routers import user_info, expt_session

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
app.include_router(expt_session.router,
    prefix='/expt_session',
    tags=['expt_session'],
    responses={404: {"description": "Not found"}}
)
