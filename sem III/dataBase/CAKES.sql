CREATE DATABASE Cakes
GO
USE Cakes
GO

IF OBJECT_ID('PlaceOrder','U') IS NOT NULL
	DROP TABLE PlaceOrder
IF OBJECT_ID('Orders','U') IS NOT NULL
	DROP TABLE Orders
IF OBJECT_ID('Cake','U') IS NOT NULL
	DROP TABLE Cake
IF OBJECT_ID('CTypes','U') IS NOT NULL
	DROP TABLE CTypes
IF OBJECT_ID('Chef','U') IS NOT NULL
	DROP TABLE Chef
GO

CREATE TABLE CTypes(
Tid INT PRIMARY KEY IDENTITY(1,1),
TName VARCHAR(20),
Descc VARCHAR(100) )

CREATE TABLE Chef(
ChID INT PRIMARY KEY IDENTITY(1,1),
ChName VARCHAR(20),
Gender VARCHAR(20),
DoB VARCHAR(100))

CREATE TABLE Cake(
Cid INT PRIMARY KEY IDENTITY(1,1),
CName VARCHAR(100),
CShape VARCHAR(40),
CWeight INT,
ChID INT FOREIGN KEY REFERENCES Chef(ChID),
Tid INT FOREIGN KEY REFERENCES CTypes(TId))

CREATE TABLE Orders(
Oid INT PRIMARY KEY IDENTITY(1,1),
DATE VARCHAR(50))

CREATE TABLE PlaceOrder(
Cid INT FOREIGN KEY REFERENCES Cake(Cid),
Oid INT FOREIGN KEY REFERENCES Orders(Oid),
Quantity INT,
CONSTRAINT pk_PO PRIMARY KEY(Cid,Oid))

INSERT INTO CTypes VALUES ('CHEESECAKES','WITH CHEESE'),('FRUIT CAKES','WITH FRUITS')
INSERT INTO Chef VALUES('BOB','M','12.11.1990'),('MEG','F','14.08.1992')
INSERT INTO Cake VALUES('CHEESECAKE OREO','ROUND',900,1,1),('CHEESECAKE VANILLA','ROUND',1100,1,2),('DIPLOMAT','SQUARE',500,2,1)
INSERT INTO Orders VALUES('12.01.2019'),('24.05.2019')
INSERT INTO PlaceOrder VALUES (1,1,5),(1,2,1),(2,1,3),(3,2,4)

--SELECT * FROM Cake
go

CREATE OR ALTER PROCEDURE P1 @oid INT, @cname VARCHAR(100), @p INT
AS
BEGIN
DECLARE @no INT
SET @no = 0
DECLARE @cid INT

SET @cid = (SELECT CID FROM Cake WHERE @cname=CName)

SELECT @no=count(*)FROM PlaceOrder WHERE Oid=@oid AND Cid=@cid
IF(@no<>0)
	BEGIN
	UPDATE PlaceOrder
	SET Quantity=@p
	WHERE Oid=@oid AND Cid=@cid
	END
ELSE
	BEGIN
	INSERT INTO PlaceOrder VALUES(@cid,@oid,@p)
	END
END

exec P1 2,'CHEESECAKE OREO',5 
EXEC P1 2,'CHEESECAKE OREO',11
EXEC P1 1,'DIPLOMAT',10
SELECT * FROM PlaceOrder