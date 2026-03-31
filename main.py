from fastapi import FastAPI
from routers.auth_router import router as auth_router
from routers.mission_router import router as mission_router
from routers.drone_router import router as drone_router

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Ground Control System API", "status": "running"}

app.include_router(auth_router)
app.include_router(mission_router)
app.include_router(drone_router)


