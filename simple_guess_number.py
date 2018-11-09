import random
computer_n = random.randint(1,40)
exit_app = input("type z to exit , or enter to contuine")
user_attempt = 0
while True :
    user_attempt +=  1
    if exit_app == 'z':
        print("Goodbye the number was = ", computer_n)
        break
    user_answer = int(input("Enter your number \t "))
    if user_answer == computer_n :
        print("great , attempts = ", user_attempt)

    elif user_answer > computer_n :
        print(" higher ")
    elif user_answer < computer_n :
        print("lower")
