# Copyright 2022, Rayyan Hodges, TAFE NSW
# rayyan.hodges@studytafensw.edu.au

#Getting user to choose type of wood
woodtype=int(input("Please select the type of wood you would like to use (1 for pine, 2 for oak): "))

#Defining answer
answer=woodtype

#Determining answer
if woodtype <2:
    print("You have selected pine wood The pine table will cost you $100.")

if woodtype >1:
    print("You have selected oak wood. The oak table will cost you $285.")
