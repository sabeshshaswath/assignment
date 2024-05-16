from .util import Db_prop,DBConnutil
from .Exception import EnrollmentNotFoundException,CourseNotFoundException,PaymentNotFoundException,StudentNotFoundException,TeacherNotFoundException,PaymentValidationException
from tabulate import tabulate

class StudentManagement:
    def __init__(self) -> None:
        self.connection=DBConnutil.get_connectionOBJ(Db_prop.getconstring())
        self.cursor=self.connection.cursor()
    def getStudentbyID(self, stu_id):
        try:
            self.cursor.execute("SELECT * FROM Students WHERE student_id = ?", (stu_id,))
            print(self.cursor.fetchone())
        except Exception as e:
            self.connection.rollback()
        raise StudentNotFoundException(f"Student with ID {stu_id} not found.")
    def add_student(self,student):
        try:
            self.cursor.execute("INSERT INTO Students (student_id, first_name, last_name, date_of_birth, email, phone_number) VALUES (?, ?, ?, ?, ?, ?)"
                                , (student.student_id,student.first_name,student.last_name,student.date_of_birth,student.email,student.phone_number,))
            self.connection.commit()
        except Exception as e:
            self.connection.rollback()
        raise e(f"Error")
    def update_student(self,student):
        try:
            self.cursor.execute("UPDATE Students SET first_name = ?, last_name = ?, date_of_birth = ?, email = ?, phone_number = ? WHERE student_id = ?"
                                , (student.first_name,student.last_name,student.date_of_birth,student.email,student.phone_number,student.student_id))
            self.connection.commit()
        except Exception as e:
            self.connection.rollback()
        raise StudentNotFoundException(f"Error")
    def EnrollCourse(self,student_id,course_id):
        try:
            self.cursor.execute("select enrollment_id from enrollments order by enrollment_id desc offset 0 rows fetch next 1 rows only")
            currentEnrollId=self.cursor.fetchone()
            self.cursor.execute("INSERT INTO Enrollments VALUES (?, ?, ?, GETDATE())", (currentEnrollId[0] + 1, student_id, course_id))
            self.connection.commit()
        except Exception as e:
            self.connection.rollback()
            raise StudentNotFoundException(" Error: {}".format(str(e)))
    def makepayment(self,student_id,amount):
        try:
            self.cursor.execute("select payment_id from payments order by payment_id desc offset 0 rows fetch next 1 rows only")
            payment_id=self.cursor.fetchone()
            self.cursor.execute("INSERT INTO payments VALUES (?, ?, ?, GETDATE())", (payment_id[0] + 1, student_id, amount))
            self.connection.commit()
        except Exception as e:
            self.connection.rollback()
            raise StudentNotFoundException("Error: {}".format(str(e)))
    def DisplayStudentInfo(self,Student_id):
        try:
            self.cursor.execute("Select * from students where student_id=?", (Student_id))
            print(tabulate(self.cursor.fetchall()))
        except Exception as e:
            self.connection.rollback()
            raise StudentNotFoundException("Error: {}".format(str(e)))
    def GetEnrolledCourses(self,student_id):
        try:
            self.cursor.execute("select students.student_id,first_name,last_name,course_name from students inner join enrollments  on students.student_id=enrollments.student_id inner join courses on courses.course_id=enrollments.course_id where students.student_id=?"
                                , (student_id))
            print(tabulate(self.cursor.fetchall()))
        except Exception as e:
            self.connection.rollback()
            raise StudentNotFoundException("Error: {}".format(str(e)))
    def GetPaymentHistory(self,student_id):
        try:
            self.cursor.execute("Select * from payments where student_id=?"
                                , (student_id))
            print(tabulate(self.cursor.fetchall()))
        except Exception as e:
            self.connection.rollback()
            raise StudentNotFoundException("Error: {}".format(str(e)))
    def close(self):
        self.cursor.close()
        self.connection.close()

class EnrollmentManagement:
    def __init__(self) -> None:
        self.connection=DBConnutil.get_connectionOBJ(Db_prop.getconstring())
        self.cursor=self.connection.cursor()
    def GetStudent(self,EnrollementID):
        try:
            self.cursor.execute("select first_name,last_name,course_id from students inner join enrollments on students.student_id=enrollments.student_id where enrollment_id=?"
                                , (EnrollementID))
            print(tabulate(self.cursor.fetchall()))
        except Exception as e:
            self.connection.rollback()
            raise EnrollmentNotFoundException("Error: {}".format(str(e)))
    def GetCourse(self,EnrollementID):
        try:
            self.cursor.execute("select course_name,credits,teacher_id from courses inner join enrollments on courses.course_id=enrollments.course_id where enrollment_id=?"
                                , (EnrollementID))
            print(tabulate(self.cursor.fetchall()))
        except Exception as e:
            self.connection.rollback()
            raise EnrollmentNotFoundException("Error: {}".format(str(e)))
    def close(self):
        self.cursor.close()
        self.connection.close()
    
