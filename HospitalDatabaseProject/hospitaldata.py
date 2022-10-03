import random
def doctors():
    doctor_list=[110,102,109,148,121,130,200,240,260,395,381,309,318,394,399,181,192,222,286,187]
    doctor=random.choice(doctor_list)
    return doctor


def patient():
    patient_id=random.randint(700,1800)
    return patient_id
