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

INSERT INTO apiarist (`first_name`, `last_name`, address, email, phone, `date_joined`, status) VALUES (`Tom`, `Smith`,`24 Main St, Karori, Wellington, New Zealand 5011`,`johnsmith@google.nz`, `0211234231`,`04/02/2022`,`1`);
INSERT INTO apiarist (`first_name`, `last_name`, address, email, phone, `date_joined`, status) VALUES (`Sarah`, `White`,`2 Tawa Rd, Burnside, Christchurch, New Zealand 4021`,`sarahwhite@hotmail.com.nz`, `0214567231`,`04/02/2020`,`1`);
INSERT INTO apiarist (`first_name`, `last_name`, address, email, phone, `date_joined`, status) VALUES (`Mary`, `Wang`,`3 Bevin St, NewMarket, Auckland, New Zealand 6022`,`marywang@google.nz`, `0375234231`,`06/07/2023`,`1`);
INSERT INTO apiarist (`first_name`, `last_name`, address, email, phone, `date_joined`, status) VALUES (`Lori`, `Pye`,`11 Bidwill St, Mt Cook, Wellington, New Zealand 5067`,`loripye@gmail.com.nz`, `0214284631`,`08/05/2021`,`1`);
INSERT INTO apiarist (`first_name`, `last_name`, address, email, phone, `date_joined`, status) VALUES (`GioGio`, `Giovana`,`5 Jo Place, Te Aro, Otago, New Zealand 3021`,`giogio@giovana.com.nz`, `0743567081`,`10/12/2005`,`1`);

INSERT INTO staff (`first_name`, `last_name`, email, `work_phone_number`, `hire_date`,`position`,`department`,`staff_status`) VALUES (`Rosemary`, `Evans`,`rosemaryevans@123.com`, `0497667668`,`07/01/2023`,`supporter`, `support team`,`1`);

INSERT INTO staff (`first_name`, `last_name`, email, `work_phone_number`, `hire_date`,`position`,`department`,`staff_status`) VALUES (`Kim`, `Wang`,`kimwang@123.com.nz`, `0414567694`,`04/10/2009`,`administrator`, `admin`,`1`);
