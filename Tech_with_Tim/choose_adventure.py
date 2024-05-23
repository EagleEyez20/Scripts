name = input("Type your name: ")
print("Welcome", name,"to this adventure!")

answer = input("You are in a dark room with two doors. Do you go through door #1 or door #2? ").lower()

if answer == "door #1":
    answer = input("There's a giant bear here eating a cheese cake. What do you do? 1. Take the cake " or "2. scream at the bear? Type 1 or 2: ").lower
    
    if answer == "1":
        print("The bear eats you instead. Good job! Game over.")
        break
    elif answer == "2":
        print("The bear tells you that you have bad breath. Do you 1. smack the bear or 2. run away? Type 1 or 2: ").lower()
        
        if answer == "1":
            print("The bear eats you instead. Good job! Game over.")
            break
        elif answer == "2":
            print("You run directly into a pot of gold! You WIN! Thank you for playing!"
            break        
                       
    else:
    print("Not a valid option. Fatality!!")
        
    
elif answer == "door #-1":
    print()
else:
    print("Not a valid option Dumbass! You lose.")




