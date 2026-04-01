from fastapi import FastAPI
from contextlib import asynccontextmanager
from routers.auth_router import router as auth_router
from routers.mission_router import router as mission_router
from routers.drone_router import router as drone_router
from routers.mission_router import mission_service
from services.drone_service import DroneService
import services.drone_service as drone_service_module

@asynccontextmanager
async def lifespan(app: FastAPI):
    drone_service_module.drone_service = DroneService(mission_service)
    yield
    if drone_service_module.drone_service:
        await drone_service_module.drone_service.close()

app = FastAPI(lifespan=lifespan)

app.include_router(auth_router)
app.include_router(mission_router)
app.include_router(drone_router)


