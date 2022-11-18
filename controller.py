from model import *
from view import *

class IsDepartmentExistsMixin:
    def is_dep_exist(self, name: str):
        new_name = name.lower()
        department = list(filter(lambda x: x.name.lower() == new_name, Departments.departments_list))
        return department

class IsStudentExistsMixin:
    def is_st_exist(self, name: str, surname: str):
        name_surname = f"{surname.lower()}{name.lower()}"
        student = list(filter(lambda x: f"{x.surname.lower()}{x.name.lower()}" == name_surname, Students.students_list))
        return student

class IsInstructorExistsMixin:
    def is_instr_exist(self, name: str, surname: str):
        name_surname = f"{surname.lower()}{name.lower()}"
        instructor = list(filter(lambda x: f"{x.surname.lower()}{x.name.lower()}" == name_surname, Instructors.instructors_list))
        return instructor

class IsSubjectExistsMixin:
    def is_subject_exist(self, name: str):
        subject_name = f"{name.lower()}"
        instructor = list(filter(lambda x: f"{x.lesson.lower()}" == subject_name, Instructors.instructors_list))
        return instructor

class DepartmentController(IsDepartmentExistsMixin):
    def __init__(self, view, model):
        self.view = view()
        self.departments = Departments
        self.model = model

    def show_all_department(self):
        departments_list = self.departments.get_departments()
        self.view.show_all_departments(departments_list)

    def show_department(self, name: str):
        department = self.is_dep_exist(name)
        if department:
            self.view.show_department(department[0])

        else:
            self.view.show_department_error(name)

    def add_department(self, name: str):
        department = self.is_dep_exist(name)
        if department:
            self.view.show_added_department_error(name)

        else:
            new_department = self.model(name.upper())
            self.departments.add_department(new_department)
            self.view.show_added_department(name)


class StudentController(IsDepartmentExistsMixin, IsStudentExistsMixin):
    def __init__(self, view, model):
        self.view = view()
        self.model = model
        self.students = Students

    def show_all_students(self):
        students_list = self.students.students_list
        self.view.show_all_students(students_list)

    def show_student(self, name: str, surname: str):
        student = self.is_st_exist(name, surname)
        if student:
            self.view.show_student(student[0])
        
        else:
            self.view.show_student_error(f"{surname} {name}")

    
    def add_student(self, name: str, surname: str, id: str, department_name: str):
        new_name = name.title()
        new_surname = surname.title()
        student = self.is_st_exist(name, surname)
        if student:
            self.view.show_added_student_error(name, surname)

        else:
            department = self.is_dep_exist(department_name)
            if department:
                new_student = self.model(id, new_name, new_surname)
                Students.add_student(new_student)
                department[0].add_student(new_student)
                self.view.show_added_student(name, surname)

            else:
                self.view.show_added_student_dep_error(department_name)


class InstructorController(IsInstructorExistsMixin, IsStudentExistsMixin, IsSubjectExistsMixin):
    def __init__(self, view, model):
        self.view = view()
        self.model = model
        self.instructors = Instructors

    def show_all_instructors(self):
        instructors_list = self.instructors.get_instructors()
        self.view.show_all_instructors(instructors_list)

    def show_instructor(self, name: str, surname: str):
        instructor = self.is_instr_exist(name, surname)
        if instructor:
            self.view.show_instructor(instructor[0])

        else:
            self.view.show_instructor_error(name, surname)

    def add_instructor(self, name: str, surname: str, id: str, lesson: str):
        new_name = name.title()
        new_surname = surname.title()
        instructor = self.is_instr_exist(name, surname)
        if instructor:
            self.view.show_added_instructor_error(name, surname)

        else:
            new_instructor = self.model(id, new_name, new_surname, lesson)
            Instructors.add_instructor(new_instructor)
            self.view.show_added_instructor(name, surname)

    def add_subject_to_student(self, name: str, surname: str, subject_name: str):
        student = self.is_st_exist(name, surname)
        subject = self.is_subject_exist(subject_name)
        if student and subject:
            subject[0].add_student(student[0])
            self.view.show_added_subject_to_student(name, surname, subject_name)
        
        elif student and not subject:
            self.view.show_added_subject_to_student_error2(name, surname, subject_name)

        else:
            self.view.show_added_subject_to_student_error1(name, surname, subject_name)

    def put_grades(self, name: str, surname: str, subject_name: str, mark: int):
        student = self.is_st_exist(name, surname)
        subject = self.is_subject_exist(subject_name)
        if student and subject:
            subject[0].put_grade(student[0], mark)
            self.view.show_putted_grade(name, surname, subject_name, mark)
        
        else:
            self.view.show_chaged_putted_grade_error(name, surname, subject_name, mark)

    def change_grade(self, name: str, surname: str, subject_name: str, mark: int):
        student = self.is_st_exist(name, surname)
        subject = self.is_subject_exist(subject_name)
        if student and subject:
            subject[0].put_grade(student[0], mark)
            self.view.show_changed_grade(name, surname, subject_name, mark)
        
        else:
            self.view.show_chaged_putted_grade_error(name, surname, subject_name, mark)


# same lessons might esist


    

     




        
