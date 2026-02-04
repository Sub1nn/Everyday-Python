----------------------------------------------------------------------------------
--- student table
----------------------------------------------------------------------------------
CREATE TABLE student (
	id integer PRIMARY KEY AUTOINCREMENT,
	first_name varchar(255) NOT NULL,
	last_name varchar(255),
	age int,
	address varchar,
	grade varchar,
	gender varchar(1) not null
);

insert into
student ('first_name', 'last_name', 'age', 'address', 'grade', 'gender')
values
('Ramesh','Pradhan', 95, 'Lalitpur', 'Bachelor', 'M'),
('Hari', 'Bahadur', 45, 'Kathmandu', 'Master', 'M'),
('Madan', 'Bahadur', 36, 'Kathmandu', 'Doctorate', 'M'),
('Sita', 'Devi', 36, "Kathmanud", 'SLC', 'F'),
('Gita', 'Maya', 32, "Kathmanud", '+2', 'F'),
('Maya', 'Devi', 31, 'Lalitpur', 'Master', 'M');

SELECT * FROM student;

select * from student where age > 35;

update student set address = 'Kathamandu' where address ='Kathmanud' ;

update student set age = 40 where first_name ='Madan' ;

update student set gender = 'F' where first_name ='Maya' and last_name ='Devi' ;

----------------------------------------------------------------------------------
--- college table
----------------------------------------------------------------------------------
CREATE TABLE college (
	id integer PRIMARY KEY AUTOINCREMENT,
	name varchar(255) NOT NULL,
	location varchar(255)
);

insert into
college ('name', 'location')
values
('St. Xavier', 'Kathmandu'),
('Pulchowk Campus', 'Lalitpur'),
('Amrit Science Campus', 'Kathmandu');

----------------------------------------------------------------------------------
--- Add college_id as nullable foreign key to student table
----------------------------------------------------------------------------------
ALTER TABLE student
ADD COLUMN college_id INTEGER REFERENCES college(id) NULL;

-- Update student records with college_id
UPDATE student SET college_id = (SELECT id FROM college WHERE name = 'St. Xavier') WHERE first_name IN ('Sita', 'Gita');
UPDATE student SET college_id = (SELECT id FROM college WHERE name = 'Pulchowk Campus') WHERE first_name IN ('Hari', 'Madan');
UPDATE student SET college_id = (SELECT id FROM college WHERE name = 'Amrit Science Campus') WHERE first_name = 'Ramesh';

-- aggregation query

SELECT AVG(age) from student s ;

SELECT MAX(age) from student s ;

SELECT MIN(age) from student s ;

SELECT SUM(age) from student s ;

SELECT COUNT(id) from student s ;

select * from student s  where first_name LIKE 'r%';

select * from student s  where first_name LIKE '_i%' and last_name = 'Maya';

select * from student s  where (first_name LIKE '_i%' and last_name = 'Maya') or age > 25;

select count(*) from student s  where (first_name LIKE '_i%' and last_name = 'Maya') or age > 25;

select * from student where age between 20 and 40 ORDER by first_name asc;

select * from student where age between 20 and 40 ORDER by first_name desc;

select * from student where age between 20 and 40 ORDER by first_name asc, last_name desc, age asc;

select first_name, last_name, age
from student where age between 20 and 40
ORDER by first_name asc, last_name desc, age asc;


select DISTINCT last_name
from student where age between 20 and 40
ORDER by first_name asc, last_name desc, age asc;
----------------------------------------------------------------------------------