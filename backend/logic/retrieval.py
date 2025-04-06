from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def retrieve_cargo():
    return {"message": "Cargo retrieved successfully!"}
