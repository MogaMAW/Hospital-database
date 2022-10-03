-- Active: 1654421263924@@127.0.0.1@3306@hospital_management
/*
All SQL statements for hosipital_management database.
*/
*/
CREATE TABLE patient(  
    patient_id INT NOT NULL PRIMARY KEY,
    patient_type INT,
    names VARCHAR(255),
    age INT,
    gender VARCHAR(10),
    disease VARCHAR(255),
    address_location VARCHAR(255),
    doctor_id INT

);

CREATE TABLE doctor(  
    doctor_id INT NOT NULL PRIMARY KEY,
    names VARCHAR(255),
    age INT,
    address_location VARCHAR(255),
    gender VARCHAR(10)
);


CREATE TABLE in_patient(  
    room_no VARCHAR(225) PRIMARY KEY,
    patient_id INT NOT NULL,
    date_of_admission VARCHAR(225),
    date_of_discharge VARCHAR(225),
    lab_no INT, 
    bill INT
);
DROP TABLE in_patient;

CREATE TABLE out_patient(
    patient_id INT NOT NULL,
    lab_no INT, 
    date_of_admission VARCHAR(225),
    date_of_discharge VARCHAR(225),  
    bill INT
);
DROP TABLE out_patient;

CREATE TABLE room(  
    room_no VARCHAR(225) NULL PRIMARY KEY,
    room_type INT
);
DROP TABLE room;


CREATE TABLE room_category(  
    category_no INT NOT NULL PRIMARY KEY,
    names VARCHAR(255)
);

CREATE TABLE laboratory(  
    lab_id VARCHAR(225) NOT NULL PRIMARY KEY,
    patient_id  INT, 
    doctor_id INT,
    lab_type INT
);


CREATE TABLE labs(  
    lab_no INT NOT NULL PRIMARY KEY,
    lab_name  VARCHAR(255), 
    lab_manager INT,
    amount INT
);

--implementation of foreign keys
ALTER TABLE patient ADD FOREIGN KEY (doctor_id) REFERENCES doctor(doctor_id) ON DELETE SET NULL;
ALTER TABLE out_patient ADD FOREIGN KEY (patient_id) REFERENCES patient(patient_id) ON DELETE CASCADE;
ALTER TABLE in_patient ADD FOREIGN KEY (patient_id) REFERENCES patient(patient_id) ON DELETE CASCADE;
ALTER TABLE in_patient ADD FOREIGN KEY (room_no) REFERENCES room(room_no) ON DELETE CASCADE;
ALTER TABLE room ADD FOREIGN KEY (room_type) REFERENCES room_category(category_no) ON DELETE SET NULL;
ALTER TABLE laboratory ADD FOREIGN KEY (patient_id) REFERENCES patient(patient_id) ON DELETE SET NULL;
ALTER TABLE laboratory ADD FOREIGN KEY (doctor_id) REFERENCES doctor(doctor_id) ON DELETE SET NULL;
ALTER TABLE laboratory ADD FOREIGN KEY (lab_type) REFERENCES labs(lab_no) ON DELETE SET NULL;
ALTER TABLE labs ADD FOREIGN KEY (lab_manager) REFERENCES doctor(doctor_id) ON DELETE SET NULL;

--addition of data to doctor table
INSERT INTO doctor VALUES(102,'ATURIA SARAH AKOL', 28, 'FEMALE','SOROTI');
INSERT INTO doctor VALUES(104,'AYEBARE MOSES', 38, 'MALE','MBARARA');
INSERT INTO doctor VALUES(221,'AYUPO NODREEN', 42, 'FEMALE','GULU');
INSERT INTO doctor VALUES(243,'BUGEMBE RICHARD NATHAN', 24, 'MALE','KAMPALA');
INSERT INTO doctor VALUES(256,'BUKWIRWA HENRY WILLIAM', 30, 'MALE','KITGUM');
INSERT INTO doctor VALUES(376,'BWAMBALE YOSHUA', 29, 'MALE','KAMPALA');
INSERT INTO doctor VALUES(410,'EJOKU JOSEPH', 50, 'MALE','LIRA');
INSERT INTO doctor VALUES(206,'EPIU ISABELLA', 35, 'FEMALE','HOIMA');
INSERT INTO doctor VALUES(646,'KATEREGGA GEORGE', 39, 'MALE','WAKISO');
INSERT INTO doctor VALUES(078,'IRANDUKUNDA CYNTHIA', 25, 'FEMALE','MUKONO');


--Data to labs
INSERT INTO labs VALUES(1000,'EMMERGENCY',646,2000000);
INSERT INTO labs VALUES(1001,'X-RAY',376,50000);
INSERT INTO labs VALUES(1002,'BLOOD TESTING',243,30000);
INSERT INTO labs VALUES(1003,'MATERNAL CARE',104,100000);
INSERT INTO labs VALUES(1004,'SURGERY',410,500000);
DELETE FROM labs WHERE lab_no=1005;


--Data to room_category
INSERT INTO room_category VALUES(1,'Executive');
INSERT INTO room_category VALUES(2,'Classic');
INSERT INTO room_category VALUES(3,'Ordinary');
DELETE FROM in_patient WHERE patient_id=882;

