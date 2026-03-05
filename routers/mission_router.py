from fastapi import APIRouter, HTTPException
from schemas.mission_schema import MissionCreateRequest, MissionCreateResponse, MissionResponse
from services.mission_service import MissionService

router = APIRouter()

mission_service = MissionService()


@router.post("/missions", response_model=MissionCreateResponse)
def create_mission(request: MissionCreateRequest):
    try:
        mission_service.create_mission(request.mission_id, request.name, request.description)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    return MissionCreateResponse(success=True, message="Mission created successfully")


@router.get("/missions", response_model=list[MissionResponse])
def get_all_missions():
    return mission_service.get_all_missions()
