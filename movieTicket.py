#Gathering user's age and the rating they wish to view.
age=int(input("Please enter your age: "))

rating=input("Please enter the rating of the movie you wish to view: ")

#Aged 12 or younger and 65 and over, therefore allowed discount on movie ticket.
if age<13 or age>64:
    if rating == "g" or rating == "G":
        print("You are eligible for a discounted movie ticket.")
    else: print("You are NOT eligible for a discounted movie ticket")
else:
    print("You are NOT eligible for a discounted movie ticket.")

