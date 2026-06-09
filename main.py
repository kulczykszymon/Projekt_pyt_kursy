from tkinter import Tk

from view import CourseView
from controller import add_course


root = Tk()

view = CourseView(root)

view.button_add_course.config(
    command=lambda: add_course(view)
)

root.mainloop()