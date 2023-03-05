import random

def room(choice):
    ##these are the different categories of rooms E for Executive, O for Ordinary and C for Classic 
    if choice ==1:
        room=random.randint(2000,5000)
        room_no="E"+str(room)
        return (room_no)

    if choice ==2:
        room=random.randint(2000,5000)
        room_no="C"+str(room)
        return (room_no)
        
    if choice ==3:
        room=random.randint(2000,5000)
        room_no="O"+str(room)
        return (room_no)
    
