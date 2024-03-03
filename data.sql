-- The apiarist infor should be entered by registering. Not inserting to has the password.
INSERT INTO secureaccount (username, password, email, user_type) VALUES
('johnsmith', 'password123', 'johnsmith@google.nz','apiarist'),
('sarahwhite', 'password456', 'sarahwhite@hotmail.com.nz', 'apiarist'),
('marywang', 'password789', 'marywang@google.nz', 'apiarist'),
('loripye', 'passwordabc', 'loripye@gmail.com.nz', 'apiarist'),
('giogio', 'passwordxyz', 'giogio@giovana.com.nz', 'apiarist');

INSERT INTO apiarist (`first_name`, `last_name`, address, email, phone, `date_joined`, status) VALUES ('John', 'Smith','24 Main St, Karori, Wellington, New Zealand 5011','johnsmith@google.nz', '0211234231','2022-04-02','active');
INSERT INTO apiarist (`first_name`, `last_name`, address, email, phone, `date_joined`, status) VALUES ('Sarah', 'White','2 Tawa Rd, Burnside, Christchurch, New Zealand 4021','sarahwhite@hotmail.com.nz', '0214567231','2020-04-02','active');
INSERT INTO apiarist (`first_name`, `last_name`, address, email, phone, `date_joined`, status) VALUES ('Mary', 'Wang','3 Bevin St, NewMarket, Auckland, New Zealand 6022','marywang@google.nz', '0375234231','2023-06-07','active');
INSERT INTO apiarist (`first_name`, `last_name`, address, email, phone, `date_joined`, status) VALUES ('Lori', 'Pye','11 Bidwill St, Mt Cook, Wellington, New Zealand 5067','loripye@gmail.com.nz', '0214284631','2021-08-05','active');
INSERT INTO apiarist (`first_name`, `last_name`, address, email, phone, `date_joined`, status) VALUES ('GioGio', 'Giovana','5 Jo Place, Te Aro, Otago, New Zealand 3021','giogio@giovana.com.nz', '0743567081','2005-10-12','active');

INSERT INTO images (bee_id, image_id, image_date) VALUES
('1', '1', 'url('/static/afb.jpeg')')
('2', '2', 'url('/static/Varroa mites.jpeg')')
('3', '3', 'url('/static/Nosema.jpeg')')
('4', '4', 'url('/static/Chalkbrood Disease.jpeg')')
('5', '5', 'url('/static/Sacbrood.jpeg')')
('6', '6', 'url('/static/DWV.jpeg')')
('7', '7', 'url('/static/Black queen cell virus.jpeg')')
('8', '8', 'url('/static/Wax Moth.jpeg')')
('9', '9', 'url('/static/Vespula Wasps.jpeg')')
('10', '10', 'url('/static/PMS.jpeg')')


INSERT INTO images (bee_id, image_name, image_data) VALUES
(1, 'afb', LOAD_FILE('/app/static/Images/afb.jpeg')),
(2, 'Varroa mites', LOAD_FILE('/app/static/Images/Varroa mites.jpeg')),
(3, 'Nosema', LOAD_FILE('/app/static/Images/Nosema.jpeg')),
(4, 'Chalkbrood Disease', LOAD_FILE('/app/static/Images/Chalkbrood Disease.jpeg')),
(5, 'Sacbrood', LOAD_FILE('/app/static/Images/Sacbrood.jpeg')),
(6, 'DWV', LOAD_FILE('/app/static/Images/DWV.jpeg')),
(7, 'Black queen cell virus', LOAD_FILE('/app/static/Images/Black queen cell virus.jpeg.jpeg')),
(8, 'Wax Moth', LOAD_FILE('/app/static/Images/Wax Moth.jpeg.jpeg')),
(9, 'Vespula Wasps', LOAD_FILE('/app/static/Images/Vespula Wasps.jpeg')),
(10, 'PMS', LOAD_FILE('/app/static/Images/PMS.jpeg'));

24 Main St, Karori, Wellington, New Zealand 5011
johnsmith@google.nz
0211234231

Sarah White
2 Tawa Rd, Burnside, Christchurch, New Zealand 4021
sarahwhite@hotmail.com.nz
0214567231

