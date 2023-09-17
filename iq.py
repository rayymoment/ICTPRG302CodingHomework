# Copyright 2022, Rayyan Hodges, TAFE NSW
# rayyan.hodges@studytafensw.edu.au

#ISSUE: INVALID IQ AND BELOW AVERAGE TRIGGER WHEN INVALID ANSWER GIVEN

#Obtaining and defining IQ
iq=int(input("Please enter your IQ: "))
answer=iq

#Invalid IQ Error
if answer<0 or answer>200:
    print("Error: Invalid IQ")


#Below Average IQ
if answer<100 and answer>-1:
    print("You have below average IQ.")

#Average IQ
if answer==100:
    print("You have average IQ.")

#Above IQ Average
if answer>100 and answer<201:
    print("You have above average IQ.")
