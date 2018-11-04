import random


greater_list = []
lower_list = []
all_numbers = []
# random number from 0 to 10
def get_numbers():
    return random.randint(1,40)


def play_with_number():
    print(" Guess a number from 1 to 20")
    computer_number = get_numbers()
    user_try = 0
    exit_app = input(" type exit to exit OR type enter to contuine .\n ")
    while True :
        if exit_app == 'exit':
            print(" the number was ", computer_number)
            break
        user_try += 1
        user = int(input("Enter you number\t "))
        if user == computer_number  :
            print("Great , you got it after {}".format(user_try) + " times , Goodbye ")
            break
        else :
            if user >= computer_number :
                greater_list.append(user)
                print(" Your guess is too high ")
            elif user <= computer_number :
                lower_list.append(user)
                print(" Your guess is too low ")
    if exit_app != 'exit':
        multiply_list()



def multiply_list():
    print("Higher number is = ",greater_list)
    for i in greater_list:
        for x in lower_list:
            result = i * x
            if result not in all_numbers:
                all_numbers.append(result)
    print("Lower number is = ",lower_list)
    print("Multiply this two list is = ",all_numbers)


play_with_number()
