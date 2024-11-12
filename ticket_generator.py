from fakermodule import fake_question
from ticket import Ticket

class TicketGenerator:
    def __init__(self, teacher, subject, student_group):
        self.teacher = teacher
        self.subject = subject
        self.student_group = student_group

    def get_ticket(self, n):
        try:
            real_count_students = len(self.student_group.students)
            if real_count_students > n:
                raise ValueError(f"Количество билетов меньше чем количество студентов в группе {self.student_group.group_name}")
            for ticket in range(n):
                yield Ticket(fake_question(), self.subject, ticket)
        except ValueError as err:
            if f"Количество билетов меньше чем количество студентов в группе {self.student_group.group_name}" == str(err):
                raise err