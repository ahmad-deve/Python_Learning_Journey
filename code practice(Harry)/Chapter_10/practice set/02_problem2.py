import random

def game():
    print("You are playing the game.." )
    score = random.randint(1,62)
# Fetch the hiscore
    

with open ("hisscore.txt") as f:
    hisscore = f.read()
    if(hisscore == ""):
        hisscore = int(hisscore)

    print(f"Your score: {score}")
    if (score>hisscore or hisscore == ""):
    
    return score

game()

