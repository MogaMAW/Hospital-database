
def room_category():
    print("We have these room categories: \n1. Executive rooms\n 2. Classic rooms \n3. Ordinary rooms")

    choice=int(input("Enter your room category choice from 1 to 3:"))
    while choice>3 or choice<1:
        choice=int(input("Enter your room category choice from 1 to 3:"))
    
    return choice