import json
from person import Person


class Database:
    def __init__(self):
        self.people = []

    def add_person(self, person):
        self.people.append(person)

    def search(self, query):
        """Поиск по имени, фамилии или отчеству"""
        query = query.lower()
        return [person for person in self.people
                if query in person.first_name.lower() or
                   query in person.last_name.lower() or
                   query in person.patronymic.lower()]

    def save_to_file(self, filename):
        """Сохранение в JSON файл"""
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump([self.person_to_dict(person) for person in self.people], f, ensure_ascii=False, indent=4)

    def load_from_file(self, filename):
        """Загрузка из JSON файла"""
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
        self.people = [self.dict_to_person(item) for item in data]

    def person_to_dict(self, person):
        """Преобразование объекта Person в словарь"""
        return {
            "first_name": person.first_name,
            "last_name": person.last_name,
            "patronymic": person.patronymic,
            "birth_date": person.birth_date.strftime("%d.%m.%Y"),
            "death_date": person.death_date.strftime("%d.%m.%Y") if person.death_date else None,
            "gender": person.gender
        }

    def dict_to_person(self, data):
        """Преобразование словаря в объект Person"""
        return Person(
            first_name=data['first_name'],
            last_name=data['last_name'],
            patronymic=data['patronymic'],
            birth_date=data['birth_date'],
            death_date=data['death_date'],
            gender=data['gender']
        )