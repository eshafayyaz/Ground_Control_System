from fastapi import APIRouter, HTTPException, Depends
from typing import List
import services.drone_service as drone_service_module
from schemas.drone_schema import AssignDroneMissionRequest, AssignDroneMissionResponse
from entities.drone import Drone
from services.drone_service import DroneService

router = APIRouter()

def get_drone_service() -> DroneService:
    if not drone_service_module.drone_service:
        raise HTTPException(status_code=503, detail="Drone service not initialized")
    return drone_service_module.drone_service

@router.post("/assign_mission", response_model=AssignDroneMissionResponse)
async def assign_mission(
    request: AssignDroneMissionRequest,
    service: DroneService = Depends(get_drone_service)
) -> AssignDroneMissionResponse:
    try:
        return await service.assign_mission(request.drone_id, request.mission_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")

@router.get("/drones", response_model=List[Drone])
async def get_all_drones(
    service: DroneService = Depends(get_drone_service)
) -> List[Drone]:
    try:
        return await service.get_all_drones()
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")