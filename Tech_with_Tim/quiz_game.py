print("Welcome to my computer quiz!")

playing = input("Are you ready to play? yes/no? ")

#text for git response
if playing != "yes":
    quit()
    
print("Ok, Let's play")
score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
    
else:
    print("Incorrect")
    
answer = input("What does GPU stand for? ")
if answer.lower() == "graphical processing unit":
    print("Correct!")
    score += 1
    
else:
    print("Incorrect")
    
answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
    
else:
    print("Incorrect")
    

print("You got " + str(score) + " questions correct!")
