from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def run_simulation():
    return {"message": "Simulation executed successfully!"}
