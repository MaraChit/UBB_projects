CREATE DATABASE HistoricalFemaleFigures
GO
USE HistoricalFemaleFigures
GO

CREATE TABLE Century(
CeID INT PRIMARY KEY,
Number VARCHAR(10) NOT NULL)

CREATE TABLE Nationality(
Nid INT PRIMARY KEY,
Name VARCHAR(30) NOT NULL)

CREATE TABLE Female(
Fid INT PRIMARY KEY,
Name VARCHAR(50) NOT NULL,
YoB INT,
CeID INT FOREIGN KEY REFERENCES Century(CeID),
Nid INT FOREIGN KEY REFERENCES Nationality(Nid))

CREATE TABLE Husband(
Hid INT PRIMARY KEY,
Name VARCHAR(50) NOT NULL,
YoB INT)


CREATE TABLE Marriage(
Fid INT FOREIGN KEY REFERENCES Female(Fid),
Hid INT FOREIGN KEY REFERENCES Husband(Hid),
year INT,
length INT,
divorce VARCHAR(5),  
CONSTRAINT PK_MARRIAGE PRIMARY KEY(Fid, Hid))

CREATE TABLE Profession(
Pid INT PRIMARY KEY,
Name VARCHAR(50) NOT NULL)

CREATE TABLE KnownFor(
Fid INT FOREIGN KEY REFERENCES Female(Fid),
Pid INT FOREIGN KEY REFERENCES Profession(Pid),
year INT CHECK (year > 0 AND year <=2019),
CONSTRAINT PK_KNOWN_FOR PRIMARY KEY(Fid,Pid))

CREATE TABLE Kids(
Kid INT PRIMARY KEY,
Name VARCHAR(50) not null,
Gender VARCHAR(30),
fromMarriage VARCHAR(30),
Fid INT FOREIGN KEY REFERENCES Female(Fid))

CREATE TABLE Country(
Cid INT PRIMARY KEY,
Name VARCHAR(70) NOT NULL)

CREATE TABLE Moved_To(
Fid INT FOREIGN KEY REFERENCES Female(Fid),
Cid INT FOREIGN KEY REFERENCES Country(Cid),
Year INT,
reason VARCHAR(30),
CONSTRAINT PK_MOVED_TO PRIMARY KEY(Fid, Cid))

INSERT INTO Century(CeID,Number)
VALUES (1, 'X'),
	   (2, 'XI'),
	   (3,'XII'),
	   (4, 'XIII'),
	   (5,'XV'),
	   (6,'XVI'),
	   (7,'XVII'),
	   (8,'XVIII'),
	   (9,'XIX'),
	   (10,'XX');

INSERT INTO Nationality(Nid,Name)
VALUES (1, 'French'),
	   (2, 'Spanish'),
	   (3, 'Romanian'),
	   (4, 'English'),
	   (5, 'Italian'),
	   (6, 'Polish'),
	   (7, 'German'),
	   (8, 'Irish'),
	   (9, 'Scottish'),
	   (10, 'Swis'),
	   (11, 'Austrian'),
	   (12, 'Belgian'),
	   (13, 'Portugese'),
	   (14, 'Greek'),
	   (15, 'Danish'),
	   (16, 'Croatian'),
	   (17, 'Egiptian'),
	   (18, 'Japanese'),
	   (19, 'Chinese'),
	   (20, 'American');

INSERT INTO Female(Fid,Name,YoB,CeID,Nid)
VALUES (1, 'Anne Boleyn',null,5,4),
	   (2, 'Catherine of Aragon',1485,5,2),
	   (3, 'Jane Seymour',null,5,4),
	   (4, 'Amelia Earhart',1897,9,20),
	   (5, 'Marie Curie',1867,9,6),
	   (6, 'Jane Austen',1775,8,4),
	   (7, 'Mary Stuart',1542,6,9);

