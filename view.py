from tkinter import *

class CourseView:
    def __init__(self, root):
        self.root = root


        self.root.title("System zarządzania kursami online")
        self.root.geometry("900x600")

        Label(
            root,
            text="SYSTEM ZARZĄDZANIA KURSAMI ONLINE",
            font=("Arial", 16, "bold")
        ).grid(row=0, column=0, columnspan=3, pady=10)

        # ===== KURSY =====

        self.frame_courses = Frame(root)
        self.frame_courses.grid(row=1, column=0, padx=20, pady=20)

        Label(
            self.frame_courses,
            text="KURSY"
        ).grid(row=0, column=0, sticky=W)

        self.listbox_courses = Listbox(
            self.frame_courses,
            width=30,
            height=15
        )
        self.listbox_courses.grid(row=1, column=0, rowspan=7)

        Label(
            self.frame_courses,
            text="Formularz kursu"
        ).grid(row=1, column=1, columnspan=2)

        Label(
            self.frame_courses,
            text="Nazwa:"
        ).grid(row=2, column=1, sticky=W)

        self.entry_course_title = Entry(self.frame_courses)
        self.entry_course_title.grid(row=2, column=2)

        Label(
            self.frame_courses,
            text="Kategoria:"
        ).grid(row=3, column=1, sticky=W)

        self.entry_course_category = Entry(self.frame_courses)
        self.entry_course_category.grid(row=3, column=2)

        Label(
            self.frame_courses,
            text="Prowadzący:"
        ).grid(row=4, column=1, sticky=W)

        self.entry_course_instructor = Entry(self.frame_courses)
        self.entry_course_instructor.grid(row=4, column=2)

        self.button_add_course = Button(
            self.frame_courses,
            text="Dodaj kurs"
        )
        self.button_add_course.grid(
            row=5,
            column=1,
            columnspan=2
        )

        self.button_delete_course = Button(
            self.frame_courses,
            text="Usuń kurs"
        )
        self.button_delete_course.grid(
            row=6,
            column=1,
            columnspan=2
        )

        self.button_edit_course = Button(
            self.frame_courses,
            text="Edytuj kurs"
        )
        self.button_edit_course.grid(
            row=7,
            column=1,
            columnspan=2
        )

        # ===== UCZESTNICY =====

        self.frame_participants = Frame(root)
        self.frame_participants.grid(row=1, column=1, padx=20)

        Label(
            self.frame_participants,
            text="UCZESTNICY"
        ).grid(row=0, column=0, sticky=W)

        self.listbox_participants = Listbox(
            self.frame_participants,
            width=30,
            height=15
        )
        self.listbox_participants.grid(row=1, column=0, rowspan=7)

        Label(
            self.frame_participants,
            text="Formularz uczestnika"
        ).grid(row=1, column=1, columnspan=2)

        Label(
            self.frame_participants,
            text="Imię:"
        ).grid(row=2, column=1, sticky=W)

        self.entry_participant_name = Entry(
            self.frame_participants
        )
        self.entry_participant_name.grid(row=2, column=2)

        Label(
            self.frame_participants,
            text="Email:"
        ).grid(row=3, column=1, sticky=W)

        self.entry_participant_email = Entry(
            self.frame_participants
        )
        self.entry_participant_email.grid(row=3, column=2)

        self.button_add_participant = Button(
            self.frame_participants,
            text="Dodaj uczestnika"
        )
        self.button_add_participant.grid(
            row=4,
            column=1,
            columnspan=2
        )

        self.button_delete_participant = Button(
            self.frame_participants,
            text="Usuń uczestnika"
        )
        self.button_delete_participant.grid(
            row=5,
            column=1,
            columnspan=2
        )

        self.button_edit_participant = Button(
            self.frame_participants,
            text="Edytuj uczestnika"
        )
        self.button_edit_participant.grid(
            row=6,
            column=1,
            columnspan=2
        )

        # ===== ZAPISY =====

        self.frame_enrollments = Frame(root)
        self.frame_enrollments.grid(row=1, column=2, padx=20)

        Label(
            self.frame_enrollments,
            text="ZAPISY"
        ).grid(row=0, column=0, sticky=W)

        self.listbox_enrollments = Listbox(
            self.frame_enrollments,
            width=30,
            height=15
        )
        self.listbox_enrollments.grid(row=1, column=0, rowspan=6)

        Label(
            self.frame_enrollments,
            text="Formularz zapisu"
        ).grid(row=1, column=1, columnspan=2)

        Label(
            self.frame_enrollments,
            text="Kurs:"
        ).grid(row=2, column=1, sticky=W)

        self.entry_enrollment_course = Entry(
            self.frame_enrollments
        )
        self.entry_enrollment_course.grid(row=2, column=2)

        Label(
            self.frame_enrollments,
            text="Uczestnik:"
        ).grid(row=3, column=1, sticky=W)

        self.entry_enrollment_participant = Entry(
            self.frame_enrollments
        )
        self.entry_enrollment_participant.grid(row=3, column=2)

        self.button_add_enrollment = Button(
            self.frame_enrollments,
            text="Dodaj zapis"
        )
        self.button_add_enrollment.grid(
            row=4,
            column=1,
            columnspan=2
        )

        self.button_delete_enrollment = Button(
            self.frame_enrollments,
            text="Usuń zapis"
        )
        self.button_delete_enrollment.grid(
            row=5,
            column=1,
            columnspan=2
        )
