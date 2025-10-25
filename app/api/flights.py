from fastapi import APIRouter, HTTPException, Depends
from datetime import date
from app.models.flight import Flight
from app.core.security import api_key_auth

router = APIRouter(tags=["flights"])

_DB: dict[str, Flight] = {
    "IB123": Flight(id="IB123", origin="MAD", destination="BCN", departure=date(2025, 7, 1)),
    "UX456": Flight(id="UX456", origin="MAD", destination="PMI", departure=date(2025, 7, 2)),
}

@router.get("/", response_model=list[Flight], summary="Listar vuelos")
def list_flights(auth: bool = Depends(api_key_auth)):
    return list(_DB.values())

@router.get("/{flight_id}", response_model=Flight, summary="Obtener vuelo por ID")
def get_flight(flight_id: str, auth: bool = Depends(api_key_auth)):
    f = _DB.get(flight_id)
    if not f:
        raise HTTPException(status_code=404, detail="Flight not found")
    return f

@router.post("/{flight_id}/change-date", response_model=Flight, summary="Cambiar fecha de vuelo")
def change_date(flight_id: str, new_date: date, auth: bool = Depends(api_key_auth)):
    f = _DB.get(flight_id)
    if not f:
        raise HTTPException(status_code=404, detail="Flight not found")
    if new_date <= date.today():
        raise HTTPException(status_code=400, detail="New date must be in the future")
    f.departure = new_date
    _DB[flight_id] = f
    return f
