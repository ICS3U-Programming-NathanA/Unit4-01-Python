#!/usr/bin/env python3
# Created by: Nathan Araujo
# Created on: Oct 26 2022
# This program asks the user for a number it then adds up every nubmer until it reaches the users number


def main():
    # set counter and sum to 0
    sum = 0
    counter = 0
    # Get the users number
    user_num_string = input("Enter a integer: ")

    # An try catch to catch any errors if they enter a string or a decimal
    try:
        user_num = int(user_num_string)
    except Exception:
        print("Please a enter valid integer")
    else:
        # An if statement to see if the integer is a negative
        if user_num >= 0:
            # A while loop to add up the users sum
            while counter <= user_num:
                print("{} +".format(counter))
                sum = sum + counter
                counter = counter + 1
            print("= {}".format(sum))
        else:
            print("Please enter a positive integer")


if __name__ == "__main__":
    main()
