#! python3
# pass.py - Test for strong password

import pyperclip, re

passRegex = re.compile(r"(\d+)")

passTest = passRegex.findall("Auto Fede 1997")

print(passTest)

# Output: list with 1997

