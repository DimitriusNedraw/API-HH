from typing import List
from pydantic import BaseModel, Field


class MetroStation(BaseModel):
    station_id: str
    station_name: str
    line_id: str
    line_name: str
    lat: float | None
    lng: float | None

class Address(BaseModel):
    city: str | None
    street: str | None
    building: str | None
    description: str | None
    lat: float | None
    lng: float | None
    metro_stations: List[MetroStation]







    