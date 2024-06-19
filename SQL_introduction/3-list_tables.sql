-- List all tables from a database passed as argument

SET @sql := CONCAT('SHOW TABLES IN `', DATABASE(), '`');
PREPARE stmt FROM @sql;
EXECUTE stmt;
DEALLOCATE PREPARE stmt;
