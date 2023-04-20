-- creates a table called first_table
-- in the current database in your MySQL server
-- if table first_table already exists, it will not fail.

-- if u want to add a primary key constraint to the table, use:
-- ALTER TABLE first_table ADD PRIMARY KEY (id);

-- if u want to remove a primary key constraint from the table, use:
-- ALTER TABLE first_table DROP PRIMARY KEY;

CREATE TABLE IF NOT EXISTS first_table (
	id INT,
	name VARCHAR(256)
);
