CREATE TABLE student(
	id int primary key,
	name varchar not null,
	address varchar not null,
	college varchar not null,
	age int not null,
	gender varchar(1) not null,
	faculty varchar not null
);

INSERT INTO student 
('id', 'name', 'address', 'college', 'age', 'gender', 'faculty')
VALUES
(1, 'ram', 'kathmandu', 'ncit', 18, 'm', 'IT'),
(2, 'shyam', 'lalitpur', 'islington', 20, 'm', 'CSIT'),
(3, 'gita', 'pokhara', 'ncit', 21, 'f', 'SE'),
(4, 'sita', 'kathmandu', 'ioe pulchowk', 24, 'f','CE');

-- * means get all columns FROM student table
SELECT * FROM student;

SELECT name, address FROM student;

UPDATE student set address = 'lalitpur' WHERE id = 3;

ALTER table student add university varchar default 'TU';

UPDATE student set university = 'UK' WHERE college='islington';

UPDATE student set university = 'PK' WHERE id=1 or id=3;

DELETE FROM student WHERE id = 3;

INSERT into student 
('id', 'name', 'address', 'college', 'age', 'gender', 'faculty')
VALUES
(3, 'gita', 'pokhara', 'ncit', 21, 'f', 'SE'),
(5, 'hari', 'kathmandu', 'ioe pulchowk', 24, 'm','CIVIL'),
(6, 'madan', 'pokhara', 'ncit', 21, 'f', 'SE'),
(7, 'maya', 'kathmandu', 'islington', 24, 'f','BIT');

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

SELECT * FROM student WHERE name like '%t_';

ALTER table student add contact varchar(20);

ALTER table student add email varchar(20);

-- aggregation
SELECT AVG(age) FROM student;

SELECT AVG(age) as 'Average Age' FROM student;

SELECT MAX(age) FROM student;

SELECT MIN(age) FROM student;

SELECT SUM(age) FROM student;

SELECT COUNT(id) FROM student;

SELECT COUNT(*) FROM student;





