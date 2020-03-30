-- prepares a MySQL server database hbnb_test_db user hbnb_test password all privileges select 
-- create a database hbnb_test_db
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- drop user if exist avoiding confilcts
DROP USER IF EXISTS 'hbnb_test'@'localhost';
-- flush privileges
FLUSH PRIVILEGES;
-- create user hbnb_test in localhost and set password to hbnb_test_pwd
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
-- flush privileges
FLUSH PRIVILEGES;
-- grant select privilege on performance_schema to hbnb_test
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
-- grant all privileges on hbnb_dev_db to hbnb_test
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
-- flush privileges
FLUSH PRIVILEGES;
