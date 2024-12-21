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
        """Расчёт возраста"""
        today = self.death_date or datetime.date.today()
        years = today.year - self.birth_date.year

        if (today.month, today.day) < (self.birth_date.month, self.birth_date.day):
            years -= 1
        return years

    def gender_check(self):
        if self.gender == 'm':
            return True
        else:
            return False

    def __str__(self):
        """Вывод информации о персоне"""
        gender_str = "мужчина" if self.gender_check() else "женщина"
        birth_name = "Родился" if self.gender_check() else "Родилась"
        death_name = "Умер" if self.gender_check() else "Умерла"
        age = self.calculate_age()

        if age % 10 == 1 and age % 100 != 11:
            age_str = f"{age} год"
        elif 2 <= age % 10 <= 4 and not (12 <= age % 100 <= 14):
            age_str = f"{age} года"
        else:
            age_str = f"{age} лет"

        death_info = f"{death_name}: {self.death_date}" if self.death_date else "Жив(а)"
        return f"{self.first_name} {self.last_name} {self.patronymic}, {age_str}, {gender_str}. " \
               f"{birth_name}: {self.birth_date}. {death_info}"