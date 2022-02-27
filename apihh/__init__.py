import requests
from .methods import context, vacancy



class APIHH:
    __BASE_URL = 'https://api.hh.ru/'
    __session: requests.Session
    __context = None
    __vacancy = None
    def __init__(self, access_token: str | None = None):
        self.__session = requests.session()
        if access_token is not None:    
            self.__session.headers.update({'Authorization': f'Bearer {access_token}'})
    
    @property
    def context(self):
        if self.__context is None:
            self.__context = context.Context(self.__BASE_URL, self.__session)
        return self.__context

    
    @property
    def vacancy(self):
        if self.__vacancy is None:
            self.__vacancy = vacancy.Vacancy(self.__BASE_URL, self.__session)
        return self.__vacancy





