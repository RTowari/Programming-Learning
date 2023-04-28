#! python3
# replace.py - Reads a file and replace the words ADJETIVE, NOUN, ADVERB or VERB with new words the user decide to write

# Open a .txt file and copy all the content into a string. Close the file after that
file = open("Text.txt", "r")
oldString = file.read()
file.close()

# Replace word in the list with new ones
words = ["ADJECTIVE", "NOUN", "ADVERB", "VERB"]
newString = []

for word in words:
    # For each iteration ask user for replacement word
    print("Enter an " + str.lower(word) + ": ")
    newWord = input()

    print("Here is word: " + word)
    print("Here is newWord: " + newWord)

    # newString will have the new words
    newString = oldString.replace(word, newWord)
    print("Here is newString: " + newString)

    # newString will be copied into oldString
    oldString = newString
    print("Here is oldString: " + oldString)

# TODO: # Write string into a new text file
file = open("newText.txt", "w")

file.write(oldString)

file.close()