class CourseManagement():
    def __init__(self) -> None:
        self.connection=DBConnutil.get_connectionOBJ(Db_prop.getconstring())
        self.cursor=self.connection.cursor()
    def AssignTeacher(self,courseID,TeahcerId):
        try:
            self.cursor.execute("UPDATE Courses SET teacher_id=? WHERE course_id = ?"
                                , (TeahcerId,courseID))
            self.connection.commit()
        except Exception as e:
            self.connection.rollback()
        raise StudentNotFoundException(f"Error")
    def UpdateCourseInfo(self,Course):
        try:
            self.cursor.execute("UPDATE Courses SET course_name=?,credits?,teacher_id=? WHERE course_id = ?"
                                , (Course.course_name,Course.credits,Course.TeahcerId,Course.courseID))
            self.connection.commit()
        except Exception as e:
            self.connection.rollback()
            raise CourseNotFoundException("Error: {}".format(str(e)))          
    def DisplayCourseInfo(self,CourseID):
        try:
            self.cursor.execute("Select * from courses WHERE course_id = ?"
                                , (CourseID))
            print(tabulate(self.cursor.fetchall()))
        except Exception as e:
            self.connection.rollback()
            raise CourseNotFoundException("Error: {}".format(str(e)))        
    def GetEnrollments(self,CourseID):
        try:
            self.cursor.execute("select course_name,count(student_id) as Count from courses as c left join enrollments as e on c.course_id=e.course_id group by course_name,c.course_id having c.course_id=?"
                                , (CourseID))
            print(tabulate(self.cursor.fetchall()))
        except Exception as e:
            self.connection.rollback()
            raise CourseNotFoundException("Error: {}".format(str(e)))      
    def GetTeacher(self,CourseID):
        try:
            self.cursor.execute("select first_name,last_name,course_name from teacher inner join courses on courses.teacher_id=teacher.teacher_id where course_id=?"
                                , (CourseID))
            print(tabulate(self.cursor.fetchall()))
        except Exception as e:
            self.connection.rollback()
            raise CourseNotFoundException("Error: {}".format(str(e)))   
    def close(self):
        self.cursor.close()
        self.connection.close()
      
class TeacherManagement():
    def __init__(self) -> None:
        self.connection=DBConnutil.get_connectionOBJ(Db_prop.getconstring())
        self.cursor=self.connection.cursor()
    def DisplayTeacherInfo(self,teacher_id):
        try:
            self.cursor.execute("select * from teacher  where teacher_id=?"
                                , (teacher_id))
            print(tabulate(self.cursor.fetchall()))
        except Exception as e:
            self.connection.rollback()
            raise TeacherNotFoundException("Error: {}".format(str(e)))  
    def GetAssignedCourses(self,teacher_id):
        try:
            self.cursor.execute("select first_name,last_name,course_name from teacher inner join courses on courses.teacher_id=teacher.teacher_id where courses.teacher_id=?"
                                , (teacher_id))
            print(tabulate(self.cursor.fetchall()))
        except Exception as e:
            self.connection.rollback()
            raise TeacherNotFoundException("Error: {}".format(str(e))) 
    def UpdateTeacher(self,teacher):
        try:
            self.cursor.execute("Update table teacher set first_name=?,last_name=?,email=? where teacher_id=?",(teacher.first_name,teacher.last_name,teacher.email,teacher.teacher_id))
            print(tabulate(self.cursor.fetchall()))
        except Exception as e:
            self.connection.rollback()
            raise TeacherNotFoundException("Error: {}".format(str(e)))   
    def close(self):
        self.cursor.close()
        self.connection.close()
    
class PaymentManagement():
    def __init__(self) -> None:
        self.connection=DBConnutil.get_connectionOBJ(Db_prop.getconstring())
        self.cursor=self.connection.cursor()
    def GetPaymentAmount(self,student_id):
        try:
            self.cursor.execute("select amount from Payments  inner join students on Payments.student_id=students.student_id where students.student_id=?;"
                                , (student_id))
            print(tabulate(self.cursor.fetchall()))
        except Exception as e:
            self.connection.rollback()
            raise PaymentValidationException("Error: {}".format(str(e)))  
    def GetPaymentDate(self,payment_id):
        try:
            self.cursor.execute("select date from Payments where payment_id=?;"
                                , (payment_id))
            print(tabulate(self.cursor.fetchall()))
        except Exception as e:
            self.connection.rollback()
            raise PaymentValidationException("Error: {}".format(str(e)))      
    def GetStudent(self,payment_id):
        try:
            self.cursor.execute("select * from Payments p inner join students s on p.student_id=s.student_id where payment_id=?;"
                                , (payment_id))
            print(tabulate(self.cursor.fetchall()))
        except Exception as e:
            self.connection.rollback()
            raise PaymentValidationException("Error: {}".format(str(e)))
    def close(self):
        self.cursor.close()
        self.connection.close()
    
