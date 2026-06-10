from tkinter import Tk

from view import CourseView

from controller import (
    add_course,
    delete_course,
    edit_course,
    add_participant,
    delete_participant
)
root = Tk()

view = CourseView(root)

view.button_add_course.config(
    command=lambda: add_course(view)
)

view.button_delete_course.config(
    command=lambda: delete_course(view)
)

view.button_edit_course.config(
    command=lambda: edit_course(view)
)

view.button_add_participant.config(
    command=lambda: add_participant(view)
)

view.button_delete_participant.config(
    command=lambda: delete_participant(view)
)
root.mainloop()