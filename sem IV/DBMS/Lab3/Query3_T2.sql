USE Females
GO

--- DIRTY READS
SET TRANSACTION ISOLATION LEVEL READ UNCOMMITTED
BEGIN TRAN
SELECT * FROM Female
WAITFOR DELAY '00:00:15'
SELECT * FROM Female
COMMIT TRAN

-- solution
SET TRANSACTION ISOLATION LEVEL READ COMMITTED
BEGIN TRAN
SELECT * FROM Female
WAITFOR DELAY '00:00:15'
SELECT * FROM Female
COMMIT TRAN

--- NON-REPEATABLE READS
SET TRANSACTION ISOLATION LEVEL READ COMMITTED
BEGIN TRAN
SELECT * FROM Profesion
WAITFOR DELAY '00:00:15'
SELECT * FROM Profesion
COMMIT TRAN

-- solution
SET TRANSACTION ISOLATION LEVEL REPEATABLE READ
BEGIN TRAN
SELECT * FROM Profesion
WAITFOR DELAY '00:00:15'
SELECT * FROM Profesion
COMMIT TRAN

--- PHANTOM READS
SET TRANSACTION ISOLATION LEVEL REPEATABLE READ
BEGIN TRAN
SELECT * FROM Profesion
WAITFOR DELAY '00:00:15'
SELECT * FROM Profesion
COMMIT TRAN

-- solution
SET TRANSACTION ISOLATION LEVEL SERIALIZABLE
BEGIN TRAN
SELECT * FROM Profesion
WAITFOR DELAY '00:00:15'
SELECT * FROM Profesion
COMMIT TRAN

--- DEADLOCK
BEGIN TRANSACTION
UPDATE Profesion SET PName = 'UBB Student' WHERE Pid = 2
WAITFOR DELAY '00:00:10'
UPDATE Profesion SET PName = 'Pirate' WHERE Pid = 1
COMMIT TRAN


-- solution: deadlock priority
SET DEADLOCK_PRIORITY HIGH
BEGIN TRANSACTION
UPDATE Profesion SET PName = 'UBB Student' WHERE Pid = 2
WAITFOR DELAY '00:00:10'
UPDATE Profesion SET PName = 'Pirate' WHERE Pid = 1
COMMIT TRAN

select * from Female
select * from Profesion
select * from KnownFor