from abc import ABC, abstractmethod
import json

from src.class_vacancies import VacanciesHH


class WorkWithFile(ABC):
    """Абстрактный класс для добавления вакансий в файл, получения данных из файла по указанным критериям и удаления
    информации о вакансиях."""
    @abstractmethod
    def add_vacancy(self, *args, **kwargs):
        pass

    @abstractmethod
    def get_vacancy(self):
        pass

    @abstractmethod
    def del_vacancy(self):
        pass


class SaveJson(WorkWithFile):
    """Класс для сохранения информации о вакансиях в json file"""
    def __init__(self, file_name="vacancies.json"):
        self.file_name = f"{file_name}"

    def add_vacancy(self, vacancy_data):
        """Добавляет вакансии в файл json."""
        with open(self.file_name, 'w') as file:
            json.dump(vacancy_data, file, ensure_ascii=False, indent=4)

    def get_vacancy(self):
        """Получает данные по вакансиям из файла."""
        with open(self.file_name, 'r') as file:
            data = json.load(file)
            vacancies = []
            for vacancy in data:
                vacancies.append(VacanciesHH(
                    name=vacancy['name'],
                    salary_from=vacancy['salary']['from'],
                    salary_to=vacancy['salary']['to'],
                    url=vacancy['alternate_url'],
                    employer=vacancy['employer']['name']
                ))
            return vacancies

    def del_vacancy(self):
        """Удаляет информацию о вакансиях."""
        pass