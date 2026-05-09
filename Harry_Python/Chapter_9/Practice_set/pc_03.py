import random

def game():
    print("You are playing the game..")
    score = random.radint(1, 62)

    #fetch the high score
    with open("hiscore.txt") as f:
        hiscore = f.read()

        if(hiscore == ""):
            hiscore = int(hiscore)

        else:
            hiscore = 0

    print(f"The high score is {hiscore}")

    if(score>hiscore):
        # write this hiscore to the file\
        with open("hiscore.txt", 'w') as f:
            f.write(str(score))

    return score
game()