def amount(category,lab_no,days):
    
    if category==1:
        if lab_no==1:
            amount=(days*50000)+20000
            return amount
        elif lab_no==2:
            amount=(days*30000)+15000
            return amount
        elif lab_no==3:
            amount=(days*20000)+5000
            return amount
        elif lab_no==4:
            amount=(days*15000)+10000
            return amount
        elif lab_no==5:
            amount=(days*50000)+80000
            return amount
    elif category==2:
        if lab_no==1:
            amount=(days*25000)+10000
            return amount
        elif lab_no==2:
            amount=(days*25000)+10000
            return amount
        elif lab_no==3:
            amount=(days*15000)+5000
            return amount
        elif lab_no==4:
            amount=(days*10000)+9000
            return amount
        elif lab_no==5:
            amount=(days*25000)+70000
            return amount
    elif category==3:
        if lab_no==1:
            amount=(days*15000)+9000
            return amount
        elif lab_no==2:
            amount=(days*15000)+5000
            return amount
        elif lab_no==3:
            amount=(days*10000)+4500
            return amount
        elif lab_no==4:
            amount=(days*9000)+8000
            return amount
        elif lab_no==5:
            amount=(days*15000)+60000
            return amount
    
def amount1(days,lab_no):
    if lab_no==1:
        amount=days*200000
        return amount
    elif lab_no==2:
        amount=days*50000
        return amount
    elif lab_no==3:
        amount=days*10000
        return amount
    elif lab_no==4:
        amount=days*15000
        return amount
    elif lab_no==5:
        amount=days*150000
        return amount
    
        