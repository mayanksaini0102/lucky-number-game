import random 
number = random.randint(1,10)
for i in range(3):
    guess = int(input("guess a number (1-10): "))
    if guess == number:
        print("you win!")
        break
    else:
        print("try again")
        if guess != number:
            print("game over!")
            print("correct number:", number)  
