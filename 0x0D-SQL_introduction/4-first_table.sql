-- creates a table called first_table in the current database
CREATE TABLE IF NOT EXISTS first_table (
	id INT UNSIGNED NOT NULL,
	name VARCHAR(256)
)
ENGINE=INNODB;
