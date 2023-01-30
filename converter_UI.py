# Name: Rachelyn Flazer
# Course: CS 361
# Assignment 5 - Converter Ui
# Description:


import os
import sys
import time
import re

path = "/Users/rayche/PycharmProjects/CS361/Assignment5"
dirs = os.listdir(path)

# CSH2 - n/a
# CSH4 - same features for both smartphone and tablet versions
# CSH3 - app information and instructions
print("This tool converts color values from RGB to HEX or HEX to RGB.")
print("Use arrow key to get started.")
print("Enter 'h' for help and 'x' to exit app.\n")
# CSH1 - two conversion options with description provided
choice = input("Select conversion option. Enter '1' for RGB to HEX or '2' for HEX to RGB: ")


def rgb_to_hex():
    while True:
        try:
            # CSH6 - user is ask to enter RGB color values separately
            r = int(input("\nEnter RGB color values:\nR: "))
            g = int(input("G: "))
            b = int(input("B: "))
            # CSH7 - error is given if user does not enter correct value
            if r > 255 or r < 0:
                print('\nError! Ensure RGB values are between 0 and 255.')
                return
            if g > 255 or g < 0:
                print('\nError! Ensure RGB values are between 0 and 255.')
                return
            if b > 255 or b < 0:
                print('\nError! Ensure RGB values are between 0 and 255.')
                return
            rgb_code = ('#' + '{:02x}{:02x}{:02x}').format(r, g, b)
            print("\nHEX color code:", rgb_code)
            p_file = open(os.path.join(sys.path[0], 'palette-service.txt'), 'w')
            p_file.write(rgb_code.lstrip('#'))
        except ValueError:
            continue
        else:
            break


def hex_to_rgb():
    # CSH5 - user input can use delete or back keys to delete/change input
    while True:
        hex_code = input("Enter HEX code: ").lstrip('')
        try:
            if len(hex_code) != 6:
                print('Invalid input. Enter 6 digits in range 0-F.')
                return
            str = hex_code
            not_match = re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', str)
            if not_match:
                print('Invalid input. Enter 6 digits in range 0-F.')
            print("RGB color code: ", tuple(int(hex_code[i:i + 2], 16) for i in (0, 2, 4)))

        except ValueError:
            print('Invalid input. Enter 6 digits in range 0-F.\n')
            continue
        else:
            break

    p_file = open(os.path.join(sys.path[0], 'palette-service.txt'), 'w')
    p_file.write('{}'.format(tuple(int(hex_code[i:i + 2], 16) for i in (0, 2, 4))))
    # read conversions from palette-service.txt
    time.sleep(2)
    p_file = open(os.path.join(sys.path[0], 'palette-service.txt'), 'r')
    # f_path = p_file.readline()
    p_file.close()
    # print('Saved in textfile: ', f_path)


if choice == "1":
    rgb_to_hex()
elif choice == "2":
    hex_to_rgb()
elif choice == "h":
    print("Help: ")
    print("  h: Print this help menu.")
    print("  x: Exits the tool.")
elif choice == "x":
    # CSH8 - allows users to change decision to exit app or continue
    ans = input("Are you sure ('yes' or 'no')? ")
    if ans == 'yes':
        exit()
    elif ans == 'no':
        choice = input("\nSelect conversion option. Enter '1' for RGB to HEX or '2' for HEX to RGB: ")
        if choice == "1":
            rgb_to_hex()
        elif choice == "2":
            hex_to_rgb()
else:
    print('Not recognized.')
