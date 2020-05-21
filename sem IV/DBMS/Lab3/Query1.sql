

--create a stored procedure that inserts data in tables that are in a m:n relationship; 
--if one insert fails, all the operations performed by the procedure must be rolled back 
USE Females
GO

CREATE OR ALTER PROCEDURE addKnown
		@fName varchar(50),
		@nationality varchar(100),
		@yob int,
		@year int,
		@profesion varchar(50)
	AS
		BEGIN
		BEGIN TRAN
			BEGIN TRY
			
				IF (dbo.validateFemaleName(@fName)<>1)
					BEGIN
					RAISERROR('Name must consist only of English letters and ''/- ',14,1)
					END
				IF (dbo.validateNationality(@nationality)<>1)
					BEGIN
					RAISERROR('Name must consist only of English letters ',14,1)
					END
				IF (dbo.validateYoB(@yob)<>1)
					BEGIN
					RAISERROR('Year of birth must be between 0 and 2020 ',14,1)
					END
				IF (dbo.validateProfesionName(@profesion)<>1)
					BEGIN
					RAISERROR('Profesion must consist only of English letters ',14,1)
					END
				IF (dbo.validateYear(@year)<>1)
					BEGIN
					RAISERROR('Year must be between 0 and 2020 ',14,1)
					END

				INSERT INTO Female(FName,YoB,Nationality)VALUES(@fName,@yob,@nationality)
				DECLARE @fid INT
				SET @fid = (SELECT IDENT_CURRENT('Female'))

				IF (dbo.validateExistence(@profesion)<>0)
					BEGIN
					DECLARE @pid INT
					SET @pid = (SELECT Pid FROM Profesion WHERE PName = @profesion)
					PRINT 'EXISTS IN DB'
					END
				ELSE
					BEGIN
					INSERT INTO Profesion(PName)VALUES(@profesion)
					SET @pid = (SELECT IDENT_CURRENT('Profesion'))
					PRINT 'INSERTED'
					END
					

				INSERT INTO KnownFor(year,Fid,Pid) VALUES (@year,@fid,@pid)

				COMMIT TRAN
				PRINT 'Transaction committed'
			END TRY

			BEGIN CATCH
				PRINT ERROR_MESSAGE()
				PRINT 'Transaction rollbacked'
				ROLLBACK TRAN
			END CATCH
		END

--good case
EXEC addKnown 'Mara Chit','Romanian',1999,2018,'Student'

--bad case
--fails knownFor because of year > 2020
EXEC addKnown 'Mara Chitt','Romanian',1999,2022,'Student'

SELECT * FROM Female
SELECT * FROM Profesion
SELECT * FROM KnownFor
