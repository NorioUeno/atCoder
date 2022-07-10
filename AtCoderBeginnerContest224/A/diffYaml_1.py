#!/opt/homebrew/bin/python3

import re

S = input()
if re.search('er$',S):
    print("er")
else:
    print("ist")
