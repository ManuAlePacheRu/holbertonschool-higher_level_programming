-- Create a table in the database passed as argument

CREATE TABLE IF NOT EXISTS first_table (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);

-- SET @database_name_get := DATABASE()
-- SET @create_table_new := CONCAT('CREATE TABLE IF NOT EXISTS ', @database_name_get, '.first_table (
-- id INT AUTO_INCREMENT PRIMARY KEY,
-- name VARCHAR(256) NOT NULL)');
-- PREPARE create_table FROM @create_table_new;
-- EXECUTE create_table;
-- DEALLOCATE PREPARE create_table;
