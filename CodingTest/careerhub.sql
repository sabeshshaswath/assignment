--1. Provide a SQL script that initializes the database for the Job Board scenario “CareerHub”.

create database CareerHub;

use CareerHub;

--2. Create tables for Companies, Jobs, Applicants and Applications.

--3. Define appropriate primary keys, foreign keys, and constraints

--4. Ensure the script handles potential errors, such as if the database or tables already exist.

Create table Compaines(CompanyID int primary key,CompanyName varchar(255),Location varchar(255))

Create table Jobs(JobID int primary key ,CompanyID int foreign key references compaines(CompanyID
),JobTitle varchar(255),JobDescription varchar(255),JobLocation varchar(255),Salary decimal,
JobType varchar(255),PostedDate datetime)

create table Applicants(ApplicantID int primary key,FirstName varchar(255),LastName varchar(255)
,Email varchar(255),Phone varchar(255),Resume text,city varchar(255),state varchar(255))


create table Applications(ApplicationID int primary key,JobID int foreign key references Jobs(JobID),
ApplicantID int foreign key references Applicants(ApplicantID),ApplicationDate datetime,
CoverLetter text)

INSERT INTO Compaines (CompanyID,CompanyName, Location) VALUES
(1,'Tech Innovations', 'San Francisco'),
(2,'Data Driven Inc', 'New York'),
(3,'GreenTech Solutions', 'Austin'),
(4,'CodeCrafters', 'Boston'),
(5,'HexaWare Technologies', 'Chennai');



INSERT INTO Jobs (JobID,CompanyID, JobTitle, JobDescription, JobLocation, Salary, JobType, PostedDate) VALUES
(1,1, 'Frontend Developer', 'Develop user-facing features', 'San Francisco', 75000, 'Full-time', '2023-01-10'),
(2,2, 'Data Analyst', 'Interpret data models', 'New York', 68000, 'Full-time', '2023-02-20'),
(3,3, 'Environmental Engineer', 'Develop environmental solutions', 'Austin', 85000, 'Full-time', '2023-03-15'),
(4,1, 'Backend Developer', 'Handle server-side logic', 'Remote', 77000, 'Full-time', '2023-04-05'),
(5,4, 'Software Engineer', 'Develop and test software systems', 'Boston', 90000, 'Full-time', '2023-01-18'),
(6,5, 'HR Coordinator', 'Manage hiring processes', 'Chennai', 45000, 'Contract', '2023-04-25'),
(7,2, 'Senior Data Analyst', 'Lead data strategies', 'New York', 95000, 'Full-time', '2023-01-22');


INSERT INTO Applicants (ApplicantID,FirstName, LastName, Email, Phone, Resume) VALUES
(1,'John', 'Doe', 'john.doe@example.com', '123-456-7890', 'Experienced web developer with 5 years of experience.'),
(2,'Jane', 'Smith', 'jane.smith@example.com', '234-567-8901', 'Data enthusiast with 3 years of experience in data analysis.'),
(3,'Alice', 'Johnson', 'alice.johnson@example.com', '345-678-9012', 'Environmental engineer with 4 years of field experience.'),
(4,'Bob', 'Brown', 'bob.brown@example.com', '456-789-0123', 'Seasoned software engineer with 8 years of experience.');
INSERT INTO Applicants (ApplicantID, FirstName, LastName, Email, Phone, Resume) VALUES
(5, 'Sarah', 'Johnson', 'sarah.johnson@example.com', '678-901-2345', 'Experienced project manager with a proven track record in leading successful teams.');


INSERT INTO Applications (ApplicationID,JobID, ApplicantID, ApplicationDate, CoverLetter) VALUES
(1,1, 1, '2023-04-01', 'I am excited to apply for the Frontend Developer position.'),
(2,2, 2, '2023-04-02', 'I am interested in the Data Analyst position.'),
(3,3, 3, '2023-04-03', 'I am eager to bring my expertise to your team as an Environmental Engineer.'),
(4,4, 4, '2023-04-04', 'I am applying for the Backend Developer role to leverage my skills.'),
(5,5, 1, '2023-04-05', 'I am also interested in the Software Engineer position at CodeCrafters.');

--5. Write an SQL query to count the number of applications received for each job listing in the 
--"Jobs" table. Display the job title and the corresponding application count. Ensure that it lists all 
--jobs, even if they have no applications.


select j.Jobtitle,count(ApplicationID) as applications from jobs j left join Applications a 
on a.JobID=j.JobID
group by j.JobTitle,j.JobID 

--6. Develop an SQL query that retrieves job listings from the "Jobs" table within a specified salary 
--range. Allow parameters for the minimum and maximum salary values. Display the job title, 
--company name, location, and salary for each matching job.

select CompanyName,Location,j.salary from Compaines c inner join jobs j 
on j.CompanyID=c.CompanyID
where Salary between 60000 and 80000

