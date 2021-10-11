class Client:
    def __init__(self, name):
        self.name = name

class Contractor:
    def __init__(self, full_name, name, inn, date_from, country):
        self.full_name = full_name
        self.name = name
        self.inn = inn
        self.date_from = date_from
        self.country = country

class Representer:
    def __init__(self, first_name, last_name, middle_name, ssn, country):
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.ssn = ssn
        self.country = country

class Contract:
    def __init__(self, number, name, sign_date, start_date, end_date):
        self.number = number
        self.name = name
        self.sign_date = sign_date
        self.start_date = start_date
        self.end_date = end_date
