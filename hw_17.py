# Выбрать систему, которая может быть описана несколькими классами.
# Описать используя классы и применить принципы ООП:
# - Наследование
# - Абстрактные классы и/или интерфейсы
# - Сокрытие
# - Инкапсуляция
# У классов должно быть состояние (поля) и реализация поведения через методы.
# Требований к типам полей (экземпляра/класса) и
# методов (экземпляра/класса/статические) нет, по необходимости как вы видите.
# Написать код который создает необходимые экземпляры и демонстрирует работу систему.
# Ограничений на количество классов нет, но конечно их тут будет не пара.
# Это задание на это и следующие занятие.
# Пока советую выбрать систему, и порисовать из чего она состоит.

# hw_18
# Создать диаграмму классов для системы из домашнего задания №12
# Прикрепить ссылку на расшаренную диаграмму созданную в draw.io


# ___________________________________________________________________________________________________________________#
# information about the procedure for selecting candidates from among employees - for transfer to the main office.   #
# information about candidates(name, age, education),                                                                #
# information about the interview - number of points(interview_assessment),                                          #
# information about the decision of the management(management_decision)                                              #
# ___________________________________________________________________________________________________________________#
from abc import ABC, ABCMeta, abstractmethod, abstractclassmethod, abstractstaticmethod
from datetime import datetime, date

data_company = []  # office data
data_client = []  # Client
data_employee = []  # Employee
current_date = date.today()


# class Data_company
class Data_company(
    ABC):  # class Data (number(___), name("_", day of birthday("__/__/__"), status("client, employee, manager")

    def __init__(self, num, name, dob, status):  # method of object - constructor of class Data_company
        self.num = num
        self.name = name
        self.dob = dob
        self.status = status

    @abstractclassmethod  # abstractmethod of object - write to text file
    def write_info(info):
        with open("Data_company.txt", "a") as file:
            file.write(info)

    def get_num(self):  # method of object - database number
        return self.num

    def get_name(self):  # method of object - name
        return self.name

    def get_dob(self, name):  # method of object - date of birth
        return self.dob

    def get_status(self):  # method of object - status
        return self.status

    def print_data_company_info(self):  # method of object - print data company
        print(f"""
        number: {self.num}
        name: {self.name}
        date of birth: {self.dob}
        status: {self.status}
        """)

    @staticmethod  # staticmethod - date issue
    def get_date():
        return current_date

    @staticmethod  # staticmethod - age
    def get_age(c):
        age = datetime.strptime(c, "%d/%m/%Y")
        today = date.today()
        k = int(date(today.year, age.month, age.day) > today)
        age1 = today.year - age.year - k
        return age1


# class Employee
class Employee(
    Data_company):  # class Employee(number(___), name("_", day of birthday("__/__/__"), status("client, employee, manager"), education("_"),position("_"), salary(_)
    def __init__(self, num, name, dob, status, education, position, salary):
        super().__init__(num, name, dob, status)  # referencing the superclass Data_company
        self.education = education
        self.position = position
        self._salary = salary  # protected info - salary
        self.__bonus = 100  # privat info - bonus

    def get_position(self):
        return self.position

    # BONUS - work with information on salary bonuses
    def get_bonus(self):
        return self.__bonus

    def set_bonus(self, new_bonus):
        self.__bonus = new_bonus

    def delete_bonus(self):
        p = "no bonus"
        del self.__bonus
        return p

    bonus = property(fget=get_bonus, fset=set_bonus, fdel=delete_bonus, doc="Bonus of employee")

    def __get_salary(self, name):  # method of object
        return self._salary

    @staticmethod
    def write_info(info):
        with open("Employee.txt", "a") as file:
            file.write(info + "\n")

    @staticmethod
    def convert_list_to_dict(employee_list):
        mapping = {"name": 0,
                   "position": 1,
                   "salary": 2}
        for employee in employee_list:
            employee_as_dict = dict()
            employee_as_dict["name"] = employee[mapping["name"]]
            employee_as_dict["position"] = employee[mapping["position"]]
            employee_as_dict["salary"] = employee[mapping["salary"]]
            data_employee.append(employee_as_dict)
        return data_employee


# class Client
class Client(Data_company):
    def __init__(self, num, name, dob, status, discount, orders):
        super().__init__(num, name, dob, status)
        self.discount = discount
        self.orders = orders

    def get_orders(self):
        return self.orders

    @staticmethod
    def write_info(info):
        with open("Client.txt", "a") as file:
            file.write(info + "\n")

    @staticmethod
    def convert_list_to_dict(client_list):
        mapping = {"name": 0,
                   "orders": 1}
        for client in client_list:
            client_as_dict = dict()
            client_as_dict["name"] = client[mapping["name"]]
            client_as_dict["orders"] = client[mapping["orders"]]
            data_client.append(client_as_dict)
        return data_client


