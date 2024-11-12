
from fakermodule import fake_subject, fake_name, fake_age_teacher, fake_age_student, fake_number_group, fake_date_exam
from student import Student
from student_group import StudentGroup
from subject import Subject
from teacher import Teacher
from ticket_generator import TicketGenerator
from exam import Exam


teacher1 = Teacher(fake_name(), fake_age_teacher(), "Male")
teacher2 = Teacher(fake_name(), fake_age_teacher(), "Male")
#Создаем учителей

student1 = Student(fake_name(), fake_age_student(), "Male")
student2 = Student(fake_name(), fake_age_student(), "Female")

teacher1.teaches_subject(fake_subject())
teacher2.teaches_subject(fake_subject())

student1.get_grade(fake_subject(), 5)
student1.get_grade(fake_subject(), 5)
student2.get_grade(fake_subject(), 4)

teacher1.teaching_student(student1, fake_subject())
teacher2.teaching_student(student2, fake_subject())

student1.show_marks()
student2.show_marks()

student1.enrollment(fake_name())

students_first = [Student(fake_name(), fake_age_student(), "Male") for _ in range(10)]
students_second = [Student(fake_name(), fake_age_student(), "Male") for _ in range(15)]

sg1 = StudentGroup(fake_number_group(),students=students_first)
sg2 = StudentGroup(fake_number_group(),students=students_second)

#Студента1 Зачислили в Группу1
sg1.add_student(student1)

for student in sg1:
    print(student)

for student in sg2:
    print(student)

#Создаем экзамены для двух разных групп
exam1 = Exam(fake_subject(), sg1, fake_date_exam(), fake_date_exam())
exam2 = Exam(fake_subject(), sg2, fake_date_exam(), fake_date_exam())

#Учителя проводят экзамен
teacher1.conduct_exam(exam1)
teacher2.conduct_exam(exam2)

#Студента отчислили из Группы1
student1.kick(sg1)

#Первой группе начислили стипендию
sg1.pay_all()

#Уведомление о начале экзамена во второй группе
sg2.notify()

#Генерируем билеты
tg = TicketGenerator(teacher1, exam1.subject, sg1)
obj1 = tg.get_ticket(len(sg1.students))
for o in obj1:
    print(o)

#Сравниваем группы
print(sg1 == sg2)

#Генерируем билетов меньше чем количество учеников в группе
tg = TicketGenerator(teacher2, exam1.subject, sg2)
obj2 = tg.get_ticket(14)
for o in obj2:
    print(o)

print(sg1 == sg2)
# len(sg.students)