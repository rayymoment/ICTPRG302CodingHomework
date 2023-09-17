# Copyright 2022, Rayyan Hodges, TAFE NSW
# rayyan.hodges@studytafensw.edu.au

#Obtain Dog size and length of stay
dogsize=int(input("Please enter your dog's weight: "))
stay=int(input("How long will your dog will stay with us: "))

#Calculate overall cost of dog stay with information supplied
if dogsize < 3 and  stay < 11:
    daycost = 15
elif dogsize < 3 and stay > 10:
    daycost = 12
elif dogsize >= 3 and dogsize <= 10 and stay < 11:
    daycost = 20
elif dogsize >= 3 and dogsize <= 10 and stay > 10:
    daycost = 17
elif dogsize > 10 and  stay < 11:
    daycost = 25
elif dogsize >10 and stay > 10:
    daycost = 22

monthcost = daycost * stay

#Print final cost with error check for invalid information.
if dogsize==0 or stay==0:
    print("Invalid information, please enter valid information.")
else:
    print("Daily cost = $"+str(daycost))
    print("Monthly cost = $" + str(monthcost))







