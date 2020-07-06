import random

print("This is a dice stimulator")
x = "y"
bandera = True

while bandera == True:
    if x == "y":
        number = random.randint(1,6)

        if number == 1:
            print("----------")
            print("|        |")
            print("|    O   |")
            print("|        |")
            print("----------")
        if number == 2:
            print("----------")
            print("|        |")
            print("| O    O |")
            print("|        |")
            print("----------")
        if number == 3:
            print("----------")
            print("|    O   |")
            print("|    O   |")
            print("|    O   |")
            print("----------")
        if number == 4:
            print("----------")
            print("| O    O |")
            print("|        |")
            print("| O    O |")
            print("----------")
        if number == 5:
            print("----------")
            print("| O    O |")
            print("|    O   |")
            print("| O    O |")
            print("----------")
        if number == 6:
            print("----------")
            print("| O    O |")
            print("| O    O |")
            print("| O    O |")
            print("----------")
        x = input("Press y to roll again or n to close the program ")
        continue
    
    ##if  x != "y" and x != "n": 
      ##  x = input("Please, press the y button to roll the dice or n to close the program ")
        ##continue
    if  x not in ("y", "n"): 
        x = input("Please, press the y button to run the dice or n to close the program ")
        continue
        

    else: ##x == "n":
        bandera = False
        print("thanks for use the dice!!")
        
        
    
      