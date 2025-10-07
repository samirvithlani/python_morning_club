season = input("enter season :")


match season:
    case "monsoon" | "MONSOON" | "m":
        print("buy umbrella !!")
    case "summer":
        print("buy ac :")       
    case "winter":
        print("winter is coming..")
    case _:
        print("invalid season...")        

#_ ->default..        