# Assignment 2

## task 1.Database Desing

1. Create the database named "SISDB

```sql
CREATE database SISDB
```

2. Define the schema for the Students, Courses, st item prEnrollments, Teacher, and Payments tables based 
on the provided schema. Write SQL scripts to create the mentioned tables with appropriate data 
types, constraints, and relationships. 
   - Students 
   - Courses
   - Enrollments 
   - Teacher 
   - Payments

```sql
Create table students(student_id INT Primary key,first_name varchar(255),last_name varchar(255),
date_of_birth varchar(255),email varchar(255),phone_number int)

alter table students drop column phone_number;
ALTER TABLE students
ADD phone_number varchar(255);
create table teacher(teacher_id int primary key,first_name varchar(255),last_name varchar(255),email varchar(255))

create table courses(course_id INT primary key,course_name varchar(255),credits INT,teacher_id int foreign key references teacher(teacher_id))

create table enrollments(enrollment_id int primary key,student_id int foreign key references students(student_id),course_id int foreign key 
references courses(course_id));
alter table enrollments add enrollment_date DATE;
CREATE TABLE Payments (
    payment_id INT PRIMARY KEY,
    student_id INT,
    amount DECIMAL(10, 2),
    payment_date DATE,
    FOREIGN KEY (student_id) REFERENCES Students(student_id)
);
```

1. Create an ERD (Entity Relationship Diagram) for the database.

![erd](image.png)



4. Create appropriate Primary Key and Foreign Key constraints for referential integrity.✔
5. Insert at least 10 sample records into each of the following tables.
   - Students
   - Courses
   - Enrollments
   - Teacher
   - Payments
```sql
INSERT INTO Students (student_id, first_name, last_name, date_of_birth, email, phone_number)
VALUES
(1, 'Suresh', 'Patel', '1998-05-20', 'suresh.patel@email.com', '9876543210'),
(2, 'Priya', 'Singh', '1997-08-12', 'priya.singh@email.com', '8765432109'),
(3, 'Manoj', 'Kumar', '1996-11-25', 'manoj.kumar@email.com', '7654321098'),
(4, 'Divya', 'Shah', '1999-03-15', 'divya.shah@email.com', '6543210987'),
(5, 'Ananya', 'Verma', '1995-09-08', 'ananya.verma@email.com', '5432109876'),
(6, 'Rajesh', 'Gupta', '1997-12-10', 'rajesh.gupta@email.com', '4321098765'),
(7, 'Asha', 'Malhotra', '1998-06-18', 'asha.malhotra@email.com', '3210987654'),
(8, 'Vishnu', 'Sharma', '1994-04-22', 'vishnu.sharma@email.com', '2109876543'),
(9, 'Meera', 'Joshi', '1993-07-30', 'meera.joshi@email.com', '1098765432'),
(10, 'Arjun', 'Goyal', '1996-02-14', 'arjun.goyal@email.com', '0987654321');

INSERT INTO Courses (course_id, course_name, credits, teacher_id)
VALUES
(1, 'Computer Science', 3, 101),
(2, 'Mathematics', 4, 102),
(3, 'Physics', 3, 103),
(4, 'Chemistry', 3, 104),
(5, 'Biology', 4, 105),
(6, 'History', 3, 106),
(7, 'Literature', 3, 107),
(8, 'Economics', 4, 108),
(9, 'Geography', 3, 109),
(10, 'Political Science', 4, 110);



INSERT INTO Enrollments (enrollment_id, student_id, course_id, enrollment_date)
VALUES
(1, 1, 1, '2024-04-01'),
(2, 2, 2, '2024-04-03'),
(3, 3, 3, '2024-04-05'),
(4, 4, 4, '2024-04-07'),
(5, 5, 5, '2024-04-09'),
(6, 6, 6, '2024-04-11'),
(7, 7, 7, '2024-04-13'),
(8, 8, 8, '2024-04-15'),
(9, 9, 9, '2024-04-17'),
(10, 10, 10, '2024-04-19');

INSERT INTO Teacher (teacher_id, first_name, last_name, email)
VALUES
(101, 'Karthik', 'Gupta', 'karthik.gupta@email.com'),
(102, 'Shalini', 'Verma', 'shalini.verma@email.com'),
(103, 'Manoj', 'Singh', 'manoj.singh@email.com'),
(104, 'Priya', 'Shah', 'priya.shah@email.com'),
(105, 'Suresh', 'Malhotra', 'suresh.malhotra@email.com'),
(106, 'Divya', 'Joshi', 'divya.joshi@email.com'),
(107, 'Rajesh', 'Sharma', 'rajesh.sharma@email.com'),
(108, 'Asha', 'Kumar', 'asha.kumar@email.com'),
(109, 'Vishnu', 'Patel', 'vishnu.patel@email.com'),
(110, 'Meera', 'Singh', 'meera.singh@email.com');

INSERT INTO Payments(payment_id, student_id, amount, payment_date)
VALUES
(1, 1, 500.00, '2024-04-02'),
(2, 2, 600.00, '2024-04-04'),
(3, 3, 700.00, '2024-04-06'),
(4, 4, 800.00, '2024-04-08'),
(5, 5, 900.00, '2024-04-10'),
(6, 6, 1000.00, '2024-04-12'),
(7, 7, 1100.00, '2024-04-14'),
(9, 9, 1300.00, '2024-04-18'),
(10, 10, 1400.00, '2024-04-20');
```



