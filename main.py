from controller import *
from view import * 
from model import *
from termcolor import colored

def main():
    while True:
        print()
        print(colored("----- CHOOSE OPERATION -----", "blue"))
        print("1: Show all departments")
        print("2: Show department")
        print("3: Add department")
        print()
        print("4: Show all students")
        print("5: Show student")
        print("6: Add student")
        print()
        print("7: Show all instructors")
        print("8: Show instructor")
        print("9: Add instructor")
        print("10: Add subject to the student")
        print("11: Put grade to the student")
        print("12: Change student's grade")


        print("0: Exit")
        choise = input(colored("Your choise: ", "green"))
        d_controller = DepartmentController(DepartmentView, CollegeDepartment)
        s_controller = StudentController(StudentView, CollegeStudent)
        i_controller = InstructorController(InstructorView, CollegeInstructor)
        if choise == "0":
            break

        elif choise == "1":
            d_controller.show_all_department()

        elif choise == "2":
            name = input("Enter department's name: ")
            d_controller.show_department(name)

        elif choise == "3":
            name = input("Enter department's name: ")
            d_controller.add_department(name)

        elif choise == "4":
            s_controller.show_all_students()

        elif choise == "5":
            name = input("Enter student's name: ")
            surname = input("Enter student's surname: ")
            s_controller.show_student(name, surname)

        elif choise == "6":
            name = input("Enter student's name: ")
            surname = input("Enter student's surname: ")
            student_id = input("Enter student's id: ")
            department = input("Enter department's name: ")
            s_controller.add_student(name, surname, student_id, department)
        
        elif choise == "7":
            i_controller.show_all_instructors()

        elif choise == "8":
            name = input("Enter instructor's name: ")
            surname = input("Enter instructor's surname: ")
            i_controller.show_instructor(name, surname)
        
        elif choise == "9":
            id = input("Enter instructor's id: ")
            name = input("Enter instructor's name: ")
            surname = input("Enter instructor's surname: ")
            lesson = input("Enter leson's name: ")
            i_controller.add_instructor(name, surname, id, lesson)

        elif choise == "10":
            st_name = input("Enter student's name: ")
            st_surname = input("Enter student's surname: ")
            subject_name = input("Enter subjetc's name: ")
            i_controller.add_subject_to_student(st_name, st_surname, subject_name)

        elif choise == "11":
            st_name = input("Enter student's name: ")
            st_surname = input("Enter student's surname: ")
            subject_name = input("Enter subjetc's name: ")
            mark = int(input("Enter mark: "))
            i_controller.put_grades(st_name, st_surname, subject_name, mark)

        elif choise == "12":
            st_name = input("Enter student's name: ")
            st_surname = input("Enter student's surname: ")
            subject_name = input("Enter subjetc's name: ")
            mark = int(input("Enter mark: "))
            i_controller.change_grade(st_name, st_surname, subject_name, mark)

        else:
            print("Please choose a valid choise!!!!")

if __name__ == "__main__":
    main()
