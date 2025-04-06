from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def test_waste():
    return {"message": "Waste management endpoint is working!"}
