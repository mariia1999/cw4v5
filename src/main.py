from src.class_HH_API import HeadHunterApi
from src.class_vacancies import VacanciesHH
from src.class_json import SaveJson
from src.utils import filter_by_salary, filter_by_keyword


# Функция для взаимодействия с пользователем
def user_interaction():
    search_query = input("Введите название вакансии: ").lower()
    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
    salary_range = input("Введите диапазон зарплат в формате мин зарпалата - макс зарплата: ")
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))

    # Создание экземпляра класса для работы с API сайтов с вакансиями
    hh = HeadHunterApi()

    # Подключаемся к API и получаем вакансии по ключевому слову
    hh_vacancies = hh.load_vacancies(search_query)

    file_worker = SaveJson('data/vacancies.json')  # название файла, куда будут сохраняться вакансии
    file_worker.add_vacancy(hh_vacancies)

    vacancies = [
        VacanciesHH(
            name=vacancy['name'],
            url=vacancy['url'],
            salary_from=vacancy['salary'].get('from') if vacancy['salary'] else 0,
            salary_to=vacancy['salary'].get('to') if vacancy['salary'] else 0,
            currency=vacancy['salary'].get('currency') if vacancy['salary'] else '',
            employer=vacancy['employer']['name'])
        for vacancy in file_worker.get_vacancy()['items']]

    filtered_vacancies = filter_by_keyword(vacancies, filter_words)
    ranged_vacancies = filter_by_salary(filtered_vacancies, salary_range)
    sorted_vacancies = sorted(ranged_vacancies, reverse=True)
    top_ranged_vacancies = sorted_vacancies[:top_n]
    print(top_ranged_vacancies)


user_interaction()
