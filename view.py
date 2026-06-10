from tkinter import *


class CourseView:
    def __init__(self, root):
        self.root = root

        self.root.title("System zarządzania kursami online")
        self.root.geometry("1200x700")

        Label(
            root,
            text="SYSTEM ZARZĄDZANIA KURSAMI ONLINE",
            font=("Arial", 16, "bold")
        ).grid(row=0, column=0, columnspan=3, pady=10)

        # ================= FIRMY =================

        self.frame_companies = Frame(root)
        self.frame_companies.grid(row=1, column=0, padx=20, pady=20)

        Label(
            self.frame_companies,
            text="FIRMY"
        ).grid(row=0, column=0, sticky=W)

        self.listbox_companies = Listbox(
            self.frame_companies,
            width=30,
            height=15
        )
        self.listbox_companies.grid(row=1, column=0, rowspan=8)

        Label(
            self.frame_companies,
            text="Formularz firmy"
        ).grid(row=1, column=1, columnspan=2)

        Label(
            self.frame_companies,
            text="Nazwa:"
        ).grid(row=2, column=1, sticky=W)

        self.entry_company_name = Entry(
            self.frame_companies
        )
        self.entry_company_name.grid(row=2, column=2)

        Label(
            self.frame_companies,
            text="Miasto:"
        ).grid(row=3, column=1, sticky=W)

        self.entry_company_city = Entry(
            self.frame_companies
        )
        self.entry_company_city.grid(row=3, column=2)

        Label(
            self.frame_companies,
            text="Adres:"
        ).grid(row=4, column=1, sticky=W)

        self.entry_company_address = Entry(
            self.frame_companies
        )
        self.entry_company_address.grid(row=4, column=2)

        self.button_add_company = Button(
            self.frame_companies,
            text="Dodaj firmę"
        )
        self.button_add_company.grid(
            row=5,
            column=1,
            columnspan=2
        )

        self.button_delete_company = Button(
            self.frame_companies,
            text="Usuń firmę"
        )
        self.button_delete_company.grid(
            row=6,
            column=1,
            columnspan=2
        )

        self.button_edit_company = Button(
            self.frame_companies,
            text="Edytuj firmę"
        )
        self.button_edit_company.grid(
            row=7,
            column=1,
            columnspan=2
        )

        # ================= KLIENCI =================

        self.frame_clients = Frame(root)
        self.frame_clients.grid(row=1, column=1, padx=20)

        Label(
            self.frame_clients,
            text="KLIENCI"
        ).grid(row=0, column=0, sticky=W)

        self.listbox_clients = Listbox(
            self.frame_clients,
            width=30,
            height=15
        )
        self.listbox_clients.grid(row=1, column=0, rowspan=8)

        Label(
            self.frame_clients,
            text="Formularz klienta"
        ).grid(row=1, column=1, columnspan=2)

        Label(
            self.frame_clients,
            text="Nazwa:"
        ).grid(row=2, column=1, sticky=W)

        self.entry_client_name = Entry(
            self.frame_clients
        )
        self.entry_client_name.grid(row=2, column=2)

        Label(
            self.frame_clients,
            text="Firma:"
        ).grid(row=3, column=1, sticky=W)

        self.entry_client_company = Entry(
            self.frame_clients
        )
        self.entry_client_company.grid(row=3, column=2)

        Label(
            self.frame_clients,
            text="Miasto:"
        ).grid(row=4, column=1, sticky=W)

        self.entry_client_city = Entry(
            self.frame_clients
        )
        self.entry_client_city.grid(row=4, column=2)

        self.button_add_client = Button(
            self.frame_clients,
            text="Dodaj klienta"
        )
        self.button_add_client.grid(
            row=5,
            column=1,
            columnspan=2
        )

        self.button_delete_client = Button(
            self.frame_clients,
            text="Usuń klienta"
        )
        self.button_delete_client.grid(
            row=6,
            column=1,
            columnspan=2
        )

        self.button_edit_client = Button(
            self.frame_clients,
            text="Edytuj klienta"
        )
        self.button_edit_client.grid(
            row=7,
            column=1,
            columnspan=2
        )

        # ================= PRACOWNICY =================

        self.frame_employees = Frame(root)
        self.frame_employees.grid(row=1, column=2, padx=20)

        Label(
            self.frame_employees,
            text="PRACOWNICY"
        ).grid(row=0, column=0, sticky=W)

        self.listbox_employees = Listbox(
            self.frame_employees,
            width=30,
            height=15
        )
        self.listbox_employees.grid(row=1, column=0, rowspan=8)

        Label(
            self.frame_employees,
            text="Formularz pracownika"
        ).grid(row=1, column=1, columnspan=2)

        Label(
            self.frame_employees,
            text="Imię:"
        ).grid(row=2, column=1, sticky=W)

        self.entry_employee_name = Entry(
            self.frame_employees
        )
        self.entry_employee_name.grid(row=2, column=2)

        Label(
            self.frame_employees,
            text="Firma:"
        ).grid(row=3, column=1, sticky=W)

        self.entry_employee_company = Entry(
            self.frame_employees
        )
        self.entry_employee_company.grid(row=3, column=2)

        Label(
            self.frame_employees,
            text="Miasto:"
        ).grid(row=4, column=1, sticky=W)

        self.entry_employee_city = Entry(
            self.frame_employees
        )
        self.entry_employee_city.grid(row=4, column=2)

        self.button_add_employee = Button(
            self.frame_employees,
            text="Dodaj pracownika"
        )
        self.button_add_employee.grid(
            row=5,
            column=1,
            columnspan=2
        )

        self.button_delete_employee = Button(
            self.frame_employees,
            text="Usuń pracownika"
        )
        self.button_delete_employee.grid(
            row=6,
            column=1,
            columnspan=2
        )

        self.button_edit_employee = Button(
            self.frame_employees,
            text="Edytuj pracownika"
        )
        self.button_edit_employee.grid(
            row=7,
            column=1,
            columnspan=2
        )