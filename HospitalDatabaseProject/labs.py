import random
def lab():
    print("We have these labs: \n1. EMMERGENCY LAB. \n2. X-RAY LAB. \n3. BLOOD TESTING LAB. \n4. MATERNAL CARE AND FAMILY LAB. \n5. SURGERY LAB.")
    choice=int(input("Enter the Lab you have to enter:"))
    while choice>5 or choice<1:
        choice=int(input("Enter the Lab you have to enter:"))
    return choice


def lab_id(choice):
    if choice==1:
        id='EME1'+str(random.randint(10,20))
        return id
    if choice==2:
        id='XRA2'+str(random.randint(20,30))
        return id
    if choice==3:
        id='BT3'+str(random.randint(30,40))
        return id
    if choice==4:
        id='MAC4'+str(random.randint(40,50))
        return id
    if choice==5:
        id='SUR5'+str(random.randint(50,60))
        return id

def lab_type(choice):
    if choice==1:
        return 1000
    if choice==2:
        return 1001
    if choice==3:
        return 1002
    if choice==4:
        return 1003
    if choice==5:
        return 1004