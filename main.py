from tkinter import Tk

from view import CourseView

from controller import (
    add_company,
    delete_company,
    edit_company,
    add_client,
    delete_client,
    edit_client,
    add_employee,
    delete_employee,
    edit_employee,
    show_company_clients,
    show_all_clients,
    show_company_employees,
    show_all_employees,
    filter_companies,
    filter_clients,
    filter_employees,
    show_company_courses,
    add_course,
    show_company_courses,
)

root = Tk()

view = CourseView(root)

view.button_add_company.config(
    command=lambda: add_company(view)
)

view.button_delete_company.config(
    command=lambda: delete_company(view)
)

view.button_edit_company.config(
    command=lambda: edit_company(view)
)

view.button_add_client.config(
    command=lambda: add_client(view)
)

view.button_delete_client.config(
    command=lambda: delete_client(view)
)

view.button_edit_client.config(
    command=lambda: edit_client(view)
)

view.button_add_employee.config(
    command=lambda: add_employee(view)
)

view.button_delete_employee.config(
    command=lambda: delete_employee(view)
)

view.button_edit_employee.config(
    command=lambda: edit_employee(view)
)

view.button_show_company_clients.config(
    command=lambda: show_company_clients(view)
)

view.button_show_all_clients.config(
    command=lambda: show_all_clients(view)
)
view.button_show_company_employees.config(
    command=lambda: show_company_employees(view)
)

view.button_show_all_employees.config(
    command=lambda: show_all_employees(view)
)

view.button_filter_company.config(
    command=lambda: filter_companies(view)
)

view.button_filter_client.config(
    command=lambda: filter_clients(view)
)

view.button_filter_employee.config(
    command=lambda: filter_employees(view)
)

view.button_show_courses.config(
    command=lambda: show_company_courses(view)
)

view.button_add_course.config(
    command=lambda: add_course(view)
)

view.button_show_courses.config(
    command=lambda: show_company_courses(view)
)
root.mainloop()