from fastapi import APIRouter, HTTPException, Depends
from schemas.mission_schema import MissionCreateRequest, MissionCreateResponse, MissionResponse
from services.mission_service import MissionService
from data_layer.db_context import DbContext

router = APIRouter()


def get_mission_service() -> MissionService:
    return MissionService(DbContext())


@router.post("/missions", response_model=MissionCreateResponse)
async def create_mission(request: MissionCreateRequest, service: MissionService = Depends(get_mission_service)):
    try:
        await service.create_mission(request.mission_id, request.name, request.description)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    return MissionCreateResponse(success=True, message="Mission created successfully")


@router.get("/missions", response_model=list[MissionResponse])
async def get_all_missions(service: MissionService = Depends(get_mission_service)):
    return await service.get_all_missions()
