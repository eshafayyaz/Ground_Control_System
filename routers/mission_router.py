from fastapi import APIRouter, HTTPException, Depends
from schemas.mission_schema import MissionCreateRequest, MissionCreateResponse, MissionResponse, StartMissionResponse
from services.mission_service import MissionService
from data_layer.db_context import DbContext

router = APIRouter()
mission_service = MissionService(DbContext())

def get_mission_service() -> MissionService:
    return mission_service  # Same instance return ho

@router.post("/missions", response_model=MissionCreateResponse)
async def create_mission(request: MissionCreateRequest, service: MissionService = Depends(get_mission_service)):
    try:
        await service.create_mission(request.mission_id, request.name, request.description, request.tasks)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    return MissionCreateResponse(success=True, message="Mission created successfully")

@router.get("/missions", response_model=list[MissionResponse])
async def get_all_missions(service: MissionService = Depends(get_mission_service)):
    return await service.get_all_missions()
@router.post("/missions/{mission_id}/start", response_model=StartMissionResponse)
async def start_mission(mission_id: int, service: MissionService = Depends(get_mission_service)):
    try:
        mission = await service.start_mission(mission_id)
        return StartMissionResponse(
            success=True,
            message=f"Mission '{mission.name}' started successfully",
            mission_id=mission.mission_id,
            mission_name=mission.name,
            status=mission.status,
            tasks_count=len(mission.tasks)
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))