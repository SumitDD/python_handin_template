import random
import string
import names
import csv
import matplotlib.pyplot as plt


class Student():

    def __init__(self, name, gender, data_sheet, image_url):
        self.name = name
        self.gender = gender
        self.data_sheet = data_sheet
        self.image_url = image_url

    def get_avg_grade(self):
        sum_grades = 0
        for grade in self.data_sheet.grades_as_list():
            sum_grades += int(grade)
        avg_grade = sum_grades / len(self.data_sheet.grades_as_list())
        return avg_grade

    def progression_ETCS(self):
        total_ETCS = 0
        for course in self.data_sheet.courses:
            total_ETCS += int(course.ETCS)

        progression = total_ETCS/150
        return progression


class DataSheet():

    def __init__(self, courses=[]):
        self.courses = courses

    def grades_as_list(self):
        grades = []
        for course in self.courses:
            grades.append(course.grade)
        return grades


class Course():

    def __init__(self, name, classroom, teacher, ETCS, grade):
        self.name = name
        self.classroom = classroom
        self.teacher = teacher
        self.ETCS = ETCS
        self.grade = grade


def generate_students(number):
    course_names = ['Python', 'Typescript', 'Security']
    genders = ['male', 'female']
    grades = ['-3', '00', '02', '4', '7', '10', '12']

    for x in range(0, number):
        with open('./week3.csv', 'a') as file:
            course = Course(random.choice(course_names),
                            'D klassen', 'Thomas', '20', random.choice(grades))
            data_sheet = DataSheet([course])
            name = names.get_full_name()
            image_url = ''.join(random.choice(string.ascii_lowercase)
                                for i in range(15))
            student = Student(name, random.choice(
                genders), data_sheet, image_url)

            text_to_file = "Student name: {name}, courses: {course_name}, gender: {gender}, teacher: {teacher}, ETCS: {ETCS}, classroom: {classroom}, grade: {grade}, image_url: {image_url}".format(
                name=student.name, course_name=course.name, gender=student.gender, teacher=course.teacher, ETCS=course.ETCS, classroom=course.classroom, grade=course.grade, image_url=student.image_url)

            file.write(text_to_file + "\n")


def read_student_data():
    student_list = []
    with open('./week3.csv', 'r') as file:
        lines = file.readlines()
        for line in lines:
            name = line.split("Student name: ")[1].split(', courses')[0]
            gender = line.split("gender: ")[1].split(', teacher:')[0]
            course_name = line.split("courses: ")[1].split(', teacher')[0]
            teacher = line.split("teacher: ")[1].split(', ETCS:')[0]
            ETCS = line.split("ETCS: ")[1].split(', classroom')[0]
            classroom = line.split("classroom:")[1].split(', grade:')[0]
            grade = line.split("grade:")[1].split(',')[0]
            image_url = line.split("image_url:")[1]

            course = Course(course_name, classroom, teacher, ETCS, grade)
            data_sheet = DataSheet([course])
            student = Student(name, gender, data_sheet, image_url)
            student_list.append(student)

    return student_list


def print_students():
    student_list = read_student_data()
    for student in student_list:
        print("Name: " + student.name, "image_url: " +
              student.image_url, "grade: " + str(student.get_avg_grade()))


print_students()


def sort_avg_grade():
    student_list = read_student_data()
    student_list.sort(key=lambda x: x.get_avg_grade(), reverse=True)
    for student in student_list:
        print(student.get_avg_grade())


def create_bar_chart():
    student_list = read_student_data()
    for student in student_list:
        plt.bar([student.name], [student.get_avg_grade()],
                width=0.5, align='center')


plt.xticks(rotation=45, horizontalalignment='right', fontweight='light')


def create_barchat_study_progression():

    student_list = read_student_data()
    progression_secruity = 0
    students_secruity = 0
    progression_typescript = 0
    students_typescript = 0
    progression_kotlin = 0
    students_kotlin = 0

    for student in student_list:
        for course in student.data_sheet.courses:
            if course.name == "Security":
                progression_secruity += student.progression_ETCS()
                students_secruity += 1
            if course.name == "Typescript":
                progression_typescript += student.progression_ETCS()
                students_typescript += 1
            if course.name == "Python":
                progression_kotlin += student.progression_ETCS()
                students_kotlin += 1

    plt.bar([progression_secruity], [students_secruity],
            width=0.5, align='center')
    plt.bar([progression_typescript], [
            students_typescript], width=0.5, align='center')
    plt.bar([progression_kotlin], [students_kotlin], width=0.5, align='center')
    plt.xticks(rotation=45, horizontalalignment='right', fontweight='light')
