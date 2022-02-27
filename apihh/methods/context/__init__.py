from requests import Session
import json
from . import responses

class Context:
    def __init__(self, BASE_URL, session: Session):
        self.__BASE_URL = BASE_URL
        self.__session = session

    def me(self) -> responses.MeEmployer | responses.MeApplication | responses.MeApplicant:
        method = 'me'
        url_path = self.__BASE_URL + method
        response = self.__session.get(url_path)
        response = json.loads(response.text)
        if response['is_application']:
            response = responses.MeApplication.parse_obj(response)
        elif response['is_applicant']:
            response = responses.MeApplicant.parse_obj(response)
        elif response['is_employer']:
            response = responses.MeEmployer.parse_obj(response)
                  
        return response
