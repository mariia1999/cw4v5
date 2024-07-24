class VacanciesHH:
    """Класс для работы с вакансиями."""
    def __init__(self, name, url, salary_from, salary_to, currency, employer):
        self.name = name
        self.url = url
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.currency = currency
        self.employer = employer
        self.validate_data()

    def __repr__(self):
        """Строковое представление объекта класса VacanciesHH"""
        return f"""
        Название вакансии: {self.name}
        Зарплата: {self.salary_from} - {self.salary_to} {self.currency}
        Работодатель: {self.employer}
        Ссылка на вакансию: {self.url}
        """

    def __gt__(self, other):
        """Сравнивает вакансии между собой."""
        return self.salary_from > other.salary_from

    def validate_data(self):
        """Валидирует данные, которыми инициализируются атрибуты"""
        if not self.salary_from and not self.salary_to:
            self.salary_from = 0
        elif not self.salary_from:
            self.salary_from = 0
        elif not self.salary_to:
            self.salary_to = 0