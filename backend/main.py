from fastapi import FastAPI
from logic import placement, retrieval, waste, simulation

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Space Cargo Management System!"}

app.include_router(placement.router, prefix="/placement", tags=["Placement"])
app.include_router(retrieval.router, prefix="/retrieval", tags=["Retrieval"])
app.include_router(waste.router, prefix="/waste", tags=["Waste Management"])
app.include_router(simulation.router, prefix="/simulation", tags=["Simulation"])
