stuff = {"rope": 1, "torch": 6, "goldCoin": 42, "dagger": 1, "arrow": 12}


def displayInventory(stuff):

    print("Inventory: ")

    totalItems = 0

    for i, n in stuff.items():
        print (n, i)
        totalItems = totalItems + n

    print("Total nuber of items: ", totalItems)

displayInventory(stuff)
