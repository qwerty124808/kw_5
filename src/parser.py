import requests
import json
import time
from src.data_to_be_process import Data


class ParsingError(Exception):
    def __str__(self):
        return "Ошибка подключения данных по API." 

class Parser():

    def __init__(self):
        self.__header = {
        "User-Agent": "unknown"
        }

        self.__employers_id = [3529, 1808, 4181, 988387, 5817234, 78638, 6596, 907345, 3607, 12550]
        self.__employers = []
        self.__vacansys_lists = []


    def get_employers(self):
        """ функция получения информации по работодателям """
        for id in self.__employers_id:
            print(f"роботодатель {id}")
            employer = Parser.response(self, id)
            employer_url = f'https://api.hh.ru/employers/{id}'
            vacanci_url = employer["vacancies_url"]
            employer_id = employer["id"]
            employer_name = employer["name"]
            vacancies_list = []
            count = 0
            response = requests.get(vacanci_url)
            if response.status_code != 200:
                raise ParsingEror()
            vacancies_list.extend(response.json()["items"][0 : 10]) 
            self.__vacansys_lists.append(Data(employer_name, employer_id, employer_url, vacancies_list))
        return self.__vacansys_lists
            

    def response(self, id):
        """ Возвращает результат запроса """
        response = requests.get(f'https://api.hh.ru/employers/{id}',
                                headers=self.__header,
                                )                      
        if response.status_code != 200:
            raise ParsingEror()
        return response.json()


