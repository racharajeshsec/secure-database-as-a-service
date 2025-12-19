CREATE DATABASE IF NOT EXISTS secure_dbaas;
USE secure_dbaas;

CREATE TABLE healthcare (
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    gender VARBINARY(256),
    age VARBINARY(256),
    weight FLOAT,
    height FLOAT,
    health_history TEXT,
    integrity_tag VARBINARY(256)
);
