class Course:
    def __init__(self, title, category, instructor):
        self.title = title
        self.category = category
        self.instructor = instructor


class Participant:
    def __init__(self, name, email):
        self.name = name
        self.email = email


class Enrollment:
    def __init__(self, course_title, participant_name):
        self.course_title = course_title
        self.participant_name = participant_name


courses = []
participants = []
enrollments = []
