# Создать классы Employee (сотрудник) и Company (компания).
# Классы должны содержать:
# минимум два поля экземпляров и одно поле класса
# минимум два метода экземпляра
# минимум один метод класса
# минимум один статический метод
# К методам добавить строки документации.
# Методы должные быть НЕ get/set поле, а что-то оригинальнее:)
# (но если надо их, тоже можно добавить)
# Написать код который создает несколько экземпляров и взаимодействует с объектами
# Задание в том числе и на фантазию

# ___________________________________________________________________________________________________________________#
# information about the procedure for selecting candidates from among employees - for transfer to the main office.   #
# information about candidates(name, age, education),                                                                #
# information about the interview - number of points(interview_assessment),                                          #
# information about the decision of the management(management_decision)                                              #
# ___________________________________________________________________________________________________________________#
result = []  # data array - submit to the manager for decision-making on applicants
a = "15.01.2023"  # date of issue


class Employee:  # class Employee (name, age, education, interview_assessment,management_decision)
    def __init__(self, name, age, education, interview_assessment, management_decision):
        self.name = name
        self.age = age
        self.education = education
        self.interview_assessment = interview_assessment
        self.management_decision = management_decision

    def get_name(self):  # method of object
        return self.name

    def get_age(self, name):  # method of object
        return self.age

    def get_education(self, name):  # method of object
        return self.education

    def print_employee_info(self):  # method of object
        print(f"""
        name: {self.name}
        age: {self.age}
        education: {self.education}
        interview assessment:{self.interview_assessment}
        management decision :{self.management_decision}
        """)

    @staticmethod  # staticmethod - date issue
    def get_date():
        return a

    @staticmethod  # staticmethod - submit to the manager for decision-making on applicants
    def convert_list_to_dict(persons_list):
        mapping = {"name": 0,
                   "interview assessment": 1}
        for person in persons_list:
            person_as_dict = dict()
            person_as_dict["name"] = person[mapping["name"]]
            person_as_dict["interview assessment"] = person[mapping["interview assessment"]]
            result.append(person_as_dict)
        return result

    @classmethod  # classmethod:     input of a new field - office, connection with the object
    def office_country(cls, name, age, education, interview_assessment, management_decision, office):
        instance = cls(name, age, education, interview_assessment, management_decision)
        instance.office = office
        return instance


# input objects:
john = Employee("John", 45, "National Dnipro University", 10, 1)  # object - john
tamara = Employee("Tamara", 35, "Dnipro High School", 6, 1)  # object - tamara
ivan = Employee("Ivan", 19, "School", 2, 0)  # object - ivan
petr = Employee("Petr", 30, "National Kyiv University", 8, 1)  # object - petr

# print objects:
print("Employee:")
tamara.print_employee_info()
petr.print_employee_info()
ivan.print_employee_info()
john.print_employee_info()

# output of a data array of employees for whom a decision was made to transfer - date "a=15.01.2023"
print("Submit to the manager for decision-making on applicants:")
print(Employee.get_date())
lst = [["John", 10]]
Employee.convert_list_to_dict(lst)
print(result)
print(john.get_name(), "-", john.get_age(john), "-", john.get_education(john))
print()
# output of a data array of employees for whom a decision was made to transfer - date "19.01.2023"
a = "19.01.2023"
print(Employee.get_date())
lst = [["Petr", 8]]
Employee.convert_list_to_dict(lst)
print(result)
print(john.get_name(), "-", john.get_age(john), "-", john.get_education(john))
print(petr.get_name(), "-", petr.get_age(petr), "-", petr.get_education(petr))
print()

# output of an array of data of employees who are transferred to the main office
a = "20.01.2023"
john_de = Employee.office_country("John", 45, "National Dnipro University", 10, 1, "Hannover,Germany")
petr_de = Employee.office_country("Petr", 30, "National Kyiv University", 8, 1, "Berlin,Germany")
print(Employee.get_date())
print("employees:", john.get_name(), ",", petr.get_name())
print("transferred to the office of the company:")
print(john_de.get_name(), "-", john_de.office)
print(petr_de.get_name(), "-", petr_de.office)

print("_____________________________________________________________")
# ___________________________________________________________________________________________________________________#
# information about open offices:                                                                                    #
# date of information update (b), office number - code, city in which the office is located (town),                  #
# number of employees (number_employees), indicator of the quality of work according to a 100 point rating system    #                                                       #
# (performance_appraisal),                                                                                           #
# ___________________________________________________________________________________________________________________#
b = "15.01.2023"  # date of information update
data_company = []  # office data


