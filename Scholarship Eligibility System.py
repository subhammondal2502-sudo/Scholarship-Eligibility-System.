# Scholarship Eligibility System.........
name=(input("enter your name :"))
math_marks=int(input("marks in mathematics :"))
physics_marks=int(input("marks in physics :"))
computer_marks=int(input("marks in computer science :"))
attendance=int(input("enter your attendance upto 100 :"))
if math_marks<0 or math_marks>100 or physics_marks<0 or physics_marks>100 or computer_marks<0 or computer_marks>100 :
    print("invalid marks")
