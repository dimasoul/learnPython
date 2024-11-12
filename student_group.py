class StudentGroup:
    def __init__(self, group_name, students: list):
        self.group_name = group_name
        self.students = students
        self.index = 0

    def __str__(self):
        return self.group_name

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.students):
            student = self.students[self.index]
            self.index += 1
            return student
        else:
            raise StopIteration

    def __len__(self):
        return len(self.students)

    def __contains__(self, item):
        return item in self.students

    def __eq__(self, other):
        return self.group_name == other.group_name and self.students == other.students

    def add_student(self, student):
        if student not in self.students:
            self.students.append(student)
            print(f"{student.name} зачислен в группу {self.group_name}")

    def remove_student(self, student):
        self.students.remove(student)
        print(f"{student.name} отчислен из группы {self.group_name}.")

# отчисление всех
    def kick_all(self):
        for student in self.students:
            student.kick()
            print(f" Все студенты отчислены из группы {self.group_name}.")

# начисление стипендии всем
    def pay_all(self):
        for student in self.students:
            print(f"Студенту {student} из группы {self.group_name}. начислена стипендия")

# уведомление группы
    def notify(self):
        print(f" Уведомление о начале экзамена для группы {self.group_name}.")
