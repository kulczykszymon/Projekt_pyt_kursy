from tkinter import Tk

from view import CourseView
from controller import add_course, delete_course


root = Tk()

view = CourseView(root)

view.button_add_course.config(
    command=lambda: add_course(view)
)

view.button_delete_course.config(
    command=lambda: delete_course(view)
)

root.mainloop()