USE Females
GO

--FEMALE VALIDATORS
CREATE OR ALTER FUNCTION validateFemaleName(@name varchar(50)) RETURNS INT AS
BEGIN
DECLARE @return INT
SET @RETURN = 0
IF (NOT @name LIKE '%[^a-Z ''-]%')
SET @return =1
RETURN @return
END
GO

CREATE OR ALTER FUNCTION validateNationality(@nat varchar(100)) RETURNS INT AS
BEGIN
DECLARE @return INT
SET @RETURN = 0
IF (NOT @nat LIKE '%[^a-Z]%')
SET @return =1
RETURN @return
END
GO

CREATE OR ALTER FUNCTION validateYoB (@yob int) RETURNS INT AS
BEGIN
DECLARE @return INT
SET @return = 0
IF(@yob > 0 AND @yob < 2020)
	SET @return = 1
RETURN @return
END

GO



--PROFESION VALIDATORS
CREATE OR ALTER FUNCTION validateProfesionName(@name varchar(50)) RETURNS INT AS
BEGIN
DECLARE @return INT
SET @RETURN = 0
IF (NOT @name LIKE '%[^a-Z ]%')
SET @return =1
RETURN @return
END
GO

CREATE OR ALTER FUNCTION validateExistence(@profesion varchar(50)) RETURNS INT AS
BEGIN
DECLARE @return INT
SET @return = (SELECT COUNT(*) FROM Profesion P WHERE @profesion=P.PName)
RETURN @return
END

GO

--KNOWN FOR VALIDATORS
CREATE OR ALTER FUNCTION validateYear (@year int) RETURNS INT AS
BEGIN
DECLARE @return INT
SET @return = 0
IF(@year > 0 AND @year < 2020)
	SET @return = 1
RETURN @return
END

GO

SELECT dbo.validateYear(2002)
SELECT dbo.validateFemaleName('Carina')
SELECT dbo.validateFemaleName('English')
SELECT dbo.validateExistence('Singer')
SELECT dbo.validateExistence('Teacher')
