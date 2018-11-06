import random


greater_list = [] # empty list to save the greater numbers
lower_list = [] # empty list to save the lowest numbers
all_numbers = [] # result of Multiply lists .
# random number from 0 to 40
def get_numbers():
    return random.randint(1,40) # return new random number when called .

# start play with computer.
def play_with_number():
    print(" Guess a number from 1 to 40")
    computer_number = get_numbers()
    user_try = 0 # to calcuate the user try .
    exit_app = input(" type exit to exit OR type enter to contuine .\n ")
    while True : # keep looping until user find the correct number
        if exit_app == 'exit':
            print(" the number was ", computer_number)
            break
        user_try += 1 # increase this value in each roll to calcuate the user try.
        try: # create try and catch , if user type text
            user_answer = int(input("Enter your number\t "))
            if user_answer == computer_number :
                print("Great , you got it after {}".format(user_try) + " times , Goodbye ")
                break
            elif user_answer > computer_number :
                print("Your guess is to high")
                greater_list.append(user_answer)
            elif user_answer < computer_number :
                print(" Your guess is to lower")
                lower_list.append(user_answer)
        except ValueError: # raise this mes when user insert string .
            print(" accept number , just number pls")
    if exit_app != 'exit': # check the script is running before call multiply_list function .
        multiply_list()


# Multiply two list .
def multiply_list():
    print("Higher number is = ",greater_list)
    for i in greater_list:
        for x in lower_list:
            result = i * x
            if result not in all_numbers: # don't duplicate numbers
                all_numbers.append(result)
    print("Lower number is = ",lower_list)
    print("Multiply this two list is = ",all_numbers)

# code start from here .
play_with_number()