INSERT INTO Female(Fid,Name,YoB,CeID,Nid)
VALUES (44, 'Amelia Earhart2',1897,9,20)

INSERT INTO Female(Fid,Name,YoB,CeID,Nid)
VALUES (10, 'Princess Diana',1961,10,4)

INSERT INTO Husband(Hid,Name,YoB)
VALUES (1, 'Henry VIII',1491),
	   (2, 'Arthur Tudor',1486),
	   (3, 'Francisc II',1544),
	   (4, 'Lord Darnley',1545),
	   (5, 'James Bothwell',1534),
	   (6, 'Pierre Curie',1859),
	   (7, 'George P. Putnam',1887);

INSERT INTO Husband(Hid,Name,YoB)
VALUES (11, 'Prince Charles',1948)

INSERT INTO Marriage(Fid,Hid,year,length,divorce)
VALUES (1,1,1533,3,'yes'),
       (2,1,1509,23,'yes'),
	   (2,2,1501,1,'no'),
	   (3,1,1536,1,'no'),
	   (4,7,1931,8,'no'),
	   (5,6,1895,11,'no'),
	   (7,3,1558,2,'no'),
	   (7,4,1565,2,'no'),
	   (7,5,1567,11,'no');

INSERT INTO Marriage(Fid,Hid,year,length,divorce)
VALUES (10,11,1981,15,'yes')

INSERT INTO Marriage(Fid,Hid,year,length,divorce)
VALUES (5,2,NULL,NULL,NULL),
	   (7,1,null,null,null)

INSERT INTO Profession(Pid, Name)
VALUES (1, 'queen'),
	   (2, 'writer'),
	   (3, 'pilot'),
	   (4, 'painter'),
	   (5, 'physicist');

INSERT INTO Profession(Pid, Name)
VALUES (6, 'princess'),
	   (7, 'lady in waiting'),
	   (8, 'regent'),
	   (9, 'warrior');


INSERT INTO Kids(Kid,Name,Gender,fromMarriage,Fid)
VALUES (1, 'Elizabeth I', 'female',1, 1),
	   (2, 'Mary Tudor', 'female',2, 2),
	   (3, 'Edward VI', 'male', 1, 3),
	   (4, 'James ', 'male',2, 7);

INSERT INTO Female(Fid,Name,YoB,CeID,Nid)
VALUES (7, 'Mary Shelly',1797,8,4);
--error because the id already exists in the database

INSERT INTO Female(Fid,Name,YoB,CeID,Nid)
VALUES (8, 'Mary Shelly',1797,9,4);

INSERT INTO KnownFor(Fid, Pid, year)
VALUES (1,1, 1533),
	   (2,1, 1509),
	   (1,7, 1530),
	   (2,6,1500);

INSERT INTO KnownFor(Fid, Pid, year)
VALUES (3,1, 1536),
	   (7,1, 1558)

INSERT INTO KnownFor(Fid, Pid, year)
VALUES (5,5, 1870)

UPDATE Female
SET CeID=8
WHERE Name='Mary Shelly'
 
UPDATE Profession
SET Name ='Queen of England'
WHERE Name='queen'

UPDATE Marriage
SET divorce = '?'
WHERE divorce is NULL

DELETE FROM Marriage WHERE length is null

/* 
	a. 2 queries with the union operation; use UNION [ALL] and OR;
	
	:show the females that are either English or were born in the XVI century 
	:show TOP 3 husbands that divorced or were married for less thand 2yearS */
SELECT *
FROM Female
WHERE CeID=6
UNION
SELECT *
FROM Female
WHERE Nid = 4


SELECT TOP 3 *
FROM Husband H, Marriage M
WHERE H.Hid=M.Hid and M.divorce = 'yes' OR H.Hid=M.Hid and M.length <2

/*
	b. 2 queries with the intersection operation; use INTERSECT and IN;

	:select the females that have the name starting with A that have an unknown YoB
	:show the females that have kids*/