-- way to update password to defalt salted abcd1234:
UPDATE secureaccount
SET password = '42e1f01ab3f6fbbf9f5984d365abd222c8d39b32626c0081918b169582531013'
WHERE userid = '1';

-- Insert data into secureaccount with default password 'abcd1234'
INSERT INTO secureaccount (username, password, email, user_type) VALUES
('rosemaryevans', '42e1f01ab3f6fbbf9f5984d365abd222c8d39b32626c0081918b169582531013', 'rosemaryevans@123.com', 'admin'),
('kimwang', '42e1f01ab3f6fbbf9f5984d365abd222c8d39b32626c0081918b169582531013', 'kimwang@123.com.nz', 'staff'),
('mythiliscott', '42e1f01ab3f6fbbf9f5984d365abd222c8d39b32626c0081918b169582531013', 'mythiliscott@hotmail.com', 'staff'),
('williambutler', '42e1f01ab3f6fbbf9f5984d365abd222c8d39b32626c0081918b169582531013', 'williamb@outlook.com', 'staff');

-- Retrieve the inserted userid values from secureaccount
SET @rosemaryevans_userid = LAST_INSERT_ID(1);
SET @kimwang_userid = LAST_INSERT_ID(2);
SET @mythiliscott_userid = LAST_INSERT_ID(3);
SET @williambutler_userid = LAST_INSERT_ID(4);

-- Insert data into staff using the retrieved userid values
INSERT INTO staff (`userid`, `first_name`, `last_name`, `staff_email`, `work_phone_number`, `hire_date`, `position`, `department`, `staff_status`) VALUES
(@rosemaryevans_userid, 'Rosemary', 'Evans', 'rosemaryevans@123.com', '0497667668', '2023-07-01', 'Administrator', 'Admin', 'active');

INSERT INTO staff (`userid`, `first_name`, `last_name`, `staff_email`, `work_phone_number`, `hire_date`, `position`, `department`, `staff_status`) VALUES
(@kimwang_userid, 'Kim', 'Wang', 'kimwang@123.com.nz', '0414567694', '2009-04-10', 'Supporter', 'Customer Service Team', 'active');

INSERT INTO staff (`userid`, `first_name`, `last_name`, `staff_email`, `work_phone_number`, `hire_date`, `position`, `department`, `staff_status`) VALUES
(@mythiliscott_userid, 'Mythili', 'Scott', 'mythiliscott@hotmail.com', '0860694769', '2021-12-30', 'Bee specialist', 'Consult Team', 'active');

INSERT INTO staff (`userid`, `first_name`, `last_name`, `staff_email`, `work_phone_number`, `hire_date`, `position`, `department`, `staff_status`) VALUES
(@williambutler_userid, 'William', 'Butler', 'williamb@outlook.com', '0473568044', '2004-08-29', 'Supporter', 'Customer Service Team', 'active');




INSERT INTO bee_pests_and_diseases (`bee_item_type`, `present_in_nz`, `common_name`, `scientific_name`) 
VALUES ('disease', 'yes','American foulbrood', 'Paenibacillus larvae');

INSERT INTO bee_infor (bee_id, `characteristics`, `biology`, `symptoms`)
VALUES (
    1,
    'Paenibacillus larvae is a rod-shaped bacterium visible only under a high power microscope. 
    Larvae up to three days old become infected by ingesting spores present in their food. 
    Young larvae less than 24 hours old are most susceptible to infection.',
    'AFB is caused when young larvae are fed spores of the bacterium, which then germinate and multiply rapidly in the tissues of the larvae, generating billions of new spores. Death then typically happens at the pupal stage. ',
    'Symptoms can include cell cappings that are sunken, perforated, darkened, or 
    greasy-looking, as well as irregular brood pattern in advanced infections. 
    Look closely, as early infections may only have one or two cells showing symptoms.'
);


INSERT INTO bee_pests_and_diseases (`bee_item_type`, `present_in_nz`, `common_name`, `scientific_name`) 
VALUES ('pest', 'yes','Varroa mites', 'Varroa destructor');

