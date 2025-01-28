import random
from helpers.timer_class import Timer

def random_add_problem(max_number):
    num1 = random.randint(1, max_number)
    num2 = random.randint(1, max_number)
    add_problem_text = (f"\n{num1} + {num2} = ?")
    add_answer = num1 + num2
    return add_problem_text, add_answer

def random_sub_problem(max_number):
    num1 = random.randint(1, max_number)
    num2 = random.randint(1, max_number)
    sub_problem_text = (f"\n{num1} - {num2} = ?")
    sub_answer = num1 - num2
    return sub_problem_text, sub_answer

def random_multi_problem(max_number):
    num1 = random.randint(1, max_number)
    num2 = random.randint(1, max_number)
    multi_problem_text = (f"\n{num1} x {num2} = ?")
    multi_answer = num1 * num2
    return multi_problem_text, multi_answer

def random_div_problem(max_number):
    num2 = random.randint(1, max_number)
    num1 = num2 * (random.randint(1, max_number))
    div_problem_text = (f"\n{num1} / {num2} = ?")
    div_answer = num1 / num2
    return div_problem_text, div_answer

def start_game():
    while True:
        selected_operation = input("\nPlease enter an operation [+, -, x, /] or 'q' to quit: ")
        
        if selected_operation.lower() == 'q':
            print('Thanks for playing!')
            break
        
        # Validate operation
        while selected_operation not in ["+", "-", "x", "/"]:
            selected_operation = input("That is not a correct operation. Please try again [+, -, x, /]: ")
            if selected_operation.lower() == 'q':  # Allow quitting during validation
                print('Thanks for playing!')
                return

        while True:
            max_number = input("Please enter a max number between 1 and 100 or 'q' to quit: ")
            
            if max_number.lower() == 'q':  # Allow quitting during validation
                print('Thanks for playing!')
                return

            # Validate if max_number is a valid integer within the range
            try:
                max_number = int(max_number)
                if 1 <= max_number <= 100:  # Check if it's within range
                    break  # Valid input, exit the loop
                else:
                    print("\nThat is not correct.")
            except ValueError:
                print("\nInvalid input.")
    
        # Start the timer
        game_timer = Timer(30)
        game_timer.start()

        # Generate problem once before the loop
        add_problem_text, add_answer = random_add_problem(max_number)
        sub_problem_text, sub_answer = random_sub_problem(max_number)
        multi_problem_text, multi_answer = random_multi_problem(max_number)
        div_problem_text, div_answer = random_div_problem(max_number)

        score = 0

        # Handle guesses while the timer is running
        while game_timer.has_time_left():
            remaining_time = game_timer.get_time_left()

            if selected_operation == "+":
                print(add_problem_text)
                print(f"You have {remaining_time} seconds left.")
                user_guess = input('Enter an answer: ')

                try:
                    user_guess = int(user_guess)  # Convert input to integer
                except ValueError:
                    print("\nInvalid input. Please enter a valid number.")
                    continue

                if user_guess == add_answer:
                    score += 1
                    print(f"\n{user_guess} is correct!")
                    add_problem_text, add_answer = random_add_problem(max_number)
                else:
                    print(f"\n{user_guess} is not correct. Try again!")

            elif selected_operation == "-":
                print(sub_problem_text)
                print(f"You have {remaining_time} seconds left.")
                user_guess = input('Enter an answer: ')

                try:
                    user_guess = int(user_guess)  # Convert input to integer
                except ValueError:
                    print("\nInvalid input. Please enter a valid number.")
                    continue

                if user_guess == sub_answer:
                    score += 1
                    print(f"\n{user_guess} is correct!")
                    sub_problem_text, sub_answer = random_sub_problem(max_number)
                else:
                    print(f"\n{user_guess} is not correct. Try again!")

            elif selected_operation == "x":
                print(multi_problem_text)
                print(f"You have {remaining_time} seconds left.")
                user_guess = input('Enter an answer: ')

                try:
                    user_guess = int(user_guess)  # Convert input to integer
                except ValueError:
                    print("\nInvalid input. Please enter a valid number.")
                    continue

                if user_guess == multi_answer:
                    score += 1
                    print(f"\n{user_guess} is correct!")
                    multi_problem_text, multi_answer = random_multi_problem(max_number)
                else:
                    print(f"\n{user_guess} is not correct. Try again!")

            else:
                print(div_problem_text)
                print(f"You have {remaining_time} seconds left.")
                user_guess = input('Enter an answer: ')

                try:
                    user_guess = int(user_guess)  # Convert input to integer
                except ValueError:
                    print("\nInvalid input. Please enter a valid number.")
                    continue

                if user_guess == div_answer:
                    score += 1
                    print(f"\n{user_guess} is correct!")
                    div_problem_text, div_answer = random_div_problem(max_number)
                else:
                    print(f"\n{user_guess} is not correct. Try again!")

        # After timer runs out
        while True:
            user_input = input()

            if user_input.lower() == 'q':  # Quit
                print('Thanks for playing!')
                return
            elif user_input == '':  # Restart the game
                print("\nStarting a new game...")
                break
            else:  # Any other input (non-empty)
                print(
                    "\nTime is up!\nSorry, you didn't get that answer in on time.\n"
                    f"You answered {score} problems!\n"
                    "Press Enter to play again or 'q' to quit."
                )

if __name__ == "__main__":
    start_game()