def collatz_Calc(number):

    while number != 1:

        # Test for even number
        if number % 2 == 0:

            # Go ahead and divide number by 2
            number = number // 2

            print(number)

        # Test of odd number
        else:

            number = number * 3 + 1

            print(number)


print("Write number here: ", end="")
    
try:
    userNumber = int(input())
    collatz_Calc(userNumber)

except ValueError:
    print("You must write an int")