INSERT INTO bee_infor (bee_id, `characteristics`, `biology`, `symptoms`)
VALUES (
    2,
    'Varroa mites are one of the most problematic pests of honey bees
    (Apis mellifera). If not controlled, varroa can seriously undermine a
    bee by feeding on their body tissues and enhancing transmission of
    bee viruses. When left unchecked, varroa can spread throughout a
    hive very quickly, cause parasitic mite syndrome and the eventual
    death of the colony. ',
    'Varroa mites are parasitic mites, which require a honey bee host to survive and reproduce. ',
    'Female varroa mites can be seen throughout a hive both on adult
    honey bees as well as developing larvae and pupae. Female mites
    are oval shaped, reddish to dark brown in colour, and measure up to
    2 mm across. '
);

INSERT INTO bee_pests_and_diseases (`bee_item_type`, `present_in_nz`, `common_name`, `scientific_name`) 
VALUES ('disease', 'yes','Nosema', 'Nosemosis');

INSERT INTO bee_infor (bee_id, `characteristics`, `biology`, `symptoms`)
VALUES (
    3,
    'They are completely oval with a dark edge. Their contents, consisting of nucleus, sporoplasm and polar tube, cannot be seen.',
    'Nosema is a disease of honey bees caused by two species of
    microsporidian parasites (a type of spore forming fungus) called
    Nosema apis and Nosema ceranae. B',
    'Symptoms are related to digestive system disturbances. They are
    more apparent when nutrition is poor and weather conditions are
    cold and wet. Sometimes, dysentery is observed, the lifespan of
    bees are reduced and the colony dwindles in late winter or early
    spring  '
);

INSERT INTO bee_pests_and_diseases (`bee_item_type`, `present_in_nz`, `common_name`, `scientific_name`) 
VALUES ('disease', 'yes','Chalkbrood Disease', 'Ascosphaera apis');

INSERT INTO bee_infor (bee_id, `characteristics`, `biology`, `symptoms`)
VALUES (
    4,
    'It causes the chalkbrood diseases in bees, which rarely kills infected colonies but can weaken them and lead to reduced honey yields[4] and susceptibility to other pests and diseases.',
    'Chalkbrood is a disease of honey bees caused by the fungus
    Ascosphaera apis.',
    'In infected colonies some larvae are covered by white fungus. This
    gives them a “chalky” and whiter appearance than that of healthy
    larvae. The brood may appear scattered with cell caps of dead
    larvae containing small holes and slightly flattened. '
);


INSERT INTO bee_pests_and_diseases (`bee_item_type`, `present_in_nz`, `common_name`, `scientific_name`) 
VALUES ('disease', 'yes','Sacbrood', 'Sacbrood virus');

INSERT INTO bee_infor (bee_id, `characteristics`, `biology`, `symptoms`)
VALUES (
    5,
    'Sacbrood is a disease caused by the sacbrood virus. It can prevent
    honey bee larvae from turning into pupa (and eventually an adult
    bee), and the larvae die in their skin forming a sac, much like a
    water balloon. ',
    'Sacbrood virus is one of the most widespread and common honey
    bee viruses in the world, and can be detected in the most apiaries
    in New Zealand. The virus infects adult honey bees and larvae, but
    may not cause obvious symptoms in adult honey bees. Despite
    being so common, most honey bee colonies are able to tolerate low
    levels of sacbrood virus infection without suffering ill effect. ',
    'Larvae are the only honey bee stage that shows obvious symptoms
    from sacbrood virus infection. The virus is passed to larvae by
    infected adult nurse bees during feeding. Infected larvae may die
    shortly after capping, before they pupate. The larvae change from
    white, to yellow, and then brown. Larvae usually die in the cells
    with their heads facing up—the head and mouthparts usually turn
    black. '
);


INSERT INTO bee_pests_and_diseases (`bee_item_type`, `present_in_nz`, `common_name`, `scientific_name`) 
VALUES ('disease', 'yes','Deformed wing virus', ' Iflaviridae');

INSERT INTO bee_infor (bee_id, `characteristics`, `biology`, `symptoms`)
VALUES (
    6,
    'Deformed wing virus is named after one of the main symptoms it
    can cause in adult honey bees, deformities of the wings, although
    the virus can also have other effects on all life stages and castes of
    honey bees.',
    'It is one of are over 28 viruses that are known to infect
    honey bees. Deformed wing virus is one of the most widespread and
    common honey bee viruses in the world, and can be detected in
    the most apiaries in New Zealand. Work by the Ministry for Primary
    Industries has shown that New Zealand has the Deformed wing
    virus A (DWV-A) subtype.',
    'The deformed wings of adult bees are easily observed and are
    unique to this viral infection. Other symptoms caused by Deformed
    wing virus are not easily observed.'
);


