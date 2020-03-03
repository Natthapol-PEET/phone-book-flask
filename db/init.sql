CREATE DATABASE project;

use project;

CREATE TABLE phone (
id_phone INT AUTO_INCREMENT PRIMARY KEY,
phone  varchar(10) NOT NULL ,
name   varchar(40) NOT NULL 
) CHARACTER SET utf8 COLLATE utf8_unicode_ci;

INSERT INTO phone (phone, name) VALUES ("0931851721", "PEET");
