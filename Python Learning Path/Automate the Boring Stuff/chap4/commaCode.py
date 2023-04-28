def main():

    listOfWords = []

    print("Type a word or a number:")

    for i in range(3):
        word = input()
        listOfWords.append(word)

    niceList(listOfWords)

def niceList(listOfWords):

    #Print all char except last
    for i in range(len(listOfWords) - 1):
        print(listOfWords[i], end = ", ")

    #Print last char with an and by the end

    print("and", listOfWords[-1], end=".")


        




if __name__ == "__main__":
    main()