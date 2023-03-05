##THIS IS THE RUNNING FILE FOR THE PATIENTS MODULE AND PROJECT.
import mysql.connector
import hospitaldata
import hospitaldata
import room_category
import room
import labs
import hospitaldata
import mysql.connector
import date
import bills
import balance
import amount
mydatabase=mysql.connector.connect(host="localhost",user="root",passwd="",database="myhospital_database")
mycursor=mydatabase.cursor()

import patient_type
name=input("Enter your names:");name=name.upper()

age=int(input("Enter your age:"))

gender=input("Enter your gender:(M/F)");gender=gender.upper()

disease=input("Enter your disease here:");disease=disease.upper()

address=input("Enter your address here:");address=address.upper()

doctor_id=patient_type.doctor_ids()

patient_id=hospitaldata.patient()
print("Enter 1 if you are an in_patient or 2 if you are an out_patient: ")
patient_type1=int(input("Enter your entry:"))
while patient_type1>2 or patient_type1<1:
    patient_type1=int(input("Enter your entry:"))
    
mycursor.execute("INSERT INTO patient(patient_id,patient_type,names,age,gender,disease,address_location,doctor_id)VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",(patient_id,patient_type1,name,age,gender,disease,address,doctor_id))
mydatabase.commit()

if patient_type1==1:
    #patient_type.in_patient(doctor_id,patient_id)
    mydatabase=mysql.connector.connect(host="localhost",user="root",passwd="",database="myhospital_database")  
    mycursor=mydatabase.cursor()

    category=room_category.room_category()
    rooms=room.room(category)

    lab_no= labs.lab()
    lab_id=labs.lab_id(lab_no)
    lab_numbers=labs.lab_type(lab_no)

    NumberOfday=int(input("Enter the number of days you have been admitted in the hospital: "))

    entrydate=date.entry_date()
    exitdate=date.going_date(NumberOfday)
    
    payment=bills.amount(category,lab_no,NumberOfday)

    print("Your room number is:",rooms)
    print("Your total bill is:{:,}".format(payment) )
    initial_payment=int(input("Are you making any payments now? \n Enter 1 to make any payments:"))
    if initial_payment==1:
        payment_enterd=amount.amount(payment)
    else:
        payment_enterd=0
    remaining=balance.balance(payment,payment_enterd)


    mycursor.execute("INSERT INTO room(room_no,room_type)VALUES(%s,%s)",(rooms,category))
    mycursor.execute("INSERT INTO in_patient(patient_id,room_no,date_of_admission,date_of_discharge,lab_no,bill,amount,balance)VALUES(%s,%s,%s,%s,%s,%s,%s,%s)",(patient_id,rooms,entrydate,exitdate,lab_no,payment,payment_enterd,remaining))
    mycursor.execute("INSERT INTO laboratory(lab_id,patient_id,doctor_id,lab_type)VALUES(%s,%s,%s,%s)",(lab_id,patient_id,doctor_id,lab_numbers))
    mydatabase.commit()
    
elif patient_type1==2:
    #patient_type.out_patient(doctor_id,patient_id)
    mydatabase=mysql.connector.connect(host="localhost",user="root",passwd="",database="myhospital_database")
    mycursor=mydatabase.cursor()
    
    lab_no= labs.lab()
    lab_numbers=labs.lab_type(lab_no)
    lab_id=labs.lab_id(lab_no)

    number_of_days=int(input("Enter the number of days you have been told to be coming to the hospital:"))

    entrydate = date.entry_date()
    exitdate = date.going_date(number_of_days)

    payment=bills.amount1(number_of_days,lab_no)
    print("Your bill is:{:,}".format(payment) )
    initial_payment=int(input("Are you making any payments Now? \n Enter 1 to make any payments:"))
    if initial_payment==1:
        payment_enterd=amount.amount(payment)
    else:
        payment_enterd=0
    remaining=balance.balance(payment,payment_enterd)

    mycursor.execute("INSERT INTO out_patient(patient_id,lab_no,date_of_admission,date_of_discharge,bill,amount,balance)VALUES(%s,%s,%s,%s,%s,%s,%s)",(patient_id,lab_no,entrydate,exitdate,payment,payment_enterd,remaining))
    mycursor.execute("INSERT INTO laboratory(lab_id,patient_id,doctor_id,lab_type)VALUES(%s,%s,%s,%s)",(lab_id,patient_id,doctor_id,lab_numbers))
    mydatabase.commit()
    
mydatabase.close()

