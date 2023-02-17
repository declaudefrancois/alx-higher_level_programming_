-- creates the database hbtn_0d_usa and the table cities.
CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa` CHARACTER SET utf8mb4
       COLLATE utf8mb4_unicode_ci;
CREATE TABLE IF NOT EXISTS `hbtn_0d_usa`.`cities` (
	id INT UNSIGNED NOT NULL AUTO_INCREMENT,
	state_id INT NOT NULL,
	name VARCHAR(256) NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(state_id) REFERENCES states(id)
)ENGINE=INNODB;

