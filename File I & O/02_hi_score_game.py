import random

def game():
    print("You are playing a number game.")
    score = random.randint(1, 10)
    print(f"The number is {score}")
    with open("hiScore.txt") as f:
        hi_score = f.read()
        if(hi_score != " "):
            hi_score = int(hi_score)
        else:
            hi_score = 0
    
    if (score > hi_score):
        print("You got a high score!")
        with open("hiScore.txt", "w") as f:
            f.write(str(score))
    return score


game()