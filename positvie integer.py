#Manav Shardha

while True:
    while True:
        try:
            x = int(input("Please enter an integer: "))
            break
        except ValueError:
            print("Error, the number you have entered is not an integer")
            
    if (x%11 == 0) and (x%12 == 0) and (x>0):
        print("win")
        break

    else:
        pass
        