SELECT f1.Name
FROM Female f1
WHERE f1.Name like 'A_%'
INTERSECT
SELECT f2.Name
FROM Female f2
WHERE f2.YoB is null
ORDER BY f1.Name

SELECT F.Name
FROM Female F
WHERE  F.Fid IN (SELECT K.Fid
				 FROM Kids K) 


/* c. 2 queries with the difference operation; use EXCEPT and NOT IN;

	:show all kids that are from a second marriage and have NOT English mothers 
	:select the females that do not have kids in he db*/
SELECT K1.Name
FROM Kids K1
WHERE K1.fromMarriage=2 
EXCEPT
SELECT K2.NAME
FROM KIDS K2, Female F
WHERE K2.Fid=F.Fid AND F.Nid=4

SELECT F.Name
FROM Female F
WHERE F.Fid NOT IN ( SELECT K.Fid
					 FROM Kids K, Female F2
					 WHERE K.Fid = F2.Fid)

					  
/*	
d. 4 queries with INNER JOIN, LEFT JOIN, RIGHT JOIN, and FULL JOIN; 
  one query will join at least 3 tables, while another one will join at least two many-to-many relationships;
		:all married females and their marriage information 
		:show all females, their YoB and their husbands and yob 
		:show all females who were queens and had a marriage longer than 3 years
		:show the kids whosw mother's name starts with J*/

SELECT DISTINCT F.Name, M.year, M.length, M.divorce
FROM Female F INNER JOIN Marriage M ON F.Fid = M.Fid


SELECT F.Name, F.YoB , H.Name, H.YoB
FROM Female F FULL JOIN Marriage M ON F.Fid=M.Fid
									FULL JOIN Husband H ON H.Hid = M.Hid

SELECT F.Name
FROM Female F RIGHT JOIN Marriage M ON F.Fid = M.Fid
									RIGHT JOIN KnownFor K ON K.Fid= F.Fid
														  RIGHT JOIN Profession P ON K.Pid = P.Pid
WHERE P.Name = 'Queen of England' AND M.length>3 

SELECT K.Name
FROM Kids K LEFT JOIN Female F ON F.Fid=K.Fid
WHERE F.Name LIKE 'J_%'

/*e. 2 queries using the IN operator to introduce a subquery in the WHERE clause; 
	in at least one query, the subquery should include a subquery in its own WHERE clause;
	:find the husbands that were married more than once
	:show the nationalities of the females that were married for more than 10 years
	*/

SELECT H.Name
FROM Husband H
WHERE H.Hid IN ( SELECT M1.Hid
				 FROM Marriage M1, Marriage M2
				 WHERE M1.Hid = M2.Hid AND M1.Fid<>M2.Fid)

SELECT N.Name
FROM Nationality N
WHERE N.Nid IN ( SELECT F.Nid
				 FROM Female F
				 WHERE F.Fid IN ( SELECT F.Fid
								  FROM Female F, Marriage M
								  WHERE F.Fid = M.Fid AND M.length >10))
/*f. 2 queries using the EXISTS operator to introduce a subquery in the WHERE clause; 
		: show the kids who have English mothers
		: show all husbands that have divorced	*/

SELECT K.Name
FROM Kids K
WHERE EXISTS ( SELECT F.Name 
			   FROM Female F
			   WHERE K.Fid = F.Fid AND F.Nid= 4)

SELECT H.Name
FROM Husband H
WHERE EXISTS ( SELECT M.length
			   FROM Marriage M
			   WHERE M.Hid=H.Hid AND M.divorce='yes')

/* g. 2 queries with a subquery in the FROM clause;  
		: show the marriages from the XVI century, ordered by length
		: show the English females born in the XV century, ordered by name*/

SELECT t.year, t.length
FROM ( SELECT *
	   FROM Marriage mariagge
	   WHERE mariagge.year > 1499 AND mariagge.year < 1600) as t
