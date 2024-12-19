import datetime


class Person:
    def __init__(self, first_name, last_name='', patronymic='', birth_date='', death_date='', gender='m'):
        if not first_name:
            raise ValueError("Имя обязательно!")
        self.first_name = first_name
        self.last_name = last_name
        self.patronymic = patronymic
        self.birth_date = self.parse_date(birth_date)
        self.death_date = self.parse_date(death_date) if death_date else None
        self.gender = gender

    def parse_date(self, date_str):
        """Парсинг даты в формат datetime.date"""
        for fmt in ("%d.%m.%Y", "%d %m %Y", "%d/%m/%Y", "%d-%m-%Y"):
            try:
                return datetime.datetime.strptime(date_str, fmt).date()
            except ValueError:
                continue
        raise ValueError("Неверный формат даты!")

    def calculate_age(self):
        """Вычисление возраста"""
        end_date = self.death_date or datetime.date.today()
        delta = end_date - self.birth_date
        return delta.days // 365

    def __str__(self):
        """Форматированный вывод информации"""
        gender_str = "мужчина" if self.gender == 'm' else "женщина"
        age = self.calculate_age()
        death_info = f"Умер(ла): {self.death_date}" if self.death_date else "Жив(а)"
        return f"{self.first_name} {self.last_name} {self.patronymic}, {age} лет, {gender_str}. " \
               f"Родился: {self.birth_date}. {death_info}"