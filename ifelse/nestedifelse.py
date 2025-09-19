age = int(input("enter age :"))

if age>18:
    print("you are eligible for voating....")
    if age>21:
        print("you are eligible for marrige....")
    else:
        print("you are not eligible for marrige....")
else:    
    print("you are not eligible for voating....")
    
    if age>16:
        print("you are eligible for learning lic......")
    else:
        print("you are not eligible for learing lic....")