#! python3
# pass.py - Test for strong password

import pyperclip, re

passRegex = re.compile(r"(\w+)")

passTest = passRegex.findall("Auto Fede 1997")

print(passTest)

# Output: list with Auto, Fede and 1997 as separated strings or togheter if the original string has no spaces



