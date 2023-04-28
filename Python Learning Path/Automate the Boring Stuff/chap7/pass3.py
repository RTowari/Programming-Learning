#! python3
# pass.py - Test for strong password

import pyperclip, re

passRegex = re.compile(r"(\D+)?(\d+)?")

passTest = passRegex.search("AutoFede")

print(passTest.groups())

# Output: AutoFede and 197 as different strings in a list