## Tasks 2: Select, Where, Between, AND, LIKE

1. Write an SQL query to insert a new student into the "Students" table with the following details:
    - First Name: John
    - Last Name: Doe
    - Date of Birth: 1995-08-15
    - Email: john.doe@example.com
    - Phone Number: 1234567890
```sql
insert into Students values(11,'John','Doe','1995-08-15','john.doe@example.com','1234567890')
```

1. Write an SQL query to enroll a student in a course. Choose an existing student and course and 
insert a record into the "Enrollments" table with the enrollment date
```sql
insert into Enrollments values(11,4,8,'2024-04-28');
```

1. update the email address of a specific teacher in the "Teacher" table. Choose any teacher and  modify their email address.
   ```sql
    update teacher set email='meera.guptah@email.com' where teacher_id=110;
   ```
2. Write an SQL query to delete a specific enrollment record from the "Enrollments" table. Select an enrollment record based on the student and course.
   ```sql
    delete from enrollments where student_id=4 AND course_id=4
   ```
3. Update the "Courses" table to assign a specific teacher to a course. Choose any course and teacher from the respective tables
   ```sql
    update courses set teacher_id=110 where course_id=1
   ```
4. --Delete a specific student from the "Students" table and remove all their enrollment records 
--from the "Enrollments" table. Be sure to maintain referential integrity

```sql
delete from enrollments where student_id=8
delete from Payments where student_id=8
delete from students where student_id=8
```

7. --Update the payment amount for a specific payment record in the "Payments" table. Choose any 
--payment record and modify the payment amount

```sql
update Payments set amount=1200.00 where student_id=4
```

8.
--Write an SQL query to calculate the total payments made by a specific student. You will need to 
--join the "Payments" table with the "Students" table based on the student's ID.

```sql
select SUM(amount) as total_amount from Payments  inner join students on Payments.student_id=students.student_id
where students.first_name='Divya';
```

## task 3. Aggregate functions, Having, Order By, GroupBy and Joins:

1. --Write an SQL query to retrieve a list of courses along with the count of students enrolled in each 
--course. Use a JOIN operation between the "Courses" table and the "Enrollments" table.
```sql
select course_name,count(student_id) from courses as c left join enrollments as e on 
c.course_id=e.course_id group by course_name;
```
2. --Write an SQL query to find the names of students who have not enrolled in any course. Use a 
--LEFT JOIN between the "Students" table and the "Enrollments" table to identify students 
--without enrollments

```sql
select first_name,last_name from students left join enrollments	
								on students.student_id=enrollments.student_id where enrollments.student_id is null;
```

3. -- Write an SQL query to retrieve the first name, last name of students, and the names of the 
--courses they are enrolled in. Use JOIN operations between the "Students" table and the 
--"Enrollments" and "Courses" tables.
```sql
select first_name,last_name,course_name from students inner join enrollments  on students.student_id=enrollments.student_id
inner join courses on courses.course_id=enrollments.course_id 
```
4. --Create a query to list the names of teachers and the courses they are assigned to. Join the 
--"Teacher" table with the "Courses" table.
```sql

select first_name,last_name,course_name from teacher inner join courses on courses.teacher_id=teacher.teacher_id
```
5. --Retrieve a list of students and their enrollment dates for a specific course. You'll need to join the 
--"Students" table with the "Enrollments" and "Courses" tables.

```sql
select first_name,last_name,course_name,enrollments.enrollment_date from students inner join enrollments  on students.student_id=enrollments.student_id
inner join courses on courses.course_id=enrollments.course_id
```

6. --Find the names of students who have not made any payments. Use a LEFT JOIN between the 
--"Students" table and the "Payments" table and filter for students with NULL payment records
```sql
select students.first_name,students.last_name from students left join Payments on Payments.student_id=students.student_id
where payments.student_id is null;
```
7. --Write a query to identify courses that have no enrollments. You'll need to use a LEFT JOIN 
--between the "Courses" table and the "Enrollments" table and filter for courses with NULL 
--enrollment records
```sql
select course_name from courses left join enrollments on courses.course_id=enrollments.course_id where enrollments.course_id is null;
```
8. --Identify students who are enrolled in more than one course. Use a self-join on the "Enrollments" 
--table to find students with multiple enrollment records.
```sql
SELECT one.student_id 
FROM enrollments AS one 
JOIN enrollments AS two ON one.student_id = two.enrollment_id 
GROUP BY  one.student_id 
HAVING COUNT(two.student_id) > 1;
```

9. -- Find teachers who are not assigned to any courses. Use a LEFT JOIN between the "Teacher" 
--table and the "Courses" table and filter for teachers with NULL course assignments.
```sql
select first_name,last_name from teacher left join courses on courses.teacher_id=teacher.teacher_id where
courses.teacher_id is null
```

## --Task 4. Subquery and its type:

