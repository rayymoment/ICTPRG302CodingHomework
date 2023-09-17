#Obtain bank and savings balance from user
checkingbal=int(input("Please enter your checking balance: "))
savingsbal=int(input("Please enter your savings balance: "))

#Checking if users checking balance is low
if checkingbal <50:
    print("Checking account balance is low")

#Checking if users savings balance is low
if savingsbal <100:
    print("Savings account balance is low")


