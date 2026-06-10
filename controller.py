from model import (
    Company,
    Client,
    Employee,
    companies,
    clients,
    employees
)


# ===== FIRMY =====

def add_company(view):
    name = view.entry_company_name.get()
    city = view.entry_company_city.get()
    address = view.entry_company_address.get()

    if name == "" or city == "" or address == "":
        return

    company = Company(
        name,
        city,
        address
    )

    companies.append(company)

    view.listbox_companies.insert(
        "end",
        f"{name} | {city}"
    )

    view.entry_company_name.delete(0, "end")
    view.entry_company_city.delete(0, "end")
    view.entry_company_address.delete(0, "end")


def delete_company(view):
    selected = view.listbox_companies.curselection()

    if not selected:
        return

    index = selected[0]

    view.listbox_companies.delete(index)
    companies.pop(index)


def edit_company(view):
    selected = view.listbox_companies.curselection()

    if not selected:
        return

    index = selected[0]

    company = companies[index]

    view.entry_company_name.delete(0, "end")
    view.entry_company_city.delete(0, "end")
    view.entry_company_address.delete(0, "end")

    view.entry_company_name.insert(
        0,
        company.name
    )

    view.entry_company_city.insert(
        0,
        company.city
    )

    view.entry_company_address.insert(
        0,
        company.address
    )

    view.button_add_company.config(
        text="Zapisz zmiany",
        command=lambda: update_company(view, index)
    )


def update_company(view, index):
    company = companies[index]

    company.name = view.entry_company_name.get()
    company.city = view.entry_company_city.get()
    company.address = view.entry_company_address.get()

    view.listbox_companies.delete(index)

    view.listbox_companies.insert(
        index,
        f"{company.name} | {company.city}"
    )

    view.entry_company_name.delete(0, "end")
    view.entry_company_city.delete(0, "end")
    view.entry_company_address.delete(0, "end")

    view.button_add_company.config(
        text="Dodaj firmę",
        command=lambda: add_company(view)
    )

# ===== KLIENCI =====

def add_client(view):
    name = view.entry_client_name.get()
    company = view.entry_client_company.get()
    city = view.entry_client_city.get()

    if name == "" or company == "" or city == "":
        return

    client = Client(
        name,
        company,
        city
    )

    clients.append(client)

    view.listbox_clients.insert(
        "end",
        f"{name} | {company}"
    )

    view.entry_client_name.delete(0, "end")
    view.entry_client_company.delete(0, "end")
    view.entry_client_city.delete(0, "end")


def delete_client(view):
    selected = view.listbox_clients.curselection()

    if not selected:
        return

    index = selected[0]

    view.listbox_clients.delete(index)
    clients.pop(index)


def edit_client(view):
    selected = view.listbox_clients.curselection()

    if not selected:
        return

    index = selected[0]

    client = clients[index]

    view.entry_client_name.delete(0, "end")
    view.entry_client_company.delete(0, "end")
    view.entry_client_city.delete(0, "end")

    view.entry_client_name.insert(0, client.name)
    view.entry_client_company.insert(0, client.company)
    view.entry_client_city.insert(0, client.city)

    view.button_add_client.config(
        text="Zapisz zmiany",
        command=lambda: update_client(view, index)
    )


def update_client(view, index):
    client = clients[index]

    client.name = view.entry_client_name.get()
    client.company = view.entry_client_company.get()
    client.city = view.entry_client_city.get()

    view.listbox_clients.delete(index)

    view.listbox_clients.insert(
        index,
        f"{client.name} | {client.company}"
    )

    view.entry_client_name.delete(0, "end")
    view.entry_client_company.delete(0, "end")
    view.entry_client_city.delete(0, "end")

    view.button_add_client.config(
        text="Dodaj klienta",
        command=lambda: add_client(view)
    )

# ===== PRACOWNICY =====

def add_employee(view):
    name = view.entry_employee_name.get()
    company = view.entry_employee_company.get()
    city = view.entry_employee_city.get()

    if name == "" or company == "" or city == "":
        return

    employee = Employee(
        name,
        company,
        city
    )

    employees.append(employee)

    view.listbox_employees.insert(
        "end",
        f"{name} | {company}"
    )

    view.entry_employee_name.delete(0, "end")
    view.entry_employee_company.delete(0, "end")
    view.entry_employee_city.delete(0, "end")


def delete_employee(view):
    selected = view.listbox_employees.curselection()

    if not selected:
        return

    index = selected[0]

    view.listbox_employees.delete(index)
    employees.pop(index)


def edit_employee(view):
    selected = view.listbox_employees.curselection()

    if not selected:
        return

    index = selected[0]

    employee = employees[index]

    view.entry_employee_name.delete(0, "end")
    view.entry_employee_company.delete(0, "end")
    view.entry_employee_city.delete(0, "end")

    view.entry_employee_name.insert(0, employee.name)
    view.entry_employee_company.insert(0, employee.company)
    view.entry_employee_city.insert(0, employee.city)

    view.button_add_employee.config(
        text="Zapisz zmiany",
        command=lambda: update_employee(view, index)
    )


def update_employee(view, index):
    employee = employees[index]

    employee.name = view.entry_employee_name.get()
    employee.company = view.entry_employee_company.get()
    employee.city = view.entry_employee_city.get()

    view.listbox_employees.delete(index)

    view.listbox_employees.insert(
        index,
        f"{employee.name} | {employee.company}"
    )

    view.entry_employee_name.delete(0, "end")
    view.entry_employee_company.delete(0, "end")
    view.entry_employee_city.delete(0, "end")

    view.button_add_employee.config(
        text="Dodaj pracownika",
        command=lambda: add_employee(view)
    )