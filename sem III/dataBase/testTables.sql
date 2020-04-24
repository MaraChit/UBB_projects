DECLARE @tableName VARCHAR(50)
	DECLARE @tableData VARCHAR(30)

DECLARE Tble CURSOR FOR
	SELECT VALUE
	FROM STRING_SPLIT( 'a a1 a2;b b1;c' , ';')
	OPEN Tble
	
	FETCH NEXT FROM Tble INTO @tableData
	DEClARE x CURSOR 
	WHILE @@FETCH_STATUS = 0
	BEGIN
		PRINT @tableData
		FETCH NEXT FROM Tble INTO @tableData
	END
	
	CLOSE Tble
	DEALLOCATE Tble
	
	


CREATE OR ALTER PROCEDURE createTest
(@testName VARCHAR (30), @data VARCHAR (500), @viewData VARCHAR(500) )
AS 
BEGIN

	--DECLARE @testId INT
	DECLARE @tableName VARCHAR(50)
	DECLARE @tableData VARCHAR(30)

	DECLARE Tble CURSOR FOR
	SELECT VALUE
	FROM STRING_SPLIT( @data , ';')
	OPEN Tble
	FETCH Tble
	INTO @tableData
	WHILE @@FETCH_STATUS = 0
	BEGIN
	DECLARE namee CURSOR FOR
	SELECT VALUE
	FROM STRING_SPLIT(@tableData , ',')
	OPEN namee
	FETCH namee
	END
	CLOSE Tble
	DEALLOCATE Tble
	
	



END


select o.name, c.name, c.column_id, t.name
from sys.objects o inner join sys.columns c on o.object_id = c.object_id
  inner join sys.types t on c.system_type_id = t.system_type_id
where o.type = 'U' AND o.name = 'Century'


CREATE OR ALTER PROCEDURE InsertRandom  @TableName varchar(100), @nr int
AS
			
	DECLARE @Index INT
	SET @Index=1
	WHILE @Index<=@nr
	BEGIN
		DECLARE @Command VARCHAR(1000)
		SET @Command = 'INSERT INTO '+@TableName+' '
		DECLARE @CIndex INT
		SET @CIndex=1

		DECLARE @ValuesType varchar(100)

		SET @ValuesType =(select t.name
							from sys.objects o inner join sys.columns c on o.object_id = c.object_id
							inner join sys.types t ON c.system_type_id = t.system_type_id
							where o.name = @TableName and c.column_id=@CIndex)
		
		DECLARE @Values varchar(1000)
		
		SET @Values = 'VALUES ('+CONVERT(varchar(10), @Index)

		SET @CIndex =@CIndex+1
		
		WHILE @ValuesType IS NOT NULL
		BEGIN
			SET @Values= @Values+', '
			
			SET @ValuesType =(select t.name
							from sys.objects o inner join sys.columns c on o.object_id = c.object_id
							inner join sys.types t ON c.system_type_id = t.system_type_id
							where o.name = @TableName and c.column_id=@CIndex)
			
			IF @ValuesType = 'int'  AND @CIndex = 2
			BEGIN
				SET @Values=@Values+CONVERT(varchar(10), @Index)
			END
			ELSE
			BEGIN
				IF @ValuesType = 'int'
				BEGIN
					DECLARE @rInt int
					SET @rInt =RAND()*(@nr-1)+1
					SET @Values = @Values+CONVERT(VARCHAR(20),@rInt)
				END
			END
			IF @ValuesType = 'varchar'
			BEGIN
				DECLARE @str VARCHAR(15)
				SET @str = CHAR(39)
				DECLARE @num INT
				SET @num = RAND()*(10-1)+1
				DECLARE @c VARCHAR(1)
				WHILE @num > 0
				BEGIN
					SET @c = CHAR(CAST(RAND()*(122-97)+97 as INT))
					SET @str = CONCAT(@str,@c)
					SET @num=@num-1
				END
				SET @str = CONCAT(@str, char(39))
				SET @Values = @Values+@str
			END

			SET @CIndex =@CIndex+1

			SET @ValuesType =(select t.name
							from sys.objects o inner join sys.columns c on o.object_id = c.object_id
							inner join sys.types t ON c.system_type_id = t.system_type_id
							where o.name = @TableName and c.column_id=@CIndex)
			
		END
		SET @Values = @Values + ')'
		
		SET @Command = @Command+@Values
		
		EXEC (@Command)
	SET @Index=@Index+1
	END
GO