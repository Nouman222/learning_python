# The Challenge: "The Secret Code Breaker"

# Build a small interactive game where the user has to guess a randomly generated secret code and clean up a scrambled hint.

# Requirements:

# 1. Variables, Int, & Random:
# 	• Generate a random secret number between 10 and 50 using the random module.
# 	• Create a variable attempts_left set to 5.
# 	• Create a boolean variable is_won set to False.
# 2. String & String Methods:
# 	• Create a messy hint string: raw_hint = "   tHe sEcReT nUmBeR iS eVeN   " (Note: make sure your logic checks if the actual random number is even or odd, or adjust the hint dynamically!).
# 	• Use string methods to remove the extra spaces from both ends and format it cleanly (e.g., all lowercase or capitalized properly).
# 	• Print the cleaned hint to the user, along with the total character length of the cleaned hint.

import random

# # 1. Variables, Int, & Random
# secret_number = random.randint(10, 50)
# attempts_left = 5
# is_won = False

# # 2. String & String Methods
# raw_hint = "   tHe sEcReT nUmBeR iS eVeN   "
# clean_hint = raw_hint.strip().capitalize()  # Gives: "The secret number is even"

# # Dynamically update the hint if secret_number is odd
# if secret_number % 2 != 0:
#     clean_hint = clean_hint.replace("even", "odd")

# # Game Loop
# for ans in range(attempts_left):
#     user = int(input("Guess the number between 10 and 50: "))

#     if user == secret_number:
#         print("Great, you won!")
#         is_won = True
#         break
#     else:
#         attempts_left -= 1
#         print(f"Wrong! Attempts left: {attempts_left}")
#         print(f"Hint: {clean_hint} (Length: {len(clean_hint)} characters)")

# if not is_won:
#     print(f"Game over! The secret number was {secret_number}.")


# 3. While Loop & Conditionals:
# 	• Run a while loop that continues as long as attempts_left > 0 and is_won is False.
# 	• Inside the loop, ask the user for a guess (convert the input to an int).
# 	• Use if / elif / else to check if the guess is too high, too low, or correct.
# 	• If correct, set is_won = True and break out of the loop.
# 	• If wrong, decrease attempts_left by 1.
# 4. Ternary Operator:
# 	• After each wrong guess, use a single-line ternary operator to print either "1 attempt left!" (if attempts_left == 1) or f"{attempts_left} attempts left!" (for any other number).

secret_number = random.randint(10, 50)
attempts_left = 5
is_won = False

while attempts_left > 0 and not is_won:
  user_ans = int(input("Guess the secret number between 10 and 50: "))

  if user_ans == secret_number:
    print("You won! Congratulations!")
    is_won = True
    break
  else:
    if user_ans < secret_number:
      print("Guess is too low")
    else:
      print("Guess is too high")

    attempts_left -= 1
    print(
        "1 attempt left!"
        if attempts_left == 1
        else f"{attempts_left} attempts left!"
    )



# 5. For Loop (Victory/Game Over Bonus):
# 	• After the while loop ends, check is_won.
# 	• If True, use a for loop to print a celebratory message 3 times (e.g., "Access Granted!").
# 	• If False, print "Game Over!" and reveal the secret number.