INSERT INTO bee_pests_and_diseases (`bee_item_type`, `present_in_nz`, `common_name`, `scientific_name`) 
VALUES ('disease', 'yes','Black queen cell virus', 'Dicistroviridae');

INSERT INTO bee_infor (bee_id, `characteristics`, `biology`, `symptoms`)
VALUES (
    7,
    'The black queen cell virus (BQCV) is a virus that infects honey bees, specifically Apis mellifera, Apis florea, and Apis dorsata.[1] Infection of the latter two species is more recent and can be attributed to genetic similarity and geographical closeness.',
    'Black queen cell virus (BQCV) is caused by a virus in the Cripavirus genus. BQCV causes mortality in queen bee pupae, with dead queen bee larvae turning yellow and then brown-black. The disease is most common in spring and early summer.',
    'Queen bee pupae turn yellow
    and the skin of the pupae to become sac-like.
    At later stages, the dead queen bee changes to
    brown-black.'
);


INSERT INTO bee_pests_and_diseases (`bee_item_type`, `present_in_nz`, `common_name`, `scientific_name`) 
VALUES ('pest', 'yes','Wax Moth', 'Achroia grisella and Galleria mellonella ');

INSERT INTO bee_infor (bee_id, `characteristics`, `biology`, `symptoms`)
VALUES (
    8,
    'There are two species of wax moth, the Greater wax moth (Galleria mellonella) and the Lesser wax moth (Achroia grisella). Both species eat beeswax, particularly unprocessed wax, pollen, remains of larval honey bees, honey bee cocoon silk and enclosed honey bee faeces found on walls of brood cells.',
    'Both species are pests of active hives; however they will usually take advantage of already diseased or declining honey bee colonies and will therefore indicate to some other underlying problem(s) with the colony. Both Greater and Lesser wax moth will more commonly cause damage to unattended combs in storage, especially in areas that are dark, warm and poorly ventilated.',
    'Wax moth are small and grey
    (10-19 mm long). Larvae have dark heads with
    several body segments. They create white, yellow
    and/or dark brown cocoons.'
);



INSERT INTO bee_pests_and_diseases (`bee_item_type`, `present_in_nz`, `common_name`, `scientific_name`) 
VALUES ('pest', 'yes','Vespula Wasps', 'Vespula vulgaris');

INSERT INTO bee_infor (bee_id, `characteristics`, `biology`, `symptoms`)
VALUES (
    9,
    'Vespula vulgaris is a eusocial vespid that builds its tan paper nest in or on a structure capable of supporting it. A founding queen searches for a hollow tree, wall cavity, rock crevice, or even a hole made by other animals to build a nest. One colony cycle lasts for about 6–11 months and each colony cycle produces around 3,000–8,000 larvae.',
    'German and common wasps (Vespula species) are social wasps that, since being introduced into New Zealand have spread throughout the country and during the "wasp season" there numbers are so high that they are a pest of urban, rural, and natural ecosystems.',
    'German and common wasps look very similar.
    They have spread throughout most of the country and are a
    significant pest of urban, rural, and native ecosystems.'
);


INSERT INTO bee_pests_and_diseases (`bee_item_type`, `present_in_nz`, `common_name`, `scientific_name`) 
VALUES ('disease', 'yes','Parasitic Mite Syndrome (PMS)', 'Parasitic Mite Syndrome (PMS)');

INSERT INTO bee_infor (bee_id, `characteristics`, `biology`, `symptoms`)
VALUES (
    10,
    'PMS or Parasitic Mite Syndrome is a condition that causes a honey bee colony to deteriorate and eventually dwindle away and die.',
    'There has not yet been a pathogen detected which causes the brood symptoms that appear with this syndrome. However there are always varroa mites present with this syndrome.',
    'Spotty brood pattern, lack of
    adult population, high mite infestation, larvae do
    not rope, and/or larvae are slumped and possibly
    discoloured.'
);