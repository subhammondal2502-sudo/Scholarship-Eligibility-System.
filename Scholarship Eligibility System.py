# Scholarship Eligibility System.........
name=(input("enter your name :"))
percentage = int(input("enter your percentage : "))
income = int(input("enter Family Annual Income : "))
category = input("enter your category (general / obc / sc / st) :")
if percentage < 60 or income > 300000:
    print("not eligible ")
else:
    if category== "general":
         if percentage>=75:
             print("eligible for scholarship")
         else:
             print("not eligible for scholarship")    
    elif category== "obc":
        if percentage>=70:
            print("eligible for scholarship")
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
