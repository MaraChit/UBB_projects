--model examen practic
--entities: trains, train types, stations, routes

CREATE DATABASE TrainSchedule
GO
USE TrainSchedule
GO

IF OBJECT_ID('RoutesStation','U') IS NOT NULL
	DROP TABLE RoutesStation
IF OBJECT_ID('Station','U') IS NOT NULL
	DROP TABLE Station
IF OBJECT_ID('Routes','U') IS NOT NULL
	DROP TABLE Routes
IF OBJECT_ID('Trains','U') IS NOT NULL
	DROP TABLE Trains
IF OBJECT_ID('TrainTypes','U') IS NOT NULL
	DROP TABLE TrainTypes
GO

CREATE TABLE TrainTypes(
TypeId INT PRIMARY KEY IDENTITY(1,1),
Tdescription VARCHAR(50))

CREATE TABLE Trains(
Tid INT PRIMARY KEY IDENTITY(1,1),
TName VARCHAR(20),
TypeId INT FOREIGN KEY REFERENCES TrainTypes(TypeId))

CREATE TABLE Stations(
Sid INT PRIMARY KEY IDENTITY(1,1),
SName VARCHAR(50) UNIQUE)

CREATE TABLE Routes(
Rid INT PRIMARY KEY IDENTITY(1,1),
RName VARCHAR(50) UNIQUE,
Tid INT FOREIGN KEY REFERENCES Trains(Tid))

CREATE TABLE RS(
Rid INT FOREIGN KEY REFERENCES Routes(Rid),
Sid INT FOREIGN KEY REFERENCES Stations(Sid),
ArrivalTime time,
DepartureTime time,
CONSTRAINT pk_RS PRIMARY KEY(Rid,Sid))

INSERT INTO TrainTypes VALUES ('description 1'),('description 2')
INSERT INTO Trains VALUES ('InterRegio',1),('InterCity',1),('Regio',2)
INSERT INTO Stations VALUES ('Cluj'),('Brasov'),('Bucuresti')
INSERT INTO Routes VALUES ('Sighisora',1),('Medias',2)
INSERT INTO RS VALUES (1,1,'12:00:00','18:00:00'),(1,2,'15:30:00','22:42:00'),(2,2,'08:05:00','21:48:00')
GO

select * from TrainTypes
select * from Trains
select * from Stations
select * from Routes
select * from RS
GO

CREATE OR ALTER PROCEDURE Add_RS @rid INT, @sid INT, @at time, @dt time
AS
BEGIN
DECLARE @no INT
SET @no = 0
SELECT @no=count(*)FROM RS WHERE Rid=@rid AND Sid=@sid
IF(@no<>0)
	BEGIN
	UPDATE RS
	SET ArrivalTime=@at, DepartureTime=@dt
	WHERE Rid=@rid AND Sid=@sid
	END
ELSE
	BEGIN
	INSERT INTO RS VALUES(@rid,@sid,@at,@dt)
	END
END

SELECT * FROM RS
EXEC Add_RS 2,1,'5:00:00','9:00:00'
SELECT * FROM RS
go

CREATE OR ALTER VIEW view1
AS
SELECT RName
FROM Routes  INNER JOIN RS ON Routes.Rid=RS.Rid 
			 GROUP BY RName
			 HAVING COUNT(*)=(SELECT COUNT(*)
							  FROM Stations)
go

SELECT * FROM view1
GO

CREATE OR ALTER FUNCTION fct(@r INT)
RETURNS TABLE
AS
RETURN
SELECT DISTINCT S.Sid,SName, COUNT(SName) as NoOfRoutes
FROM Stations S INNER JOIN RS ss ON ss.Sid=S.Sid
GROUP BY S.Sid, SName
HAVING COUNT(SName)>=@r

go