from fastapi import FastAPI
from routers.auth_router import router as auth_router
from routers.mission_router import router as mission_router

app = FastAPI()
app.include_router(auth_router)
app.include_router(mission_router)



