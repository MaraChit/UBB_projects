--create a scenario that reproduces the update conflict under an optimistic isolation leve
USE Females
GO

WAITFOR DELAY '00:00:10'
BEGIN TRAN
UPDATE Profesion
SET PName = 'Policewoman'
WHERE Pid = 2
WAITFOR DELAY '00:00:10'
COMMIT TRAN

select * from Female
SELECT * FROM Profesion
SELECT * FROM KnownFor