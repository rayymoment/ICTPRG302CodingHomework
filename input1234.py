# Copyright 2022, Rayyan Hodges, TAFE NSW
# rayyan.hodges@studytafensw.edu.au

# Obtain answer from user and determining that within our code.
number=int(input("Please enter a number ranging from 1 to 4: "))
i = number

# If answer is either 1, 2 or 3, this section prints "Good Job!" and continues asking the user to provide a number
# until the user types out a number bigger than 3 or exits the program.
if number <4:
  print("Good Job!")
loop()


# If the answer is bigger than 4, print an error stating that an invalid entry was submitted.
if i > 4:
  print("This is an invalid entry, please try again.")

# If the answer is 4, terminate the program with no message.
if i == 4:
  breakpoint()