ORDER BY t.length


SELECT f.Name, f.YoB
FROM (SELECT *
	  FROM Female F
	  WHERE F.CeID='5' AND F.Nid='4' ) AS f
ORDER BY f.Name



/*h. 4 queries with the GROUP BY clause, 3 of which also contain the HAVING clause;
		2 of the latter will also have a subquery in the HAVING clause; use the aggregation operators: COUNT, SUM, AVG, MIN, MAX;
		:for each female find the number of husbands and the total years they were married
		:find the females that were married for at least 5 years
		:find the females with at least two professions 
		:shows the year in which at least 2 females were born
		*/
SELECT F.Fid, COUNT (*) AS no_hb, SUM(length) AS sum_length
FROM Female F, Marriage M
WHERE F.Fid=M.Fid 
GROUP BY  F.Fid

SELECT F.Fid, AVG(length) AS avg_length
FROM Female F, Marriage M
WHERE F.Fid=M.Fid
GROUP BY F.Fid
HAVING AVG(length)>=5

SELECT F.Fid, COUNT(K.Pid) AS nr_profession
FROM Female F, KnownFor K INNER JOIN Profession P ON P.Pid=K.Pid
WHERE F.Fid=K.Fid 
GROUP BY F.Fid
HAVING COUNT(K.Pid)>1

SELECT F.YoB
FROM Female F
GROUP BY F.YoB
HAVING 1< (SELECT COUNT(*)
		   FROM Female F2
		   WHERE F2.YoB = F.YoB)

/* i. 4 queries using ANY and ALL to introduce a subquery in the WHERE clause;
	2 of them should be rewritten with aggregation operators,
	while the other 2 should also be expressed with [NOT] IN. 
	:show the husbands who were born earlier than all the husbands who had a divorce
	:show the kids who don't have English mothers 
	:show the females who are knowk for a profesion different than physicist
	:show the marriages that ended in divorce that happened after all the marriages that did not end in a divorce*/

SELECT H.Name
FROM Husband H
WHERE H.YoB < ALL (SELECT DISTINCT H2.YoB
				   FROM Husband H2, Marriage M
				   WHERE H2.Hid=M.Hid AND M.divorce='yes')
ORDER BY H.Name

SELECT H.Name
FROM Husband H
WHERE H.YoB < (SELECT MIN( H2.YoB)
				   FROM Husband H2, Marriage M
				   WHERE H2.Hid=M.Hid AND M.divorce='yes')
ORDER BY H.Name
	

SELECT K.Name
FROM Kids K
WHERE K.Fid <> ALL ( SELECT DISTINCT F.Fid
					 FROM Female F
					 WHERE F.Nid = 4 )

SELECT K.Name
FROM Kids K
WHERE K.Fid NOT IN ( SELECT DISTINCT F.Fid
					 FROM Female F
					 WHERE F.Nid = 4 )


SELECT F.Name
FROM Female F
WHERE F.Fid = ANY ( SELECT DISTINCT F.Fid
					FROM Female F INNER JOIN KnownFor K ON F.Fid=K.Fid
											INNER JOIN Profession P ON K.Pid=P.Pid
					WHERE P.Name != 'physicist')

SELECT F.Name
FROM Female F
WHERE F.Fid in ( SELECT DISTINCT F.Fid
					FROM Female F INNER JOIN KnownFor K ON F.Fid=K.Fid
											INNER JOIN Profession P ON K.Pid=P.Pid
					WHERE P.Name != 'physicist')


SELECT M.year
FROM Marriage M
WHERE M.year > all ( SELECT DISTINCT M.year
					 FROM Marriage M
					 WHERE M.divorce = 'no')


SELECT M.year
FROM Marriage M
WHERE M.year > ( SELECT MAX( M.year)
					 FROM Marriage M
					 WHERE M.divorce = 'no')
