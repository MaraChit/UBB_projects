create database Females
go

use Females
go

create table Female(
Fid int primary key identity(1,1),
FName varchar(50),
YoB int,
Nationality varchar(100))

create table Profesion(
Pid int primary key identity(1,1),
PName varchar(50))

create table KnownFor(
Kid int primary key identity(1,1),
year int,
Fid int foreign key references Female(Fid),
Pid int foreign key references Profesion(Pid))

INSERT INTO Female(FName, YoB, Nationality) VALUES 
('Andreea Corlaci', 2005, 'French'),
('Cristina Bogdan', 1978, 'Romanian'),
('Daria Sabina', 2000, 'Romanian')

INSERT INTO Profesion(PName) VALUES ('Opera singer'),('Producer'),('Designer')

INSERT INTO KnownFor(year, Fid, Pid) VALUES (2019, 1, 3),(2000, 2, 1), (2012, 3, 1)

SELECT * FROM Female
SELECT * FROM Profesion
SELECT * FROM KnownFor