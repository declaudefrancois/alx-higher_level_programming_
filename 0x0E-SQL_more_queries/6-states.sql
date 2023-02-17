-- creates the database hbtn_0d_usa and the table states.
CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa` CHARACTER SET utf8mb4
       COLLATE utf8mb4_unicode_ci;
CREATE TABLE IF NOT EXISTS `hbtn_0d_usa`.`states` (
	id INT UNSIGNED NOT NULL AUTO_INCREMENT,
	name VARCHAR(256) NOT NULL,
	PRIMARY KEY (id)
);

