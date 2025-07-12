from fastapi import APIRouter

router = APIRouter()

@router.get("/", summary="System Base Route")
async def base_route():
    return {"message": "Welcome to Metrics Monitoring System"}