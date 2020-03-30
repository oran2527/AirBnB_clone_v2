-- prepares a MySQL server database hbnb_dev_db user hbnb_dev password all privileges select 
-- create a database hbnb_dev_db
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- drop user if exist avoiding confilcts
DROP USER IF EXISTS 'hbnb_dev'@'localhost';
-- flush privileges
FLUSH PRIVILEGES;
-- create user hbnb_dev in localhost and set password to hbnb_dev_pwd
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
-- flush privileges
FLUSH PRIVILEGES;
-- grant select privilege on performance_schema to hbnb_dev
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
-- grant all privileges on hbnb_dev_db to hbnb_dev
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
-- flush privileges
FLUSH PRIVILEGES;
