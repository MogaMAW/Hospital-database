import random

def room(choice):
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
    
