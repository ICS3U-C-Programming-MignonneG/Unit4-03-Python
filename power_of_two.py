#!/usr/bin/env python3
# Created by: Mignonne Gihozo
# Created on: 11/16/2026
# This program displays the squares of whole numbers from 0 to the user's number.


def main():
    # This function displays the square of each whole number up to the user's number.

    # Input
    user_input = input("Enter a whole number: ")

    # Process and output
    try:
        user_number = int(user_input)

        if user_number < 0:
            print(f"{user_input} is not a whole number.")
        else:
            for number in range(user_number + 1):
                print(f"{number}^2 = {number ** 2}")
    except ValueError:
        print(f"{user_input} is not a valid whole number.")


if __name__ == "__main__":
    main()
