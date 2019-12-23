#!/usr/bin/env python3

# Created by: Joseph Palermo
# Created on: December 2019
# This program prints out a word in hexadecimal


def convert(user_word):
    # This function converts a word to hexadecimal

    # dictionaries and lists
    hexadecimal = {}
    characters = []

    # dictionary
    hexadecimal["A"] = "41"
    hexadecimal["B"] = "42"
    hexadecimal["C"] = "43"
    hexadecimal["D"] = "44"
    hexadecimal["E"] = "45"
    hexadecimal["F"] = "46"
    hexadecimal["G"] = "47"
    hexadecimal["H"] = "48"
    hexadecimal["I"] = "49"
    hexadecimal["J"] = "4a"
    hexadecimal["K"] = "4b"
    hexadecimal["L"] = "4c"
    hexadecimal["M"] = "4d"
    hexadecimal["N"] = "4e"
    hexadecimal["O"] = "4f"
    hexadecimal["P"] = "50"
    hexadecimal["Q"] = "51"
    hexadecimal["R"] = "52"
    hexadecimal["S"] = "53"
    hexadecimal["T"] = "54"
    hexadecimal["U"] = "55"
    hexadecimal["V"] = "56"
    hexadecimal["W"] = "57"
    hexadecimal["X"] = "58"
    hexadecimal["Y"] = "59"
    hexadecimal["Z"] = "5a"
    hexadecimal['a'] = "61"
    hexadecimal['b'] = "62"
    hexadecimal['c'] = "63"
    hexadecimal['d'] = "64"
    hexadecimal['e'] = "65"
    hexadecimal['f'] = "66"
    hexadecimal['g'] = "67"
    hexadecimal['h'] = "68"
    hexadecimal['i'] = "69"
    hexadecimal['j'] = "6a"
    hexadecimal['k'] = "6b"
    hexadecimal['l'] = "6c"
    hexadecimal['m'] = "6d"
    hexadecimal['n'] = "6e"
    hexadecimal['o'] = "6f"
    hexadecimal['p'] = "70"
    hexadecimal['q'] = "71"
    hexadecimal['r'] = "72"
    hexadecimal['s'] = "73"
    hexadecimal['t'] = "74"
    hexadecimal['u'] = "75"
    hexadecimal['v'] = "76"
    hexadecimal['w'] = "77"
    hexadecimal['x'] = "78"
    hexadecimal['y'] = "79"
    hexadecimal['z'] = "7a"

    # process
    for counter in user_word:
        if counter in hexadecimal.keys():
            characters.append(hexadecimal[counter])
        else:
            print("Error, unable to find unicode character")

    # output
    return characters


def main():
    # this function outputs a word inputted by the user in Unicode hexadecimal

    # input
    word = input("Enter a word here: ")

    # process
    hexadecimal_word = convert(word)

    # output
    for counter in hexadecimal_word:
        print(counter, end=" ")


if __name__ == "__main__":
    main()
