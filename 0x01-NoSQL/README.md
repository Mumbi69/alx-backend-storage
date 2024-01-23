# NoSQL
* NoSQL, which stands for "not only SQL," is a term used to describe a category of databases that do not use the traditional Structured Query Language (SQL) for querying and manipulating data. NoSQL databases are designed to handle large volumes of unstructured or semi-structured data and provide more flexibility and scalability than traditional relational databases.

# SQL vs. NoSQL:
* Data Model:
> * SQL: Relational databases use a structured and predefined schema.
> * NoSQL: NoSQL databases are schema-less or schema-flexible, allowing for dynamic and unstructured data.
* Scaling:
> * SQL: Vertical scaling (adding more power to an existing machine) is common.
> * NoSQL: Horizontal scaling (adding more machines to your database) is more common and easier to achieve.
* Consistency:
> * SQL: Follows the ACID properties (Atomicity, Consistency, Isolation, Durability) strictly.
> * NoSQL: May sacrifice some aspects of ACID properties for better performance and scalability.

# ACID:
* ACID is an acronym that stands for Atomicity, Consistency, Isolation, and Durability. It defines a set of properties that guarantee database transactions are processed reliably. ACID compliance is typically associated with traditional relational databases.
> * Atomicity: Ensures that a transaction is treated as a single, indivisible unit of work. Either all of its data modifications are performed, or none of them are.
> * Consistency: Guarantees that a database remains in a consistent state before and after a transaction.
> * Isolation: Ensures that concurrent execution of transactions does not lead to interference, and the results of a transaction are not visible to other transactions until it's committed.
> * Durability: Once a transaction is committed, its changes are permanent and will survive subsequent system failures.

# Document Storage:
* Document storage is a type of NoSQL database where data is stored in a document-oriented format, typically using formats like JSON or BSON (binary JSON). Each document represents a record and contains key-value pairs, providing a flexible and schema-less structure.

# NoSQL Types:
* There are several types of NoSQL databases, including:
> * Document-oriented databases: MongoDB, CouchDB.
> * Key-value stores: Redis, DynamoDB.
> * Column-family stores: Apache Cassandra, HBase.
> * Graph databases: Neo4j, Amazon Neptune.

# Benefits of NoSQL Databases:
* Scalability: NoSQL databases are often designed for horizontal scalability, making them suitable for handling large amounts of data and traffic.
* Flexibility: NoSQL databases allow for flexible and dynamic schemas, accommodating various types of data.
* Performance: NoSQL databases can provide better performance for certain types of queries and operations compared to traditional relational databases.

# Querying in NoSQL Databases:
* Querying in NoSQL databases varies depending on the type. For document-oriented databases like MongoDB, queries are typically expressed using a query language similar to JSON.

# Insert/Update/Delete in NoSQL Databases:
* The process of inserting, updating, and deleting data in NoSQL databases is usually done using specific APIs or query languages provided by the database. Each NoSQL database has its own set of commands or methods for performing these operations.

# Usage
* To use MongoDB, you need to:
> * Install MongoDB on your server or local machine.
> * Start the MongoDB server.
> * Use the MongoDB shell or a programming language driver (e.g., MongoDB Node.js driver) to interact with the database.
> * Create databases, collections, and documents.
> * Perform CRUD (Create, Read, Update, Delete) operations using the appropriate commands or methods.
