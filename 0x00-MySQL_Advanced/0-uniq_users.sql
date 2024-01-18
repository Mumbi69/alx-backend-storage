-- This script creates a table users with id, email and name attributes
CREATE TABLE IF NOT EXISTS users (
	id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
	email VARCHAR(225) UNIQUE NOT NULL,
	name VARCHAR(225)
)
