CREATE DATABASE HistoricalFemales
GO
USE HistoricalFemales
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

