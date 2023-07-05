
CREATE DATABASE IF NOT EXISTS banco;
CREATE USER IF NOT EXISTS tux IDENTIFIED WITH mysql_native_password BY 'Mud@r123';
GRANT ALL PRIVILEGES ON banco.* TO 'tux'@'%';

USE banco;

CREATE TABLE IF NOT EXISTS tbl_dados(
id int auto_increment primary key,
nome varchar(50) not null,
email varchar(50) not null,
senha varchar(50) not null);
