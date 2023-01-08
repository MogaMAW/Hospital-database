import room_category
import room
import labs
import hospitaldata
import mysql.connector
import date

def doctor_ids():
    doctor_id=hospitaldata.doctors()
    return doctor_id
  
def in_patient(doctor_id,patient_id):
    mydatabase=mysql.connector.connect(host="localhost",user="root",passwd="",database="myhospital_database")  
    mycursor=mydatabase.cursor()
    category=room_category.room_category()
    rooms=room.room(category)
    lab_no= labs.lab()
    lab_id=labs.lab_id(lab_no)
    lab_numbers=labs.lab_type(lab_no)
    
    entrydate=date.entry_date()
    exitdate=date.going_date()
    
    bill=900000

    mycursor.execute("INSERT INTO room(room_no,room_type)VALUES(%s,%s)",(rooms,category))
    mycursor.execute("INSERT INTO in_patient(patient_id,room_no,date_of_admission,date_of_discharge,lab_no,bill)VALUES(%s,%s,%s,%s,%s,%s)",(patient_id,rooms,entrydate,exitdate,lab_no,bill))
    mycursor.execute("INSERT INTO laboratory(lab_id,patient_id,doctor_id,lab_type)VALUES(%s,%s,%s,%s)",(lab_id,patient_id,doctor_id,lab_numbers))
    mydatabase.commit()
    mydatabase.close()
    
def out_patient(doctor_id,patient_id):
     #patient_id=patient_type.out_patient(doctor_id)
    mydatabase=mysql.connector.connect(host="localhost",user="root",passwd="",database="myhospital_database")
    mycursor=mydatabase.cursor()
    lab_no= labs.lab()
    lab_numbers=labs.lab_type(lab_no)
    lab_id=labs.lab_id(lab_no)

    entrydate = date.entry_date()
    exitdate = date.going_date()

    bill=900000

    mycursor.execute("INSERT INTO out_patient(patient_id,lab_no,date_of_admission,date_of_discharge,bill)VALUES(%s,%s,%s,%s,%s)",(patient_id,lab_no,entrydate,exitdate,bill))
    mycursor.execute("INSERT INTO laboratory(lab_id,patient_id,doctor_id,lab_type)VALUES(%s,%s,%s,%s)",(lab_id,patient_id,doctor_id,lab_numbers))
    mydatabase.commit()
    mydatabase.close()
    


