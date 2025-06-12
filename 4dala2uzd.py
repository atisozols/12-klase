latvAlphabet = "AĀBCČDEĒFGHIĪJKLMNOŌPRSTUVZŽ"

dictionary = {}

for letter in latvAlphabet:
    dictionary[letter] = []

def notFull(dictionary):
    for key in dictionary:
        if dictionary[key] == []:
            return True
    return False

while notFull(dictionary):
    word = input("Enter a word: ")
    first = word[0]

    if first in dictionary:
        dictionary[first] = [word]




        