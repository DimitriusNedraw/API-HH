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

class AreaBase(BaseModel):
    id: str
    name: str

class Area(AreaBase):
    parent_id: str | None
    areas: List['Area']
Area.update_forward_refs()

class Country(AreaBase):
    url: str

class Cluster(BaseModel):
    class Item(BaseModel):
        name: str
        url: str
        count: int
        type: str | None
    id: str
    name: str
    items: List[Item]

class ClusterTypeMetroLine(Cluster):
    class MetroLine(BaseModel):
        id: str
        hex_color: str
        area: Area
    metro_line: MetroLine

class ClusterTypeMetroStation(Cluster):
    class MetroStation(BaseModel):
        id: str
        hex_color: str
        lat: float
        lng: float
        order: int
        area: Area
    metro_station: MetroStation










    