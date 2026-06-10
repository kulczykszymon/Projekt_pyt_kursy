from model import Course, Participant, courses, participants


def add_course(view):
    title = view.entry_course_title.get()
    category = view.entry_course_category.get()
    instructor = view.entry_course_instructor.get()

    if title == "" or category == "" or instructor == "":
        return

    course = Course(title, category, instructor)
    courses.append(course)

    view.listbox_courses.insert(
        "end",
        f"{title} | {category} | {instructor}"
    )

    view.entry_course_title.delete(0, "end")
    view.entry_course_category.delete(0, "end")
    view.entry_course_instructor.delete(0, "end")


def delete_course(view):
    selected = view.listbox_courses.curselection()

    if not selected:
        return

    index = selected[0]

    view.listbox_courses.delete(index)
    courses.pop(index)


def edit_course(view):
    selected = view.listbox_courses.curselection()

    if not selected:
        return

    index = selected[0]

    course = courses[index]

    view.entry_course_title.delete(0, "end")
    view.entry_course_category.delete(0, "end")
    view.entry_course_instructor.delete(0, "end")

    view.entry_course_title.insert(0, course.title)
    view.entry_course_category.insert(0, course.category)
    view.entry_course_instructor.insert(0, course.instructor)

    view.button_add_course.config(
        text="Zapisz zmiany",
        command=lambda: update_course(view, index)
    )


def update_course(view, index):
    course = courses[index]

    course.title = view.entry_course_title.get()
    course.category = view.entry_course_category.get()
    course.instructor = view.entry_course_instructor.get()

    view.listbox_courses.delete(index)

    view.listbox_courses.insert(
        index,
        f"{course.title} | {course.category} | {course.instructor}"
    )

    view.entry_course_title.delete(0, "end")
    view.entry_course_category.delete(0, "end")
    view.entry_course_instructor.delete(0, "end")

    view.button_add_course.config(
        text="Dodaj kurs",
        command=lambda: add_course(view)
    )
def add_participant(view):
    name = view.entry_participant_name.get()
    email = view.entry_participant_email.get()

    if name == "" or email == "":
        return

    participant = Participant(name, email)
    participants.append(participant)

    view.listbox_participants.insert(
        "end",
        f"{name} | {email}"
    )

    view.entry_participant_name.delete(0, "end")
    view.entry_participant_email.delete(0, "end")

def delete_participant(view):
    selected = view.listbox_participants.curselection()

    if not selected:
        return

    index = selected[0]

    view.listbox_participants.delete(index)
    participants.pop(index)