from typing import List
from pydantic import BaseModel, Field


class Skill(BaseModel):
    name: str

class Schedule(BaseModel):
    id: str
    name: str

class Experience(BaseModel):
    id: str
    name: str

class MetroStations(BaseModel):
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
    metro_stations: List[MetroStations]

class Department(BaseModel):
    id: str
    name: str

class Employment(BaseModel):
    id: str
    name: str

class Salary(BaseModel):
    from_salary: float = Field(default=None, alias='from')
    to_salary: float = Field(default=None, alias='to')
    gross: bool | None
    currency: str

class InsiderInterviewSmall(BaseModel):
    id: str
    url: str

class InsiderInterview(InsiderInterviewSmall):
    title: str

class Area(BaseModel):
    id: str
    name: str
    url: str

class Industry(BaseModel):
    id: str
    name: str

class EmployerSmall(BaseModel):
    logo_urls: dict | None
    name: str
    alternate_url: str
    id: str
    trusted: bool





class Employer(EmployerSmall):
    
   
    type: str | None
    site_url: str
    description: str | None
    branded_description: str | None
    vacancies_url: str
    open_vacancies: int
    
    
    insider_interviews: List[InsiderInterview]
    
    area: Area
    relations: List[str]
    industries: List[Industry]

class VacancyType(BaseModel):
    id: str
    name: str

class Test(BaseModel):
    required: bool

class Contacts(BaseModel):
    class Phone(BaseModel):
        country: str
        city: str
        number: str
        comment: str | None
    name: str | None
    email: str | None
    phones: List[Phone]

class BillingType(BaseModel):
    id: str
    name: str

class DriverLicenseType(BaseModel):
    id: str

class WorkingDays(BaseModel):
    id: str
    name: str

class WorkingTimeIntervals(BaseModel):
    id: str
    name: str

class WorkingTimeModes(BaseModel):
    id: str
    name: str

class ProfessionalRole(BaseModel):
    id: str
    name: str






    