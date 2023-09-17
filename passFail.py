# Copyright 2022, Rayyan Hodges, TAFE NSW
# rayyan.hodges@studytafensw.edu.au

#Obtaining course score from user and defining it
coursescore=int(input("Please enter your test score: "))

#Determining if user has passed or failed course
if coursescore <50:
    print("You have failed the course.")

if coursescore >50:
    print("You have passed the course!")

if coursescore ==50:
    print("You have passed the course!")
