from fastapi import FastAPI

app = FastAPI()

data = []

@app.get("/shipments")
def get_shipments():
    return data

@app.post("/shipments")
def create_shipment(shipment: dict):
    data.append(shipment)
    return shipment

