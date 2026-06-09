from tkinter import *


class CourseView:
    def __init__(self, root):
        self.root = root

        self.root.title("System zarządzania kursami online")
        self.root.geometry("800x600")

        Label(
            root,
            text="SYSTEM ZARZĄDZANIA KURSAMI ONLINE",
            font=("Arial", 16, "bold")
        ).pack(pady=10)

        self.frame_courses = Frame(root)
        self.frame_courses.pack(side=LEFT, padx=20)

        Label(
            self.frame_courses,
            text="KURSY"
        ).pack()

        self.listbox_courses = Listbox(
            self.frame_courses,
            width=30,
            height=15
        )
        self.listbox_courses.pack()

        self.frame_participants = Frame(root)
        self.frame_participants.pack(side=LEFT, padx=20)

        Label(
            self.frame_participants,
            text="UCZESTNICY"
        ).pack()

        self.listbox_participants = Listbox(
            self.frame_participants,
            width=30,
            height=15
        )
        self.listbox_participants.pack()

        self.frame_enrollments = Frame(root)
        self.frame_enrollments.pack(side=LEFT, padx=20)

        Label(
            self.frame_enrollments,
            text="ZAPISY"
        ).pack()

        self.listbox_enrollments = Listbox(
            self.frame_enrollments,
            width=30,
            height=15
        )
        self.listbox_enrollments.pack()