create schema biosecurity;

use biosecurity;

CREATE TABLE IF NOT EXISTS apiarist
(
apiarist_id INT auto_increment PRIMARY KEY NOT NULL,
first_name varchar(25),
last_name varchar(25) not null,
address varchar(320) not null,
email varchar(320) not null,
phone varchar(11) not null,
date_joined varchar(8) not null
status varchar(25) not null
);

CREATE TABLE IF NOT EXISTS staff
(
staff_number INT auto_increment PRIMARY KEY NOT NULL,
first_name varchar(25),
last_name varchar(25) not null,
email varchar(320) not null,
work_phone_number varchar(11) not null,
hire_date varchar(8) not null,
position varchar(25) not null,
department varchar(25) not null,
staff_status varchar(25) not null
);

INSERT INTO apiarist (`first_name`, `last_name`, address, email, phone, 'date_joined',status) VALUES ('John', 'Smith','24 Main St, Karori, Wellington, New Zealand 5011','johnsmith@google.nz', '0211234231','04/02/2022','active');
INSERT INTO apiarist (`first_name`, `last_name`, address, email, phone, 'date_joined',status) VALUES ('Sarah', 'White','2 Tawa Rd, Burnside, Christchurch, New Zealand 4021','sarahwhite@hotmail.com.nz', '0214567231','04/02/2020','inactive');

INSERT INTO staff (`first_name`, `last_name`, email, 'work_phone_number', 'hire_date','position','department','staff_status') VALUES ('Kim', 'Wang',,'kimwang@123.com.nz', '0414567694','04/10/2009','administrator', 'admin','active');
