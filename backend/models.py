from pydantic import BaseModel

class CargoItem(BaseModel):
    id: int
    name: str
    weight: float
    destination: str

class WasteItem(BaseModel):
    id: int
    type: str
    hazard_level: int

class SimulationResult(BaseModel):
    success: bool
    message: str
