-- Create a database named hbtn_0d_usa and a table named states (id, name)

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (
    id INT AUTO_INCREMENT NOT NULL UNIQUE,
    PRIMARY KEY (id),
    name VARCHAR(256) NOT NULL
);
