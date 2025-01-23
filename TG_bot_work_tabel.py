from datetime import datetime
class Company:
    def __init__(self, name_company):
        self.name_company = name_company
        self.notes = [] # Список работ, связанных с этой компанией


class Note:
    def __init__(self,company_name,  place, work):
        self.date = datetime.now()  # Дата создания записи
        self.company_name = company_name  # Название компании
        self.place = place  # Место работы
        self.work = work           # Описание выполненных работ

class NoteManager:
    def __init__(self):
        self.companys = {}  # словарь компаний
        self.notes = []  #Общий стек всех записей(список объектов Note

    def add_company(self, name_company):
        if name_company in self.companys:
            raise ValueError("Компания с таким названием уже существует.")
        self.companys[name_company] = Company(name_company)

    def add_work(self, name_company, place, work):
        task = Note(place, work)
        self.companys[name_company].notes.append(task)



manager = NoteManager()
name_company = input('Введите название компании - ')
manager.add_company(name_company)
place = input('Место работы - ')
work = input('Что было сделано - ')
manager.add_work(name_company, place,work)

print('Ваш табель:')
for company_name, company in manager.companys.items():
    print(f"Компания: {company_name}")
    for note in company.notes:
        formatted_date = note.date.strftime("%d.%m")
        print(formatted_date,' - ', note.place,' - ', note.work)
