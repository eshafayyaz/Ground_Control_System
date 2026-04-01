from fastapi import APIRouter, HTTPException
from typing import List
import services.drone_service as drone_service_module
from schemas.drone_schema import AssignDroneMissionRequest, AssignDroneMissionResponse
from entities.drone import Drone

router = APIRouter()

@router.post("/assign_mission", response_model=AssignDroneMissionResponse)
async def assign_mission(request: AssignDroneMissionRequest):
    try:
        return await drone_service_module.drone_service.assign_mission(request.drone_id, request.mission_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")

@router.get("/drones", response_model=List[Drone])
async def get_all_drones():
    try:
        return await drone_service_module.drone_service.get_all_drones()
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")