from tkinter import Tk
from view import CourseView


if __name__ == "__main__":
    root = Tk()
    view = CourseView(root)
    root.mainloop()