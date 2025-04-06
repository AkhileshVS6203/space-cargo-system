from fastapi import APIRouter

router = APIRouter()

@router.delete("/")
def handle_waste():
    return {"message": "Waste disposed successfully!"}
