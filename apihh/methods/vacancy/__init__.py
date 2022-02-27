from requests import Session
import json
from .responses import Vacancy


class VacancyRequester:
    def __init__(self, BASE_URL, session: Session):
        self.__BASE_URL = BASE_URL
        self.__session = session

    def get_vacancy(self, id:str):
        method = 'vacancies/'
        url_path = self.__BASE_URL + method + id
        response = self.__session.get(url_path)
        response = json.loads(response.text)
        response = Vacancy.parse_obj(response)
                  
        return response