--create db--
create database organizations;
go
use organizations;
go

CREATE TABLE Organization(
OID int NOT NULL PRIMARY KEY,
org_name varchar(225) NOT NULL,
headquarter varchar(225),
founded_year int);

CREATE TABLE Continent(
ConID int NOT NULL PRIMARY KEY,
con_name varchar(100));

CREATE TABLE Country(
CID int NOT NULL PRIMARY KEY,
country_name varchar(225) NOT NULL,
capital varchar(225),
area BIGINT,
population float,
ConID int FOREIGN KEY REFERENCES Continent(ConID));

CREATE TABLE Joined(
OID int FOREIGN KEY REFERENCES Organization(OID),
CID int FOREIGN KEY REFERENCES Country(CID),
CONSTRAINT PK_joined PRIMARY KEY (OID,CID));

-- insert data --
INSERT INTO Continent (ConID, con_name)
VALUES (1, 'Europe'),
	   (2, 'Asia'),
	   (3, 'North America'),
	   (4, 'South America'),
	   (5, 'Africa'),
	   (6, 'Australia'),
	   (7, 'Antarctica');

INSERT INTO Organization(OID,org_name,headquarter, founded_year)
VALUES (1, 'UNICEF', 'New York', 1946),
	   (2, 'NATO', 'Washington DC', 1949),
	   (3, 'Nordic Council of Ministers', 'Copenhagen', 1971),
	   (4, 'United Nations High Commissioner for Human Rights (UNHCHR)', 'Geneva', 1993),
	   (5, 'United Nations Office on Drugs and Crime (UNODC)', 'Vienna', 1997),
	   (6, 'World Wide Fund for Nature (WWF)', 'Gland', 1961);

INSERT INTO Country(CID, country_name, capital,	area, population, ConID)
VALUES (1, 'USA', 'Washington DC', 9372610, 328.2, 3),
	   (2, 'Austria', 'Vienna', 83879, 8.859, 1),
	   (3, 'Denmark', 'Copenhagen', 42933, 5.806, 1),
	   (4, 'Romania', 'Bucharest', 238391, 19.41, 1),
	   (5, 'Switzerland', 'Bern', 41285, 8.545, 1),
	   (6, 'Russia', 'Moscow', 17098242,144.4, 2),
	   (7, 'Egypt', 'Cairo', 1002450 , 100.4, 5),
	   (8, 'Argentina', 'Buenos Aires', 2780400, 44.94, 4),
	   (9, 'Canada', 'Ottawa', 9984670, 37.59, 3);

INSERT INTO Joined(OID,CID)
VALUES (2,1),
	   (2,3),
	   (2,4),
	   (2,9),
	   (1,9),
	   (1,5),
	   (1,1);

-- queries --

-- 1. List all the countries which are members of NATO.
SELECT C.country_name
FROM Country C JOIN Joined J ON C.CID=J.CID join Organization O ON O.OID = J.OID
WHERE O.org_name = 'NATO'

--2. List all the countries which are members of organizations founded before 1980
SELECT C.country_name
FROM Country C JOIN Joined J ON C.CID=J.CID join Organization O ON O.OID = J.OID
WHERE O.founded_year < 1980

--3. List all the countries which are members of only one organization
SELECT C.country_name
FROM Country C 
WHERE C.CID IN (SELECT C.CID
				FROM Country C INNER JOIN Joined J ON C.CID=J.CID INNER join Organization O ON O.OID = J.OID
				GROUP BY C.CID 
				HAVING COUNT(*)=1)


--4. List all the capitals which are headquarter of no organization
SELECT C.capital
FROM Country C
WHERE C.capital NOT IN (SELECT O.headquarter
						FROM Organization O)

--5. List the population of each continent
SELECT Co.con_name, SUM(C.population) AS continent_population
FROM Continent Co INNER JOIN Country C ON Co.ConID = C.ConID
GROUP BY Co.con_name

--6. Count the countries of each continent
SELECT Co.con_name, COUNT(*) AS continent_countries
FROM Continent Co INNER JOIN Country C ON Co.ConID = C.ConID
GROUP BY Co.con_name 