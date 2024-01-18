-- This script creates a table users with id, email, country and name attributes
CREATE TABLE IF NOT EXISTS users (
	id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
	email VARCHAR(255) UNIQUE NOT NULL,
	name VARCHAR(255),
        country ENUM('US', 'CO', 'TN') NOT NULL DEFAULT 'US'
)
