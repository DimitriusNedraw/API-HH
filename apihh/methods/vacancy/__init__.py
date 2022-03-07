from datetime import datetime
from typing import List
from requests import Session
import json


class VacancyRequester:
    def __init__(self, BASE_URL, session: Session):
        self.__BASE_URL = BASE_URL
        self.__session = session

    def get_vacancy(self, id:str):
        pass


    def get_vacancies(
        text: str | None = None,
        search_fields: List[str] | None = None,
        experience: str | None = None,
        employment: str | None = None,
        schedule: str | None = None,
        area: str | None = None,
        metro: str | None = None,
        industry: str | None = None,
        employers_id: List[str] | None = None,
        currency: str | None = None,
        salary: int | None = None,
        only_with_salary: bool | None = None,
        label: List[str] | None = None,
        period: int | None = None,
        date_from: datetime | None = None,
        date_to: datetime | None = None,
        top_lat: float | None = None,
        bottom_lat: float | None = None,
        left_lng: float | None = None,
        right_lng: float | None = None,
        order_by: str | None = None,
        sort_point_lat: float | None = None,
        sort_point_lng: float | None = None,
        clusters: bool | None = None,
        describe_arguments: bool | None = None,
        per_page: int | None = None,
        page: int | None = None,
        no_magic:bool | None = None,
        premium: bool | None = None,
        responses_count_enabled: bool | None = None,
        part_time: List[str] | None = None,
        professional_role: List[str] | None = None
    ):
        pass