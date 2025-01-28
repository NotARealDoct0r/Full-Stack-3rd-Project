from helpers.anagrams import get_random_word_and_count
from helpers.timer_class import Timer

def start_game():
    while True:
        word_length = input("\nPlease enter a word length [5, 6, 7, 8] or 'q' to quit: ")
        
        if word_length.lower() == 'q':
            print('Thanks for playing!')
            break

        # Validate word length
        while not (word_length.isdigit() and int(word_length) in [5, 6, 7, 8]):
            word_length = input('That is not a correct word length. Please try again [5, 6, 7, 8]: ')
            if word_length.lower() == 'q':  # Allow quitting during validation
                print('Thanks for playing!')
                return
        
        # If word length is valid, get word length lists, selected list, random word, and remaining words count
        word_length_lists, selected_list, random_word, remaining_words_count = get_random_word_and_count(word_length)

        score = 0
        correct_answers = []
        used_lists = []
        words_to_guess = selected_list[:] 
        lists_to_guess = word_length_lists[:]

        # Start the timer
        game_timer = Timer()
        game_timer.start()

        # Handle guesses while the timer is running
        while game_timer.has_time_left():
            remaining_time = game_timer.get_time_left()
            print(f"\nThe word is: {random_word.upper()}")
            print(f'There are {remaining_words_count} unguessed anagrams.')
            print(f"You have {remaining_time} seconds left.")
            user_guess = input('Make a guess: ')

            # Check if the guess has already been guessed
            if user_guess in correct_answers:
                print(f"\nYou already got {user_guess.upper()}. Try again.")
                continue # Skip to the next iteration

            # Check if the guess is valid
            if user_guess not in words_to_guess or user_guess == random_word:
                print(f"\n{user_guess.upper()} is not a valid anagram. Please try again.")
            elif user_guess in words_to_guess and user_guess != random_word:
                score += 1
                correct_answers.append(user_guess) 
                words_to_guess.remove(user_guess)
                remaining_words_count = len(words_to_guess) - 1 
                print(f"\n{user_guess.upper()} is correct!")
            
            # Check if there are no words left
            if remaining_words_count == 0 and selected_list not in used_lists:
                print(f"You got all the anagrams for {random_word.upper()}!")
                
                # Mark the current list as used
                used_lists.append(selected_list)
                lists_to_guess.remove(selected_list)

                # Check if there are more lists to guess from
                if lists_to_guess:
                    # Generate new random word from the next list
                    selected_list, random_word, remaining_words_count = get_random_word_and_count(word_length, lists_to_guess)[1:]
                    words_to_guess = selected_list[:]
                else: 
                    # Game ends when all words guessed
                    print(
                        "\nYou got all the anagrams!"
                        f"\nYou got {score} anagrams for {word_length}-letter words!"
                        "\nPress Enter to play again or 'q' to quit."
                    )

                    user_input = input()
                    
                    if user_input.lower() == 'q':
                        print('Thanks for playing!')
                        return
                    elif user_input == '':
                        print("Starting a new game...")
                        break

        # After timer runs out
        while True:
            user_input = input()

            if user_input.lower() == 'time':
                print(
                    f"\nTime is up!\nYou got {score} anagrams for {word_length}-letter words!\n"
                    "Press Enter to play again or 'q' to quit."
                )
                break  # Exit the loop after showing the "time" message
            elif user_input != '':
                print(
                    "\nTime is up!\nSorry, you didn't get that last one in on time.\n"
                    f"You got {score} anagrams for {word_length}-letter words!\n"
                    "Press Enter to play again or 'q' to quit."
                )
                break  # Exit after showing the timeout message

            # Replay or quit
            if user_input.lower() == 'q':
                print('Thanks for playing!')
                return
            elif user_input == '':
                print("Starting a new game...")
                break

if __name__ == "__main__":
    start_game()