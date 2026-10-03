# Scholarship Eligibility System.........
name=(input("enter your name :"))
math =int(input("marks in mathematics :"))
physics =int(input("marks in physics :"))
computer =int(input("marks in computer science :"))
if math <0 or math >100 or physics <0 or physics >100 or computer <0 or computer >100 :
    print("invalid marks")
elif attendance<0 or attendance>100:
    print("invalid attendance")
else:
    if(math_marks<40 or physics_marks<40 or computer_marks<40):
        print("result : fail") 
    else:
        total_marks = (math_marks+physics_marks+computer_marks)
        print("total marks :" , total_marks)
        average=(total_marks)/3
        print("average marks :" , average) 
        if average>=80 :
            if attendance>=75:
                 print("result : excellent + scholarship eligible ")
             else:
                 print("result : excellent + scholarship not eligible")
        elif average>=60 :
            if attendance>=75:
                print("result : good + scholarship eligible ")
            else:
                print("result : good + scholarship not eligible")
        elif average>=40:
            print("result : pass")
        else:
            print("result : fail")
