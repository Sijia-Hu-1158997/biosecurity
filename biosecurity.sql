create schema biosecurity;

use biosecurity;

CREATE TABLE IF NOT EXISTS apiarist
(
apiarist_id INT auto_increment PRIMARY KEY NOT NULL,
first_name varchar(25) not null,
last_name varchar(25) not null,
address varchar(320) not null,
email varchar(320) not null,
phone varchar(15) not null,
date_joined date not null,
status ENUM('active', 'inactive') NOT NULL EFAULT 'active'
);

CREATE TABLE IF NOT EXISTS staff
(
staff_number INT auto_increment PRIMARY KEY NOT NULL,
first_name varchar(25) not null,
last_name varchar(25) not null,
email varchar(320) not null,
work_phone_number varchar(15) not null,
hire_date date not null,
position varchar(25) not null,
department varchar(25) not null,
staff_status ENUM('active', 'inactive') NOT NULL EFAULT 'active'
);


CREATE TABLE IF NOT EXISTS bee_pests_and_diseases
(
bee_id INT auto_increment PRIMARY KEY NOT NULL,
bee_item_type ENUM('pest', 'disease') NOT NULL,
present_in_nz ENUM('yes', 'no') NOT NULL,
common_name varchar(50) not null,
scientific_name varchar(50) not null
);


CREATE TABLE IF NOT EXISTS bee_infor
(
bee_id INT NOT NULL,
characteristics varchar not null,
biology varchar not null,
symptoms varchar not null,
images BLOB not null,
FOREIGN KEY (bee_id) REFERENCES bee_pests_and_diseases(bee_id)
ON UPDATE CASCADE
);


CREATE TABLE IF NOT EXISTS`secureaccount` 
(
`userid` int NOT NULL AUTO_INCREMENT,
`username` varchar(100) NOT NULL,
`password` varchar(255) NOT NULL,
`email` varchar(100) DEFAULT NULL,
PRIMARY KEY (`userid`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