# class Office
class Office(Data_company):  # class creation - Company
    def __init__(self, num, name, dob, status, town, number_employees, performance_evaluation):
        super().__init__(num, name, dob, status)
        self.town = town
        self.number_employees = number_employees
        self.performance_evaluation = performance_evaluation

    def get_town(self, name):  # method of object
        return self.town

    def get_performance_evaluation(self):  # method of object
        return self.performance_evaluation

    def print_company_info(self):  # method of object
        print(f"""
        number of office: {self.num}
        name of office: {self.name}
        town: {self.town}
        number of employees: {self.number_employees}
        performance evaluation:{self.performance_evaluation}
        """)

    # method of processing and processing information about the activities of the office - office code, indicator
    @staticmethod
    def convert_list_to_dict(office_list):
        mapping = {"name of office": 0,
                   "performance evaluation": 1}
        for office in office_list:
            office_as_dict = dict()
            office_as_dict["name of office"] = office[mapping["name of office"]]
            office_as_dict["performance evaluation"] = office[mapping["performance evaluation"]]
            data_company.append(office_as_dict)
        return data_company

    # recording information about the activities of offices in a file "data.txt"
    @staticmethod
    def write_info(info):
        with open("Office.txt", "a") as file:
            file.write(info + "\n")


# input data

#  Employee
andrew = Employee(100, "Andrew Stishkov", "07/03/1977", "Manager", "Dniprovskiy Technical University", "Director", 2500)
bogdan = Employee(101, "Bogdan Bogdanov", "08/04/1978", "Manager", "Dnipropetrovskiy University", "Director", 2500)
viktor = Employee(102, "Viktor Viktorov", "09/05/1979", "Manager", "Dniprovskiy Technical University", "Director", 2500)
# Client
anna = Client(201, "Anna Galka", "10/06/1980", "Client", 10, "(10/01 - 1200)(11/01 -1300")
viktoria = Client(202, "Viktoria Hilko", "11/07/1980", "Client", 3, "(10/01 - 100)(11/01 -1000")
galina = Client(203, "Galina Vasilkovskaya", "12/08/1980", "Client", 5, "(10/01 - 1000)(11/01 -300")
# Office
dnipro = Office(300, "Ukraine-Dnipro", "20/06/2000", "Main office", "Dnipro", 5, 75)
kyiv = Office(301, "Ukraine-Kyiv", "10/03/2010", "Kyiv office", "Kyiv", 10, 95)
lviv = Office(302, "Ukraine-Lviv", "30/07/2003", "Lviv office", "Lviv", 3, 56)

# Work of programm:
print(f"Current date: {Data_company.get_date()}")
# print objects:
print("Data Company:")
# number in data
dnipro = Data_company.get_num(dnipro)
print(f"Dnipro office in database number - {dnipro}")
# status in database
g_s = Data_company.get_status(galina)
g_n = Data_company.get_name(galina)
print(f"{g_n} in database is {g_s}")
# information about the office in Lviv in database
print("Information about office:")
print(Office.print_company_info(lviv))
# information about privat data (salary)
print(f"Information about salary {Data_company.get_name(bogdan)}")
print(bogdan._Employee__get_salary(bogdan))
# age output (full years)
b = bogdan.get_dob(bogdan)
l = Data_company.get_age(b)
print(f"Full years:{bogdan.get_name()} - {l} ")
# calling salary information in a private method + protected data
print(f"Information about salary {Data_company.get_name(andrew)}")
print(andrew._Employee__get_salary(andrew))
# (privat data) bonus output
print(f"Information about Andrew`s bonus 2 month ago : {andrew.bonus}")
andrew.bonus = 150
print(f"Information about Andrew`s bonus 1 month ago : {andrew.bonus}")
print(f"Information about Andrew`s bonus today : {andrew.delete_bonus()}")

# write info employee database in text file
info = str(Data_company.get_date())
Employee.write_info(info)
nam = Data_company.get_name(bogdan)
pos = Employee.get_position(bogdan)
sal = bogdan._Employee__get_salary(bogdan)
employee_list = [[nam, pos, sal]]
p = Employee.convert_list_to_dict(employee_list)
info = str(p)
Employee.write_info(info)
# read info in file Employee.txt
print("reading information from a file:")
with open(r"Employee.txt", "r") as file:
    for line in file:
        print(line)

# write info client database in text file
info = str(Data_company.get_date())
Client.write_info(info)
nam = Data_company.get_name(anna)
orde = Client.get_orders(anna)
client_list = [[nam, orde]]
p = Client.convert_list_to_dict(client_list)
info = str(p)
Client.write_info(info)
# read info in file Client.txt
print("reading information from a file:")
with open(r"Client.txt", "r") as file:
    for line in file:
        print(line)

# write info office database in text file
info = str(Data_company.get_date())
Office.write_info(info)
nam = Data_company.get_name(lviv)
perf = Office.get_performance_evaluation(lviv)
office_list = [[nam, perf]]
p = Office.convert_list_to_dict(office_list)
info = str(p)
Office.write_info(info)
# read info in file Office.txt
print("reading information from a file:")
with open(r"Office.txt", "r") as file:
    for line in file:
        print(line)