--7 Write an SQL query that retrieves the job application history for a specific applicant. Allow a 
--parameter for the ApplicantID, and return a result set with the job titles, company names, and 
--application dates for all the jobs the applicant has applied to

select ApplicantID,a.JobID,ApplicationDate,JobTitle,c.CompanyName from Applications a inner join
Jobs j on a.JobID=j.JobID inner join Compaines c on j.CompanyID=c.CompanyID where ApplicantID=1;


--8 Create an SQL query that calculates and displays the average salary offered by all companies for 
--job listings in the "Jobs" table. Ensure that the query filters out jobs with a salary of zero.

select companyName,avg(Salary) avg_salary from Jobs j inner join 
Compaines c on j.CompanyID=c.CompanyID
group by CompanyName,j.CompanyID

--9. Write an SQL query to identify the company that has posted the most job listings. Display the 
--company name along with the count of job listings they have posted. Handle ties if multiple 
--companies have the same maximum count.

select * from Jobs

select CompanyName,c.CompanyID,COUNT(JobID) from Compaines c inner join Jobs j on c.CompanyID=j.CompanyID
group by c.CompanyID,CompanyName having COUNT(JobID)=(select max(tcount) from(
select CompanyName,c.CompanyID,COUNT(JobID) tcount from Compaines c inner join Jobs j on c.CompanyID=j.CompanyID
group by c.CompanyID,CompanyName) a)

--10. Find the applicants who have applied for positions in companies located in 'CityX' and have at 
--least 3 years of experience.
SELECT 
    c.CompanyName,
    CONCAT(a.firstName, a.lastName) AS ApplicantName
FROM 
    Compaines c
JOIN
	jobs j ON j.CompanyID=c.CompanyID
JOIN 
    Applications app ON j.JobID= app.JobID
JOIN 
    Applicants a ON app.ApplicantID = a.ApplicantID
WHERE 
    c.Location = 'New York'
    AND a.resume Like '%[3-9] years%'

--11. Retrieve a list of distinct job titles with salaries between $60,000 and $80,000.

select distinct JobTitle from jobs where salary between 60000 and 80000;

--12. Find the jobs that have not received any applications.
select * from jobs where JobID not in (select distinct JobID from Applications)

--13.  Retrieve a list of job applicants along with the companies they have applied to and the positions 
---they have applied for.

select FirstName,LastName,CompanyName from Applicants a inner join  Applications ap on a.ApplicantID=ap.ApplicantID
inner join jobs j on j.JobID=ap.JobID inner join Compaines c on j.CompanyID=c.CompanyID group by 
FirstName,LastName,a.ApplicantID,ap.JobID,j.CompanyID,CompanyName

--14. Retrieve a list of companies along with the count of jobs they have posted, even if they have not 
--received any applications

select CompanyName,COUNT(JobID) Count from Compaines c left join Jobs j on c.CompanyID=j.CompanyID
group by c.CompanyID,CompanyName

--15. List all applicants along with the companies and positions they have applied for, including those 
--who have not applied.

select FirstName,LastName,companyName,jobtitle from Applicants a left join Applications ap on
ap.ApplicantID=a.ApplicantID left join jobs j on j.JobID=ap.JobID left join Compaines c on c.CompanyID
=j.CompanyID group by FirstName,LastName,a.ApplicantID,CompanyName,JobTitle


--16. Find companies that have posted jobs with a salary higher than the average salary of all jobs.
select companyname from Compaines c inner join jobs j on 
c.CompanyID=j.CompanyID where salary>(select avg(salary) avg from Jobs)

--17. Display a list of applicants with their names and a concatenated string of their city and state
select CONCAT(firstName,lastName) as Name ,CONCAT(city,state) from  applicants;

-- 18 Retrieve a list of jobs with titles containing either 'Developer' or 'Engineer'.
select * from jobs where JobTitle Like '%Developer%' or jobtitle Like '%Engineer%';

--19. Retrieve a list of applicants and the jobs they have applied for, including those who have not 
--applied and jobs without applicants

select firstname,lastname,jobtitle from Applicants a left join Applications ap on ap.ApplicantID=a.ApplicantID
full join Jobs j on j.JobID=ap.JobID;

--20. List all combinations of applicants and companies where the company is in a specific city and the 
--applicant has more than 2 years of experience. For example: city=Chennai


SELECT 
    c.CompanyName,
    CONCAT(a.firstName, a.lastName) AS ApplicantName
FROM 
    Compaines c
JOIN
	jobs j ON j.CompanyID=c.CompanyID
JOIN 
    Applications app ON j.JobID= app.JobID
JOIN 
    Applicants a ON app.ApplicantID = a.ApplicantID
WHERE 
    c.Location = 'austin'
    AND a.resume Like '%[2-9] years%'
