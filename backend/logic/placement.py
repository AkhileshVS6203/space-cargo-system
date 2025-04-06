from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def test_placement():
    return {"message": "Placement endpoint is working!"}
