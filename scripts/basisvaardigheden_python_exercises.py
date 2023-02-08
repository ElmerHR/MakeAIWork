from random import randint
import re

def main():
    """Basisvaardigheden Python - Exercises
    """

    # Exercises 1.8 - vraag 4
    answer = (512-282)/(47*48+5)
    print(f"Exercises 1.8 - vraag 4: {answer:.4f}\n")

    # Exercises 1.8 - vraag 5
    print(f"Exercises 1.8 - vraag 5:")
    user_input = int(input("Enter a number: "))

    print("The square of ", user_input, " is ", user_input**2, ".", sep="")

    # Exercises 3.8 - vraag 2
    x = randint(1,50)
    y = randint(2,5)
    print(f"\nExercises 3.8 - vraag 2\nx: {x}\ny: {y}\nx^y: {x**y}")

    # Exercises 3.8 - vraag 6
    print(f"\nExercises 3.8 - vraag 6:")
    user_input_x = int(input("Enter a number for x: "))
    user_input_y = int(input("Enter a number for y: "))
    answer_formula = abs(user_input_x-user_input_y)/(user_input_x+user_input_y)

    print(f"\nThe answer to the formula |x-y|/(x+y) is {answer_formula:.3f}.")

    # Exercises 6.11 - vraag 1
    print(f"\nExercises 6.11 - vraag 1:\n")
    user_string = input("Please input a string: ")

    # Total number of chars
    str_chars = len(user_string)

    # seventh char of string OR return message
    seventh_char = user_string[8] if len(user_string) > 6 else "The string is not long enough"
    
    letters_to_spaces = re.sub(r'[A-Za-z]*', " ", user_string)
    
    print(
        f"\nVoor deze string hebben het volgende:"
        f"\nThe total number of characters in the string: {str_chars}"
        f"\nThe string repeated 10 times: {10*user_string}"
        f"\nThe first character of the string: {user_string[0]}"
        f"\nThe first three characters of the string: {user_string[0:3]}"
        f"\nThe last three characters of the string: {user_string[-3:]}"
        f"\nThe string backwards: {user_string[::-1]}"
        f"\nThe seventh char of the string: {seventh_char}"
        f"\nThe first and last chars removed: {user_string[1:-1]}"
        f"\nThe string in all caps: {user_string.upper()}"
        f"\nThe string with every a replaced with an e: {user_string.replace('a', 'e')}"
        f"\nThe string with every letter replaced by a space: {letters_to_spaces}"
    )
    


if __name__ == "__main__":
    main()