class Company:
    def __init__(self, name, city, address):
        self.name = name
        self.city = city
        self.address = address

        # współrzędne pobierane automatycznie
        self.latitude = None
        self.longitude = None

        self.courses = []


class Client:
    def __init__(self, name, company, city):
        self.name = name
        self.company = company
        self.city = city

        self.latitude = None
        self.longitude = None


class Employee:
    def __init__(self, name, company, city):
        self.name = name
        self.company = company
        self.city = city

        self.latitude = None
        self.longitude = None


companies = []
clients = []
employees = []