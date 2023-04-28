#! python3
# pass.py - Test for strong password

import pyperclip, re

passRegex = re.compile(r'''(
    [a-zA-Z+]?
    )''', re.VERBOSE)

passTest = passRegex.findall('Fede')

print(passTest)

# Output: 



