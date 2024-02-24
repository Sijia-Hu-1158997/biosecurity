create schema biosecurity;

use biosecurity;

CREATE TABLE IF NOT EXISTS apiarist
(
apiarist_id INT auto_increment PRIMARY KEY NOT NULL,
first_name varchar(25) not null,
last_name varchar(25) not null,
address varchar(320) not null,
email varchar(320) not null,
phone varchar(11) not null,
date_joined date not null,
status tinyint default 1
);

CREATE TABLE IF NOT EXISTS staff
(
staff_number INT auto_increment PRIMARY KEY NOT NULL,
first_name varchar(25) not null,
last_name varchar(25) not null,
email varchar(320) not null,
work_phone_number varchar(11) not null,
hire_date date not null,
position varchar(25) not null,
department varchar(25) not null,
staff_status tinyint default 1
);