import random

attempts = 1
max_attempts = 3

while(attempts <= max_attempts):
    secret_number = random.randint(1,100)

    score = 0
    pick = input("Guess your random number: ")
    print("Total attempts: ", attempts)
    print(f'Random number was: {secret_number}')
    if(pick == secret_number):
        score+=1
        print(f'Your guess was right!! {secret_number} and you score is: {score}')
    attempts+=1

