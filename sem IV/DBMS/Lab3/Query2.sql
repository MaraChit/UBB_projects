--create a stored procedure that inserts data in tables that are in a m:n relationship; 
--if an insert fails, try to recover as much as possible from the entire operation: 
--for example,if the user wants to add a book and its authors, succeeds creating the authors, 
--but fails with the book, the authors should remain in the database 
USE Females
GO

CREATE OR ALTER PROCEDURE addKnown_Recovery
		@fName varchar(50),
		@yob int,
		@nationality varchar(100),
		@profesion varchar(50),
		@year int
	AS
		BEGIN
		DECLARE @fail INT
		SET @fail = 0

		BEGIN TRAN
			--FEMALE
			BEGIN TRY
				IF (dbo.validateFemaleName(@fName)<>1)
					BEGIN
					RAISERROR ('Name must consist only of English letters and ''/- ',14,1)
					END
				IF (dbo.validateNationality(@nationality)<>1)
					BEGIN
					RAISERROR ('Nationality must consist only of English letters ',14,1)
					END
				IF (dbo.validateYoB(@yob)<>1)
					BEGIN
					RAISERROR ('Year of birth must be between 0 and 2020',14,1)
					END

				INSERT INTO Female(FName,YoB,Nationality) VALUES (@fName,@yob,@nationality)
				DECLARE @fid INT
				SET @fid = (SELECT IDENT_CURRENT('Female'))

				SAVE TRAN Female_Point
				PRINT 'Saved Female'

			END TRY

			BEGIN CATCH
				PRINT ERROR_MESSAGE()
				PRINT 'Could not save Female'
				SET @fail = 1
			END CATCH

			BEGIN TRY 
				IF(dbo.validateProfesionName(@profesion)<>1)
					BEGIN
					RAISERROR ('Profesion must consist only of English letters ',14,1)
					END

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

				SAVE TRAN Profesion_Point
				PRINT 'Saved Profesion'
			END TRY

			BEGIN CATCH
				PRINT ERROR_MESSAGE()
				PRINT 'Could not save Profesion'
				ROLLBACK TRAN Female_Point
				SET @fail = 1
			END CATCH

			IF (@fail = 0)
				BEGIN
					BEGIN TRY
						IF (dbo.validateYear(@year)<>1)
							BEGIN
							RAISERROR ('Year must be between 0 and 2020',14,1)
							END
							
						INSERT INTO KnownFor(year,Fid,Pid) VALUES (@year,@fid,@pid)
						COMMIT TRAN
						PRINT 'Saved KnownFor'
						PRINT 'Fully saved all 3 instances'
					END TRY

					BEGIN CATCH
						PRINT ERROR_MESSAGE()
						PRINT 'Transaction rollbacked for KnownFor'
						ROLLBACK TRAN Profesion_Point
						COMMIT TRAN
					END CATCH
				END
			ELSE
				BEGIN
					PRINT ERROR_MESSAGE()
					PRINT 'KnownFor could not be saved'
					COMMIT TRAN
				END
		END

--GOOD CASE
EXEC addKnown_Recovery 'Oana Nourescu',1999,'French','Singer',2018

--BAD CASE
--insertion into female fails
EXEC addKnown_Recovery 'Oana Nourescu',2022,'Romanian','Singer',2018
--insertion into KnownFor fails
EXEC addKnown_Recovery 'Ioana Ionescu',1978,'Romanian','Pilot',2022

SELECT * FROM Female
SELECT * FROM Profesion
SELECT * FROM KnownFor