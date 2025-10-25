from pydantic import BaseModel, Field
from datetime import date

class Flight(BaseModel):
    id: str
    origin: str
    destination: str
    departure: date
    status: str = Field(default="scheduled", description="scheduled|delayed|cancelled")
