import random
computer = random.choice([1,2,3])
youstr = input("Enter your choice: ")
youDict = {"r":1,"p":2,"s":3}
reverseDict = {1:"Rock", 2:"Paper" , 3:"Scissors"}
you = youDict[youstr]

print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")

if(computer == you):
    print("Its a draw")
else:
    if(computer == 1 and you ==2):
        print("You win")
    elif(computer == 1 and you == 3):
        print("Computer wins")
    elif(computer == 2 and you ==1):
        print("Computer wins")
    elif(computer == 2 and you ==3):
        print("You win")
    elif(computer == 3 and you ==1):
        print("You win")
    elif(computer == 3 and you ==2):
        print("Computer wins")
    else:
        print("Somethimg went wrong!")