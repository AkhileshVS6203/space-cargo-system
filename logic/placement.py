from fastapi import APIRouter

router = APIRouter()

@router.post("/")
def place_cargo():
    return {"message": "Cargo placed successfully!"}
