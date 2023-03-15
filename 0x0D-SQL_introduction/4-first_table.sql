-- creates a table called first_table
-- in the current database in your MySQL server
-- if table first_table already exists, it will not fail.

CREATE TABLE IF NOT EXISTS first_table (
	id INT,
	name VARCHAR(256),
	PRIMARY KEY (id)
);