1. -- Write an SQL query to calculate the average number of students enrolled in each course. Use 
-- aggregate functions and subqueries to achieve this
```sql
	SELECT course_name,total_enrollment
FROM (
    SELECT COUNT(enrollment_id) total_enrollment,course_id
    FROM Enrollments
    GROUP BY course_id
) AS enrollments inner join courses on enrollments.course_id=courses.course_id
```
2. --Identify the student(s) who made the highest payment. Use a subquery to find the maximum 
--payment amount and then retrieve the student(s) associated with that amount.
```sql
select first_name,last_name from students where student_id=(select student_id from Payments where amount=(select MAX(amount)
from Payments
))
```

3. --Retrieve a list of courses with the highest number of enrollments. Use subqueries to find the 
--course(s) with the maximum enrollment count
```sql
SELECT course_name 
FROM courses 
WHERE course_id IN (
    SELECT course_id 
    FROM enrollments 
    GROUP BY course_id 
    HAVING COUNT(course_id) = (
        SELECT MAX(enrollment_count) 
        FROM (
            SELECT COUNT(*) AS enrollment_count 
            FROM enrollments 
            GROUP BY course_id
        ) AS max_enrollments
    )
);
```
> select * from courses;
> select * from teacher; 
> select * from payments;
> select * from enrollments;

5. -- Identify students who are enrolled in all available courses. Use subqueries to compare a 
--student's enrollments with the total number of courses.
```sql
select first_name,last_name from students where student_id in
(SELECT student_id
FROM enrollments
GROUP BY student_id
HAVING COUNT(DISTINCT course_id) = (
    SELECT COUNT(*) 
    FROM courses
));
```
6. --Retrieve the names of teachers who have not been assigned to any courses. Use subqueries to 
--find teachers with no course assignments.
```sql
select first_name,last_name from teacher where teacher_id not in
(select distinct teacher_id from courses)
```

7. -- Calculate the average age of all students. Use subqueries to calculate the age of each student 
--based on their date of birth.


```sql
select avg(age) as avg_age
from (SELECT CAST(DATEDIFF(YEAR, date_of_birth, GETDATE()) AS INT) AS age
FROM students) as student_ages
```

8. --identify courses with no enrollments. Use subqueries to find courses without enrollment 
--records.
```sql
Select course_name from courses where course_id in
	(select course_id from courses where course_id not in 	
		(select course_id from enrollments)) 
```

11. --Write an SQL query to calculate the total payments made by each student. Join the "Students" 
--table with the "Payments" table and use GROUP BY to calculate the sum of payments for each student.
```sql
SELECT student_id, SUM(amount) AS total_payment
FROM (
    SELECT e.student_id, e.course_id, p.amount
    FROM Enrollments e
    INNER JOIN Payments p ON e.student_id = p.student_id
) AS student_payments
GROUP BY student_id
```
12. -- Retrieve a list of course names along with the count of students enrolled in each course. Use 
-- JOIN operations between the "Courses" table and the "Enrollments" table and GROUP BY to 
-- count enrollments.
```sql
select course_name,COUNT(enrollment_id) as total_enrollments from enrollments e inner 
join courses c  on c.course_id=e.course_id group by course_name
```

13. -- Calculate the average payment amount made by students. Use JOIN operations between the 
-- "Students" table and the "Payments" table and GROUP BY to calculate the average

```sql
select first_name,last_name,sum(amount) total_sum from
(select s.first_name,s.last_name,amount from students s 
	inner join Payments p on s.student_id=p.student_id ) l
	group by first_name,last_name
```

10. -- Identify students who have made more than one payment. Use subqueries and aggregate 
-- functions to count payments per student and filter for those with counts greater than one
```sql
select first_name,last_name from students s inner join 	
	(select student_id from Payments group by student_id having COUNT(payment_id)>1) p
		on p.student_id=s.student_id
```

4. --. Calculate the total payments made to courses taught by each teacher. Use subqueries to sum payments for each teacher's courses

```sql
    select * from teacher t inner join(select c.course_id,c.teacher_id,sum(e.amount) 
as earnings_made from course c inner join
(select s.student_id,e.course_id,s.amount from enrollments e inner join 
(select s.student_id,p.amount from students s inner join payments p on s.student_id=p.student_id)s
 on e.student_id=s.student_id)e on c.course_id=e.course_id group by c.course_id,c.teacher_id)p 
 on t.teacher_id=p.teacher_id order by p.earnings_made desc offset 0 rows fetch next 1 rows only;
```

9. List all combinations of applicants and companies where the company is in a specific city and the applicant has more than 2 years of experience. For example: city=Chennai
```sql
select s.student_id, s.first_name, s.last_name, e.course_id, e.course_name, e.total_payment
from students s 
inner join (
    select c.course_id, c.course_name, e.student_id, e.total_payment
    from course c 
    inner join (
        select e.student_id, e.course_id, sum(p.amount) as total_payment
        from enrollments e 
        inner join payments p
        on e.student_id = p.student_id
        group by e.student_id, e.course_id
    ) e
    on c.course_id = e.course_id
) e
on e.student_id = s.student_id

```
