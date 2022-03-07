from requests import Session
import json

class ContextRequester:
    def __init__(self, BASE_URL, session: Session):
        self.__BASE_URL = BASE_URL
        self.__session = session

    def me(self):
        pass
