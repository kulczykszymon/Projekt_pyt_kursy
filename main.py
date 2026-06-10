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
    edit_employee
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
root.mainloop()