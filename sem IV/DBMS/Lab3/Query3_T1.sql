--create 4 scenarios that reproduce the following concurrency issues under pessimistic isolation levels: 
--dirty reads, non-repeatable reads, phantom reads, and a deadlock;
--find solutions to solve / workaround the concurrency issues
USE Females
GO

--DIRTY READS
BEGIN TRAN
UPDATE Female
SET Nationality = 'French'
WHERE Fid = 1
WAITFOR DELAY '00:00:10'
ROLLBACK TRAN

--NON-REPEATABLE READS
INSERT INTO Profesion(PName) VALUES ('Driver')
BEGIN TRAN
--WAITFOR DELAY '00:00:10'
UPDATE Profesion
SET PName = 'Bus driver'
WHERE Pid = (SELECT IDENT_CURRENT('Profesion'))
COMMIT TRAN

--PHANTOM READS
BEGIN TRAN
WAITFOR DELAY '00:00:10'
INSERT INTO Profesion(PName) VALUES ('Chef')
COMMIT TRAN

--DEADLOCK
BEGIN TRAN
UPDATE Profesion SET PName = 'UBB Student' WHERE Pid = 1
WAITFOR DELAY '00:00:10'
UPDATE Profesion SET PName = 'Pirate' WHERE Pid = 2
COMMIT TRAN

--solution: deadlock priority
SET DEADLOCK_PRIORITY LOW
BEGIN TRAN
UPDATE Profesion SET PName = 'Fairy' WHERE Pid = 1
WAITFOR DELAY '00:00:10'
UPDATE Profesion SET PName = 'Harry Potter fan' WHERE Pid = 2
COMMIT TRAN

SELECT * FROM Female
SELECT * FROM Profesion
SELECT * FROM KnownFor