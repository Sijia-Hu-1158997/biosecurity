INSERT INTO apiarist (`first_name`, `last_name`, address, email, phone, `date_joined`, status) VALUES ('Tom', 'Smith','24 Main St, Karori, Wellington, New Zealand 5011','johnsmith@google.nz', '0211234231','2022-04-02','active');
INSERT INTO apiarist (`first_name`, `last_name`, address, email, phone, `date_joined`, status) VALUES ('Sarah', 'White','2 Tawa Rd, Burnside, Christchurch, New Zealand 4021','sarahwhite@hotmail.com.nz', '0214567231','2020-04-02','active');
INSERT INTO apiarist (`first_name`, `last_name`, address, email, phone, `date_joined`, status) VALUES ('Mary', 'Wang','3 Bevin St, NewMarket, Auckland, New Zealand 6022','marywang@google.nz', '0375234231','2023-06-07','active');
INSERT INTO apiarist (`first_name`, `last_name`, address, email, phone, `date_joined`, status) VALUES ('Lori', 'Pye','11 Bidwill St, Mt Cook, Wellington, New Zealand 5067','loripye@gmail.com.nz', '0214284631','2021-08-05','active');
INSERT INTO apiarist (`first_name`, `last_name`, address, email, phone, `date_joined`, status) VALUES ('GioGio', 'Giovana','5 Jo Place, Te Aro, Otago, New Zealand 3021','giogio@giovana.com.nz', '0743567081','2005-10-12','active');
INSERT INTO staff (`first_name`, `last_name`, email, `work_phone_number`, `hire_date`,`position`,`department`,`staff_status`) VALUES ('Rosemary', 'Evans','rosemaryevans@123.com', '0497667668','2023-07-01','Administrator', 'Admin','active');
INSERT INTO staff (`first_name`, `last_name`, email, `work_phone_number`, `hire_date`,`position`,`department`,`staff_status`) VALUES ('Kim', 'Wang','kimwang@123.com.nz', '0414567694','2009-04-10','Supporter', 'Customer Service Team','active');
INSERT INTO staff (`first_name`, `last_name`, email, `work_phone_number`, `hire_date`,`position`,`department`,`staff_status`) VALUES ('Mythili', 'Scott','mythiliscott@hotmail.com', '0860694769','2021-12-30','Bee specialist', 'Consult Team','active');
INSERT INTO staff (`first_name`, `last_name`, email, `work_phone_number`, `hire_date`,`position`,`department`,`staff_status`) VALUES ('William', 'Butler','williamb@outlook.com', '0473568044','2004-08-29','Supporter', 'Customer Service Team','active');

INSERT INTO bee_pests_and_diseases (`bee_item_type`, `present_in_nz`, `common_name`, `scientific_name`) 
VALUES ('disease', 'yes','American foulbrood', 'Paenibacillus larvae');

INSERT INTO bee_infor (bee_id, `characteristics`, `biology`, `symptoms`, `images`)
VALUES (
    1,
    'Paenibacillus larvae is a rod-shaped bacterium visible only under a high power microscope. 
    Larvae up to three days old become infected by ingesting spores present in their food. 
    Young larvae less than 24 hours old are most susceptible to infection.',
    'American foulbrood (AFB) is a fatal bacterial disease of honey bee brood caused by 
    the spore forming bacterium Paenibacillus larvae.',
    'Symptoms can include cell cappings that are sunken, perforated, darkened, or 
    greasy-looking, as well as irregular brood pattern in advanced infections. 
    Look closely, as early infections may only have one or two cells showing symptoms.',
    LOAD_FILE('iCloud Drive/Documents/GitHub/biosecurity/images/AFB.png')
);


INSERT INTO bee_pests_and_diseases (`bee_item_type`, `present_in_nz`, `common_name`, `scientific_name`) 
VALUES ('disease', 'yes','American foulbrood', 'Paenibacillus larvae');

INSERT INTO bee_infor (bee_id, `characteristics`, `biology`, `symptoms`, `images`)
VALUES (
    2,
    'Paenibacillus larvae is a rod-shaped bacterium visible only under a high power microscope. 
    Larvae up to three days old become infected by ingesting spores present in their food. 
    Young larvae less than 24 hours old are most susceptible to infection.',
    'American foulbrood (AFB) is a fatal bacterial disease of honey bee brood caused by 
    the spore forming bacterium Paenibacillus larvae.',
    'Symptoms can include cell cappings that are sunken, perforated, darkened, or 
    greasy-looking, as well as irregular brood pattern in advanced infections. 
    Look closely, as early infections may only have one or two cells showing symptoms.',
    LOAD_FILE('iCloud Drive/Documents/GitHub/biosecurity/images/AFB.png')
);
