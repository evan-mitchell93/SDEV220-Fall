from package_1.sub_package import ran

"""
Importing from sub directory not working ****

"""

def run_game():
    secret = ran.get_random()
    print(secret)
    guesses = 0

    while guesses < 3:
        user_guess = int(input("Enter a guess: "))
        if user_guess == secret:
            print("Correct")
            break
        else:
            print("Try again")
            guesses += 1

        