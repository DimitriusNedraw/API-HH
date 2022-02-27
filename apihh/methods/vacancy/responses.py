from datetime import datetime
from pydantic import BaseModel
from typing import List
from ...models import Address, Area, BillingType, Contacts, DriverLicenseType, EmployerSmall, Experience, ProfessionalRole, Salary, Schedule, Skill, Department, Employment, InsiderInterviewSmall, Test, VacancyType, WorkingDays, WorkingTimeIntervals, WorkingTimeModes


class EmployerForVacancy(EmployerSmall):
    url: str
    blacklisted: bool | None



class Vacancy(BaseModel):   
    id: str
    description: str
    branded_description: str | None
    key_skills: List[Skill]
    schedule: Schedule
    accept_handicapped: bool
    accept_kids: bool
    experience: Experience
    address: Address | None
    alternate_url: str
    apply_alternate_url: str
    code: str | None
    department: Department | None
    employment: Employment | None
    salary: Salary | None
    archived: bool
    name: str
    insider_interview: InsiderInterviewSmall | None
    area: Area
    created_at: datetime
    published_at: datetime
    employer: EmployerForVacancy
    response_letter_required: bool
    type: VacancyType
    has_test: bool
    response_url: str | None
    test: Test | None
    contacts: Contacts | None
    billing_type: BillingType
    allow_messages: bool
    premium: bool
    driver_license_types: List[DriverLicenseType]
    accept_incomplete_resumes: bool
    working_days: List[WorkingDays]
    working_time_intervals: List[WorkingTimeIntervals]
    working_time_modes: List[WorkingTimeModes]
    accept_temporary: bool | None
    professional_roles: List[ProfessionalRole]






