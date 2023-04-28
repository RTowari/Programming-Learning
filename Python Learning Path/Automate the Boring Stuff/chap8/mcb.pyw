#! python3
# mcb.pyw - Saves and loads pieces of text to the clipboard
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword
#        py.exe mbc.pyw <keyword> - Loads keyword to the clipboard
#        py.exe mcb.pyw list - Loads all keywords to clipboard

import shelve, pyperclip, sys

mcbShelf = shelve.open("mcb")

# Save clipboard content or delete from file
if len(sys.argv) == 3:
    if sys.argv[1].lower() == "save":
        mcbShelf[sys.argv[2]] = pyperclip.paste()
        print("New key saved")
    elif sys.argv[1].lower() == "delete" and sys.argv[2].lower() == "all":
        mcbShelf.clear()
        print("All keys deleted")
        
    elif sys.argv[2].lower() == "delete":
        del mcbShelf[sys.argv[2]]

    


# List keywords and load content
elif len(sys.argv) == 2:
    if sys.argv[1].lower() == "list":
        print("Keys: ")
        pyperclip.copy(str(list(mcbShelf.keys())))
        print(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])

mcbShelf.close()