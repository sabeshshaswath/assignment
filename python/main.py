from dao.Entity import Student,Course,Payment,Enrollement,Teacher
from dao import StudentManagement,CourseManagement,PaymentManagement,EnrollmentManagement,TeacherManagement

def StudentMenu():
        print("===== Student Management Menu =====")
        print("1. Get Student by ID")
        print("2. Add Student")
        print("3. Update Student")
        print("4. Enroll Course")
        print("5. Make Payment")
        print("6. Display Student Info")
        print("7. Get Enrolled Courses")
        print("8. Get Payment History")
        print("9. Exit")
        print("===============================")

def enrollment_display_menu():
        print("===== Enrollment Management Menu =====")
        print("1. Get Student")
        print("2. Get Course")
        print("3. Close")
        print("======================================")

def course_display_menu():
        print("===== Course Management Menu =====")
        print("1. Assign Teacher")
        print("2. Update Course Info")
        print("3. Display Course Info")
        print("4. Get Enrollments")
        print("5. Get Teacher")
        print("6. Close")
        print("==================================")

def teacher_display_menu():
        print("===== Teacher Management Menu =====")
        print("1. Display Teacher Info")
        print("2. Get Assigned Courses")
        print("3. Update Teacher Info")
        print("4. Close")
        print("===================================")

def payment_display_menu():
        print("===== Payment Management Menu =====")
        print("1. Get Payment Amount")
        print("2. Get Payment Date")
        print("3. Get Student")
        print("4. Close")
        print("====================================")

def mainmenu():
        print("=====  Main Menu =====")
        print("1. Student Management")
        print("2. Course Management")
        print("3. Enrollement Management")
        print("4. Teacher Management")
        print("5. Payment Management")
        print("6. Close")
        print("====================================") 



def student_management(obj):
        while True:
            StudentMenu()
            choice = input("Enter your choice: ")
            if choice == "1":
                id=int(input("Enter the StudentID: "))
                obj.getStudentbyID(id)
            elif choice == "2":
                    student_id = input("Enter student ID: ")
                    first_name = input("Enter first name: ")
                    last_name = input("Enter last name: ")
                    date_of_birth = input("Enter date of birth (YYYY-MM-DD): ")
                    email = input("Enter email: ")
                    phone_number = input("Enter phone number: ")
                    newstudent=Student(student_id,first_name,last_name,date_of_birth,email,phone_number)
                    obj.add_student(newstudent)
            elif choice == "3":
                    student_id = input("Enter student ID: ")
                    first_name = input("Enter first name: ")
                    last_name = input("Enter last name: ")
                    date_of_birth = input("Enter date of birth (YYYY-MM-DD): ")
                    email = input("Enter email: ")
                    phone_number = input("Enter phone number: ")
                    newstudent=Student(student_id,first_name,last_name,date_of_birth,email,phone_number)
                    obj.update_student()
            elif choice == "4":
                    StudentID=int(input("Enter the StudentID: "))
                    CourseID=int(input("Enter the CourseID: "))
                    obj.EnrollCourse(StudentID,CourseID)
            elif choice == "5":
                StudentID=int(input("Enter the StudentID: "))
                amount=int(input("Enter the amount: "))
                obj.makepayment(StudentID,amount)
            elif choice == "6":
                StudentID=int(input("Enter the StudentID: "))
                obj.DisplayStudentInfo(StudentID)
            elif choice == "7":
                StudentID=int(input("Enter the StudentID: "))
                obj.GetEnrolledCourses(StudentID)
            elif choice == "8":
                StudentID=int(input("Enter the StudentID: "))
                obj.GetPaymentHistory(StudentID)
            elif choice == "9":
                obj.close()
                break
            else:
                print("Invalid choice. Please enter a number from 1 to 9.")


def enrollment_management(obj):
        while True:
            enrollment_display_menu()
            choice = input("Enter your choice: ")
            if choice == "1":
                EnrollementID=int(input("Enter the EnrollementID: "))
                obj.GetStudent(EnrollementID)
            elif choice == "2":
                EnrollementID=int(input("Enter the EnrollementID: "))
                obj.GetCourse(EnrollementID)
            elif choice == "3":
                obj.close()
                break
            else:
                print("Invalid choice. Please enter a number from 1 to 3.")

def course_management(obj):
        while True:
            course_display_menu()
            choice = input("Enter your choice: ")
            if choice == "1":
                course_id = input("Enter course ID: ")
                Teacher_id = input("Enter Teacher ID: ")
                obj.AssignTeacher(course_id,Teacher_id)
            elif choice == "2":
                course_id = input("Enter course ID: ")
                course_name = input("Enter course name: ")
                credits = input("Enter credits: ")
                teacher_id = input("Enter teacher ID: ")
                new_course=Course(course_id,course_name,credits,teacher_id)
                obj.UpdateCourseInfo(new_course)
            elif choice == "3":
                course_id = input("Enter course ID: ")
                obj.DisplayCourseInfo(course_id)
            elif choice == "4":
                course_id = input("Enter course ID: ")
                obj.GetEnrollments(course_id)
            elif choice == "5":
                course_id = input("Enter course ID: ")
                obj.GetTeacher(course_id)
            elif choice == "6":
                obj.close()
                break
            else:
                print("Invalid choice. Please enter a number from 1 to 6.")

def teacher_management(obj):
        while True:
            teacher_display_menu()
            choice = input("Enter your choice: ")
            if choice == "1":
                Teacher_id = input("Enter Teacher ID: ")
                obj.DisplayTeacherInfo(Teacher_id)
            elif choice == "2":
                Teacher_id = input("Enter Teacher ID: ")
                obj.GetAssignedCourses(Teacher_id)
            elif choice == "3":
                teacher_id = input("Enter teacher ID: ")
                first_name = input("Enter first name: ")
                last_name = input("Enter last name: ")
                email = input("Enter email: ")
                new_teacher=Teacher(teacher_id,first_name,last_name,email)
                obj.UpdateTeacher(new_teacher)
            elif choice == "4":
                obj.close()
                break
            else:
                print("Invalid choice. Please enter a number from 1 to 4.")
        
def payment_management(obj):
        while True:
            payment_display_menu()
            choice = input("Enter your choice: ")
            if choice == "1":
                StudentID=int(input("Enter the StudentID: "))
                obj.GetPaymentAmount(StudentID)
            elif choice == "2":
                PaymentID=int(input("Enter the PaymentID: "))
                obj.GetPaymentDate(PaymentID)
            elif choice == "3":
                PaymentID=int(input("Enter the PaymentID: "))
                obj.GetStudent(PaymentID)
            elif choice == "4":
                obj.close()
                break
            else:
                print("Invalid choice. Please enter a number from 1 to 4.")
while True:
     mainmenu()
     choice=int(input("Enter your choice: "))
     if choice==1:
          Stuobj=StudentManagement()
          student_management(Stuobj)
     elif choice==2:
          courseObj=CourseManagement()
          course_management(courseObj)
     elif choice==3:
          enrollementobj=EnrollmentManagement()
          enrollment_management(enrollementobj)
     elif choice==4:
          teacherobj=TeacherManagement()
          teacher_management(teacherobj)
     elif choice==5:
          paymentobj=PaymentManagement()
          payment_management(paymentobj)
     elif choice==6:
          break
     else:
          print("Please enter within range")
          