class Company:  # class creation - Company
    def __init__(self, number_office, town, number_employees, performance_appraisal):  # object class constructor
        self.number_office = number_office
        self.town = town
        self.number_employees = number_employees
        self.performance_appraisal = performance_appraisal

    def get_number_office(self):  # method of object
        return self.number_office

    def get_town(self):  # method of object
        return self.town

    def get_performance_appraisal(self, number_office):  # method of object
        return self.performance_appraisal

    def print_company_info(self):  # method of object
        print(f"""
        number of office: {self.number_office}
        town: {self.town}
        number of employees: {self.number_employees}
        performance appraisal:{self.performance_appraisal}
        """)

    @staticmethod  # date of information update (b)
    def get_date():
        return b

    # classmethod:     input of a new field - country, connection with the object
    @classmethod
    def new_office_country(cls, number_office, town, number_employees, performance_appraisal, country):
        instance = cls(number_office, town, number_employees, performance_appraisal)
        instance.counry = country
        return instance

    # method of processing and processing information about the activities of the office - office code, indicator
    @staticmethod
    def convert_list_to_dict(office_list):
        mapping = {"number of ofice": 0,
                   "perfomance appraisal": 1}
        for office in office_list:
            office_as_dict = dict()
            office_as_dict["number of ofice"] = office[mapping["number of ofice"]]
            office_as_dict["perfomance appraisal"] = office[mapping["perfomance appraisal"]]
            data_company.append(office_as_dict)
        return data_company

    # recording information about the activities of offices in a file "data.txt"
    @staticmethod
    def write_info(info):
        with open("data.txt", "w") as file:
            file.write(info)


# information about the work of offices by dates(b):
print("____________________________________________________________________________")
b = "01.01.2021"
print(Company.get_date())
sv_dnipro = Company(1, "Dnipro", 10, 76)
sv_kyiv = Company(2, "Kyiv", 25, 95)
sv_lviv = Company(3, "Lviv", 7, 68)
print("Office of Company:")
sv_dnipro.print_company_info()
sv_kyiv.print_company_info()
sv_lviv.print_company_info()
print("____________________________________________________________________________")
b = "17.01.2022"
print(Company.get_date())
sv_dnipro = Company(1, "Dnipro", 12, 85)
sv_kyiv = Company(2, "Kyiv", 27, 93)
sv_lviv = Company(3, "Lviv", 15, 91)
print("Office of Company:")
sv_dnipro.print_company_info()
sv_kyiv.print_company_info()
sv_lviv.print_company_info()
print("____________________________________________________________________________")
b = "17.05.2022"
sv_hannover_de = Company.new_office_country(4, "Hannover", 5, 10, "Germany")
sv_berlin_de = Company.new_office_country(5, "Berlin", 7, 6, "Germany")
print(Company.get_date())
print("New office:", sv_hannover_de.get_town(), "№", sv_hannover_de.get_number_office(), ",", sv_berlin_de.get_town(),
      "№", sv_berlin_de.get_number_office())
print("____________________________________________________________________________")
# opening new offices and adding them to the database:
b = "19.01.2023"
print(Company.get_date())
sv_dnipro = Company(1, "Dnipro", 5, 36)  # object
sv_kyiv = Company(2, "Kyiv", 15, 45)
sv_lviv = Company(3, "Lviv", 26, 87)
sv_hannover_de = Company.new_office_country(4, "Hannover", 5, 10, "Germany")
sv_berlin_de = Company.new_office_country(5, "Berlin", 7, 6, "Germany")
print("Office of Company:")
sv_dnipro.print_company_info()
sv_kyiv.print_company_info()
sv_lviv.print_company_info()
sv_hannover_de.print_company_info()
sv_berlin_de.print_company_info()
print("____________________________________________________________________________")
# preparation of information for writing to a file data.txt
print("preparation of information for writing to a file:")
print(Company.get_date())
lst = [(1, 36), (2, 45), (3, 87), (4, 10), (5, 6)]
print(Company.convert_list_to_dict(lst))
info = str(data_company)
Company.write_info(info)
# reading information from a file data.txt
b = "20.01.2023"
print("reading information from a file:")
print(Company.get_date())
with open(r"data.txt", "r") as file:
    for line in file:
        print(line)
