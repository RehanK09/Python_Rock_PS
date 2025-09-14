import random

user_score=0
comp_score=0

opt=["rock","paper","scissors"]


                                    #we can do 3 if statement but les see #something diff.

while True:
    user_input = ("Type Rock/Paper/scissors OR Q to quit: ").lower()
    if user_input == "q": 
        break                       #this throws optside from this loop
                                    #and print goodbi
    if user_input not in opt:       #this trrows back to start "Continue"
        continue

    random_no= random.randint(0,2)  #for comp to choose r(0)/p(1)/s(2)
                                    #for picking by comp
    comp_pick=opt[random_no]
    print("Computer Picked",comp_pick + ".")

    if user_input=="rock" and comp_pick=="scissors":
        print("You Won!")
        user_score +=1
                                    #weather add here coninue(for every 
                                    # if below) or use ELIF

    elif user_input=="paper" and comp_pick=="rock":
        print("You Won!")
        user_score +=1


    elif user_input=="scissors" and comp_pick=="paper":
        print("You Won!")
        user_score +=1
                                    #Easy as we now dont have to check other conditions
    else: 
        print("You Lost!")
        comp_score +=1



print("You Won Dam!",user_score,"Times")
print("Computer Won Shit!",comp_score,"Times")
print("GoodBI")