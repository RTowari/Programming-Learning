#! python3
# pass.py - Test for strong password

import pyperclip, re

passRegex = re.compile(r'''(
    (\D+)?
    (\d+)?
    )''', re.VERBOSE)

passTest = passRegex.search('Fede1997')

print(passTest.groups())

# Output: 



