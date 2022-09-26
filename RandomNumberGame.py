import random

while True:
    computernum = random.randrange(1,101)
    usernum = int(input("Enter your numner : "))
     
    if usernum>computernum:
        print("Computer Number is : ", computernum)
        print("The guss number is too high !")

    elif usernum<computernum:
        print("Computer Number is : ", computernum)
        print("The guss number is too low !")
    else:
        print("Computer Number is : ", computernum)
        print("The guss number is equal. Congratulations !")
        break;

