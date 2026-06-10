from tkinter import Tk

from view import CourseView

from controller import (
    add_company,
    delete_company,
    edit_company
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

root.mainloop()