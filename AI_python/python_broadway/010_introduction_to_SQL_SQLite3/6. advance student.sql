CREATE TABLE student(
	id int primary key,
	name varchar not null,
	address varchar not null,
	age int not null,
	gender varchar(1) not null,
	faculty varchar not null
);

INSERT INTO student
('id', 'name', 'address', 'age', 'gender', 'faculty', 'college_id')
VALUES
(1, 'ram', 'kathmandu', 18, 'm', 'IT', 1), -- ncit
(2, 'shyam', 'lalitpur', 20, 'm', 'CSIT', 2), -- islington
(3, 'gita', 'pokhara', 21, 'f', 'SE', 1), -- ncit
(4, 'sita', 'kathmandu', 24, 'f','CE', 3); -- ioe pulchowk

-- * means get all columns FROM student table
SELECT * FROM student;

SELECT name, address FROM student;

UPDATE student set address = 'lalitpur' WHERE id = 3;

ALTER table student add university varchar default 'TU';


DELETE FROM student WHERE id = 3;

INSERT into student
('id', 'name', 'address', 'age', 'gender', 'faculty', 'college_id')
VALUES
(3, 'gita', 'pokhara', 21, 'f', 'SE', 1), -- ncit
(5, 'hari', 'kathmandu', 24, 'm','CIVIL', 3), -- ioe pulchowk
(6, 'madan', 'pokhara', 21, 'f', 'SE', 1), -- ncit
(7, 'maya', 'kathmandu', 24, 'f','BIT', 2); -- islington

UPDATE student set gender  = 'm' WHERE id=6;

SELECT * FROM student WHERE gender = 'f';

SELECT * FROM student WHERE age > 20;

SELECT * FROM student WHERE gender = 'm' and age > 20;

SELECT * FROM student WHERE age >= 20 and age <=25;

SELECT * FROM student WHERE age BETWEEN 20 and 25;

SELECT * FROM student WHERE age BETWEEN 20 and 25 order by age;

SELECT * FROM student WHERE age BETWEEN 20 and 25 order by age desc;

SELECT * FROM student WHERE age BETWEEN 20 and 25 order by age desc, gender asc;

SELECT * FROM student 
WHERE age BETWEEN 20 AND 25 
ORDER BY age DESC, 
    CASE 
        WHEN gender = 'F' THEN 1 
        WHEN gender = 'M' THEN 2 
        ELSE 3  -- For any other values, if applicable
    END;

SELECT * FROM student WHERE address ='kathmandu' and college = 'ioe pulchowk' and gender = 'm';

SELECT * FROM student WHERE 
(address = 'kathmandu' AND college = 'ncit') 
or (address='pokhara' and college='ncit');

-- same as above
SELECT * FROM student WHERE college = 'ncit' 
and (address='pokhara' or address='kathmandu');

-- same as above
SELECT * FROM student WHERE 
address in ('kathmandu', 'pokhara') and college = 'ncit';

SELECT * FROM student WHERE 
(address = 'kathmandu' AND college = 'ncit') 
or (address='pokhara' and college='ncit') and gender = 'm';

-- same as above
SELECT * FROM student WHERE 
(
	(address = 'kathmandu' AND college = 'ncit') 
	or (address='pokhara' and college='ncit')
) and (gender = 'm');

--- same as above
SELECT * FROM student WHERE 
(
	(address = 'kathmandu' AND college = 'ncit' and gender = 'm') 
	or (address='pokhara' and college='ncit' and gender = 'm')
);

-- same as above
SELECT * FROM student WHERE 
(address = 'Kathmandu' AND college = 'ncit') 
or (address='Pokhara' and college='ncit') and gender = 'm';

-- problematic code
SELECT * FROM student WHERE age > 18 and gender = 'f' and age <= 24 and address ='kathmandu' or address='pokhara';

SELECT * FROM student WHERE age > 18 and gender = 'f' and age <= 24 and 
(address ='kathmandu' or address='pokhara');

SELECT * FROM student;

SELECT * FROM student WHERE name like 'm%';

SELECT * FROM student WHERE name like '%a';

SELECT * FROM student WHERE name like 'g%a';

SELECT * FROM student WHERE name like '%it%';

SELECT * FROM student WHERE name like '_i%';

SELECT * FROM student WHERE name like '%a_';

ALTER table student add contact varchar(20);

ALTER table student add email varchar(20);

-- aggregation
SELECT AVG(age) FROM student;

SELECT AVG(age) as avg_age FROM student;

SELECT MAX(age) FROM student;

SELECT MIN(age) FROM student;

SELECT SUM(age) FROM student;

SELECT COUNT(id) FROM student;

SELECT COUNT(*) FROM student;


CREATE TABLE college(
    id integer PRIMARY KEY AUTOINCREMENT,
    name varchar(255) NOT NULL,
    location varchar(255)
);

INSERT INTO college ('id', 'name', 'location') VALUES
(1, 'ncit', 'Kathmandu'),
(2, 'islington', 'Kathmandu'),
(3, 'ioe pulchowk', 'Lalitpur');
----------------------------------------------------------------------------------
--- Add college_id as nullable foreign key to student table
----------------------------------------------------------------------------------
ALTER TABLE student
ADD COLUMN college_id INTEGER REFERENCES college(id) NULL;

-- Update student records with college_id
UPDATE student SET college_id = 1 WHERE id IN (1, 3, 6); -- ncit
UPDATE student SET college_id = 2 WHERE id IN (2, 7); -- islington
UPDATE student SET college_id = 3 WHERE id IN (4, 5); -- ioe pulchowk
