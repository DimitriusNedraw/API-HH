from datetime import datetime
from pydantic import BaseModel

class BaseMeResponse(BaseModel):
    auth_type: str
    is_admin: bool
    is_applicant: bool
    is_application: bool
    is_employer: bool

class BaseEmployerAndApplicant(BaseMeResponse):
    email: str | None
    first_name: str
    id: str
    last_name: str
    middle_name: str | None
    phone: str | None




class MeApplicant(BaseEmployerAndApplicant):
    class MeApplicantProfileCounters(BaseModel):
        new_resume_views: int
        resumes_count: int
        unread_negotiations: int
    class UserStatuses(BaseModel):
        class JobSearchStatus(BaseModel):
            description: str | None
            id: str
            name: str
        class WhenCanStartWorkStatus(BaseModel):
            id: str
            name: str
        
        job_search_status: JobSearchStatus
        when_can_work_start_status: WhenCanStartWorkStatus

    counters: MeApplicantProfileCounters
    is_in_search: bool
    negotiations_url: str
    resumes_url: str
    user_statuses: UserStatuses


class MeApplication(BaseMeResponse):
    pass
    

class MeEmployer(BaseEmployerAndApplicant):
    class MeEmployerProfileCompany(BaseModel):
        id: str
        manager_id: str
        name: str
    class Manager(BaseModel):
        has_admin_rights: bool
        has_multiple_manager_accounts: bool
        id: str
        is_main_contact_person: bool
        manager_settings_url: str
    class MeEmployerProfilePersonalManager(BaseModel):
        class PhotoUrls(BaseModel):
            big: str | None
            small: str | None
        class Unavailable(BaseModel):
            until: datetime
        email: str
        first_name: str
        id: str
        is_available: bool
        last_name: str
        photo_urls: PhotoUrls | None
        unavailable: Unavailable | None

    employer: MeEmployerProfileCompany
    manager: Manager
    personal_manager: MeEmployerProfilePersonalManager

     