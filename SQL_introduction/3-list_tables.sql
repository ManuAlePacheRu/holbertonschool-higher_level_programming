-- List all tables from a database passed as argument

SET @operation := CONCAT('SHOW TABLES IN `', DATABASE(), '`');
PREPARE consult FROM @operation;
EXECUTE consult;
DEALLOCATE PREPARE consult;
