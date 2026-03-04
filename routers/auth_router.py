from fastapi import APIRouter, HTTPException
from schemas.auth_schema import LoginRequest, LoginResponse
from services.auth_service import AuthService
from data_layer.db_context import DbContext

router = APIRouter()
auth_service = AuthService(DbContext())

@router.post("/login", response_model=LoginResponse)
def login(request: LoginRequest):
    try:
        auth_service.login(request.email, request.password)
    except ValueError as e:
        raise HTTPException(status_code=401, detail=str(e))

    return LoginResponse(success=True, message="Login successful")
