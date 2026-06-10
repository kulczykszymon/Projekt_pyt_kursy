class Company:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y


class Client:
    def __init__(self, name, company, x, y):
        self.name = name
        self.company = company
        self.x = x
        self.y = y


class Employee:
    def __init__(self, name, company, x, y):
        self.name = name
        self.company = company
        self.x = x
        self.y = y


companies = []
clients = []
employees = []