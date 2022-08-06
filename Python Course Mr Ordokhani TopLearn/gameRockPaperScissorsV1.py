# programm name: rock paper scissors game.
# programmer: Mohammad Saleh Rostami.(Saleh13611397@gmail.com)
# programming language: python 3.9.2

# import essential modules
import random , os


os.system("cls") # used for clear terminal

totalChoice={0:"rock",1:"paper",2:"scissors"} # define a dictionary for match number to choice

computerRandomChoice = random.randint(0,2) 

print("Welcom to Rock_Paper_Scissors Game\n--------\n0-->rock \n1-->paper  \n2-->scissors\n\n\nTO EXIT ENTER 1000\n----------------------")

while True:
    userChoice= int(input("please enter your choice: "))

    if userChoice==1000:
        exit()
        
    if userChoice>=0 and userChoice<=2:
        if (computerRandomChoice==userChoice):
            print("You have equal choice\n\n\n")
        elif (computerRandomChoice != userChoice):
            if (computerRandomChoice==0 and userChoice==1):
                print(f"Computer Win :computer choice is {totalChoice[computerRandomChoice]} and your choice is {totalChoice[userChoice]}\n\n\n")
            elif (computerRandomChoice==0 and userChoice==2):
                print(f"Computer Win :computer choice is {totalChoice[computerRandomChoice]} and your choice is {totalChoice[userChoice]}\n\n\n")
            elif (computerRandomChoice==1 and userChoice==0):
                print(f"user Win :computer choice is {totalChoice[computerRandomChoice]} and your choice is {totalChoice[userChoice]}\n\n\n")
            elif (computerRandomChoice==1 and userChoice==2):
                print(f"user Win :computer choice is {totalChoice[computerRandomChoice]} and your choice is {totalChoice[userChoice]}\n\n\n")
            elif (computerRandomChoice==2 and userChoice==0):
                print(f"Computer Win :computer choice is {totalChoice[computerRandomChoice]} and your choice is {totalChoice[userChoice]}\n\n\n")
            elif (computerRandomChoice==2 and userChoice==1):
                print(f"Computer Win :computer choice is {totalChoice[computerRandomChoice]} and your choice is {totalChoice[userChoice]}\n\n\n")
    else:
        # comment: 
        print("Your choice is not valid\nPlease enter valid number.\n\n\n")

