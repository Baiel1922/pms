from abc import ABC, abstractmethod
from exc import ObjectNotFoundException

class StudentAbstract(ABC):
    @abstractmethod
    def get_info(self):
        pass


class CollegeStudent(StudentAbstract):
    def __init__(self, id: str, name: str, surname: str):
        self.id = id
        self.name = name
        self.surname = surname
        self.lessons = {}

    def get_info(self):
        return f"{self.surname} {self.name} id: {self.id}"

    def get_marks(self):
        for lesson, mark in self.lessons.items():
            yield f"{lesson.lesson}: {mark}"


class InstructorAbstract(ABC):
    @abstractmethod
    def get_info(self):
        pass

    @abstractmethod
    def add_student(self):
        pass
    
    @abstractmethod
    def put_grade(self):
        pass

class Instructor:
    def __init__(self, id: int, name: str, surname: str, lesson: str):
        self.id = id
        self.name = name
        self.surname = surname
        self.lesson = lesson
        self.students_list = []
        self.students_grades = {}

    def __repr__(self):
        return f"{self.lesson}" 
    
    def get_info(self):
        return f"{self.surname} {self.name} lesson: {self.lesson}"
    


class CollegeInstructor(Instructor, InstructorAbstract):
    def __init__(self, id: int, name: str, surname: str, lesson: str):
        super().__init__(id, name, surname, lesson)
        self.id = id
        self.name = name
        self.surname = surname
        self.lesson = lesson
        self.students_list = []
        self.students_grades = {}

    def __repr__(self):
        return f"{self.lesson}" 
    
    def get_info(self):
        return f"{self.surname} {self.name} lesson: {self.lesson}"

    """
    when we add student to instructor's list,
    we also add lesson to the student's lessons
    """
    def add_student(self, student: object):
        self.students_list.append(student)
        self.students_grades[student] = "-"
    
    """
    firstly we check whether we added student to the list or not,
    if not we raise an error, if student exists in the list,
    then we put or change grade in the students grade and also
    in the students lessons
    """
    def put_grade(self, student: object, mark: int):
        if student in self.students_list:
            self.students_grades[student] = mark
            student.lessons[self] = mark
        
        else:
            raise ObjectNotFoundException

class Department(ABC):

    @abstractmethod
    def add_student():
        pass



class CollegeDepartment(Department):
    def __init__(self, name: str):
        self.name = name
        self.students = []

    def add_student(self, student: object):
        self.students.append(student)
    

class Students:
    students_list = []

    @classmethod
    def add_student(cls, student: object):
        cls.students_list.append(student)

    @classmethod
    def get_students(cls):
        return cls.students_list


class Departments:
    departments_list = []

    @classmethod
    def add_department(cls, department: object):
        cls.departments_list.append(department)

    @classmethod
    def get_departments(cls):
        return cls.departments_list


class Instructors:
    instructors_list = []

    @classmethod
    def add_instructor(cls, instructor: object):
        cls.instructors_list.append(instructor)

    @classmethod
    def get_instructors(cls):
        return cls.instructors_list


# st1 = CollegeStudent("208715002", "Baiel", "Abdyllaev")
# st2 = CollegeStudent("208715003", "Bekbol", "Askerov")
# st3 = CollegeStudent("208715004", "Daniel", "Nazirov")

# sca = Department("SCA-20A")
# sca.add_student(st1)
# sca.add_student(st2)
# sca.add_student(st3)

# instructor1 = CollegeInstructor("20871532002", "Toylu", "Toylu", "MATH")
# Instructors.add_instructor(instructor1)
# instructor1.add_student(st1)
# instructor1.add_student(st2)
# instructor1.add_student(st3)
# instructor1.put_grade(st1, 5)
# instructor1.put_grade(st2, 4)
# instructor1.put_grade(st3, 3)

# instructor1 = CollegeInstructor("2087153200223", "Irshad", "Gulbarga", "ECG")
# Instructors.add_instructor(instructor1)
# instructor1.add_student(st1)
# instructor1.add_student(st2)
# instructor1.add_student(st3)
# instructor1.put_grade(st1, 5)
# instructor1.put_grade(st2, 4)
# instructor1.put_grade(st3, 4)

# Departments.add_department(sca)

# for instructor in Instructors.instructors_list:
#     print(f"{instructor.lesson}: {instructor.name} {instructor.surname}\n")
#     for student, mark in instructor.students_grades.items():
#         print(f"{student.name} {student.surname}: {mark}")
#         print(student.lessons)
#     print("\n")

