#!/usr/bin/env python3

# Created by Donggeun Lim
# Created on December 2020
# This program is number guessing game

import random


def main():
    # this function checks if number is not 5

    # input
    integer_as_string = input("Enter your number ")
    print("")

    # process
    random_number = random.randint(1, 9)  # a number between 1 and 9

    try:
        integer_as_number = int(integer_as_string)

        if random_number == integer_as_number:
            # output
            print("You are right!")
            print("random number is {}".format(random_number))
        else:
            print("you are wrong")
            print("random number is {}".format(random_number))

    except Exception:
        print("This was not an integer")


if __name__ == "__main__":
    main()
