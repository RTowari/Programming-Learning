tableData = [['apples', 'oranges', 'cherries', 'banana'],
 ['Alice', 'Bob', 'Carol', 'David'],
 ['dogs', 'cats', 'moose', 'goose']]


# Print table
for n in range(4): # Row
    print("\n")

    for i in range(3): # Column
        
        if len(tableData[i][n]) < 8:

            while len(tableData[i][n]) < 8: # Set all string to have 8 chars
                tableData[i][n] = " " + tableData[i][n]
            print(tableData[i][n], end = "")
        else:
            print(tableData[i][n], end = "")
