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