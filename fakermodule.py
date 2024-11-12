from faker import Faker
faker = Faker('ru_RU')


def fake_subject():
    return faker.word(ext_word_list=["Геометрия", "Математика", "Английский", "Физика", "Робототехника", "Электроника"])

def fake_name():
    return faker.name()

def fake_age_student():
    return faker.random_int(min=18, max=25)

def fake_age_teacher():
    return faker.random_int(min=35, max=55)

def fake_number_group():
    return faker.bothify(letters='ABCDE')

def fake_date_exam():
    return faker.date()

def fake_question():
    return faker.sentence()