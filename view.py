from termcolor import colored
from model import *

class DepartmentView:

    def show_all_departments(self, departments: list):
        print(colored("----- DEPARTMENT LIST -----", "blue"))
        for department in departments:
            print(colored(f"* {department.name}", "green"))

    def show_department(self, department: object):
        number_of_students = len(department.students)
        print(colored("-"*100, "green"))
        print(department.name)
        print(colored(f"In this department has {number_of_students} students:", "blue"))
        for student in department.students:
            print(colored(f"* {student.surname} {student.name}", "green"))

        print(colored("-"*100, "green"))

    def show_department_error(self, department_name: str):
        print(colored("*"*100, "red"))
        print(f"{department_name} department does not exist :(")
        print(colored("*"*100, "red"))

    def show_added_department(self, name: str):
        print(colored("+"*100, "green"))
        print(f"{name} department was successfully added!!")
        print(colored("+"*100, "green"))

    def show_added_department_error(self, name: str):
        print(colored("*"*100, "red"))
        print(f"{name} department already exists :(")
        print(colored("*"*100, "red"))


class StudentView:

    def show_all_students(self, students: list):
        print(colored("----- STUDENT LIST -----", "blue"))
        for student in students:
            print(colored(f"* {student.get_info()}", "green"))

    def show_student(self, student: object):
        print(colored("-"*100, "green"))
        print(f"{student.get_info()}")
        print(colored("Courses:", "blue"))
        for course, mark in student.lessons.items():
            print(f"* {course.lesson}: {mark}")

        print(colored("-"*100, "green"))

    def show_student_error(self, student_info: str):
        print(colored("*"*100, "red"))
        print(f"{student_info} does not exist :(")

        print(colored("*"*100, "red"))

    def show_added_student(self, name: str, surname: str):
        print(colored("+"*100, "green"))
        print(f"{name} {surname} student was successfully added!!")
        print(colored("+"*100, "green"))
    
    def show_added_student_error(self, name: str, surname: str):
        print(colored("*"*100, "red"))
        print(f"{name} {surname} student already exists :(")
        print(colored("*"*100, "red"))

    def show_added_student_dep_error(self, name: str):
        print(colored("*"*100, "red"))
        print(f"We could not add the student")
        print(f"{name} department does not exist :(")
        print(colored("*"*100, "red"))

class InstructorView:

    def show_all_instructors(self, instructors: list):
        print(colored("----- INSTRUCTOR LIST -----", "blue"))
        for instructor in instructors:
            print(f"* {instructor.get_info()}")

    def show_all_students(self, students: list, subject: str, lesson: object):
        print(colored(f"----- STUDENT LIST {subject.upper()} -----", "blue"))
        for student in students:
            print(colored(f"* {student.get_info()}: {student[lesson]}", "green"))


    def show_instructor(self, instructor: object):
        print(colored("-"*100, "green"))
        print(f"{instructor.name} {instructor.surname}")
        print(f"Subject: {instructor.lesson}")
        print("Students:")
        for student, mark in instructor.students_grades.items():
            print(f"* {student.surname} {student.name}: {mark}")

        print(colored("-"*100, "green"))

    def show_instructor_error(self, name: str, surname: str):
        print(colored("*"*100, "red"))
        print(f"{surname} {name} does not exist :(")
        print(colored("*"*100, "red"))

    def show_added_instructor(self, name, surname):
        print(colored("+"*100, "green"))
        print(f"{name} {surname} instructor was successfully added!!")
        print(colored("+"*100, "green"))

    def show_added_instructor_error(self, name: str, surname: str):
        print(colored("*"*100, "red"))
        print(f"{name} {surname} instructor already exists :(")
        print(colored("*"*100, "red"))

    def show_added_subject_to_student(self, name: str, surname: str, subject_name: str):
        print(colored("+"*100, "green"))
        print(f"{name} {surname} successfully added  {subject_name} subject!!")
        print(colored("+"*100, "green"))

    def show_added_subject_to_student_error1(self, name: str, surname: str, subject_name: str):
        print(colored("*"*100, "red"))
        print(f"{name} {surname}  does not exist :(")
        print(colored("*"*100, "red"))

    def show_added_subject_to_student_error2(self, name: str, surname: str, subject_name: str):
        print(colored("*"*100, "red"))
        print(f"{subject_name}  does not exist :(")
        print(colored("*"*100, "red"))

    def show_changed_grade(self, name: str, surname: str, subject_name: str, mark: int):
        print(colored("+"*100, "green"))
        print(f"{name} {surname}'s grade in {subject_name} successfully changed to {mark}!!")
        print(colored("+"*100, "green"))

    def show_putted_grade(self, name: str, surname: str, subject_name: str, mark: int):
        print(colored("+"*100, "green"))
        print(f"{name} {surname} got {mark} in {subject_name}!!")
        print(colored("+"*100, "green"))

    def show_chaged_putted_grade_error(self, name: str, surname: str, subject_name: str, mark: int):
        print(colored("*"*100, "red"))
        print(f"Something went wrong :(")
        print(colored("*"*100, "red"))