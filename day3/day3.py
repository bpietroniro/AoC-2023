'''
Part 1

High-level plan:
- scan input lines for symbols
- for each symbol, check all the positions where it could have a number adjacent to it:
  - in the same line, at the indices to the left and right of the symbol
  - in the lines directly before and after the symbol's line, at the same index
  - in the lines directly before and after the symbol's line, at the indices to the left and right of the symbol

- in order to facilitate checking the indices AND grabbing the whole number, we can create a data structure:
  - for each string,
    - for each index,
      - the key is the index, and the value is the entire number.

To accomplish this, once we encounter a number (reading from left to right), we should probably use regex to grab all
directly adjacent numbers to the right of it, take the length of this string, and ....
THIS IS TOO COMPLICATED MAYBE

Start over.
- initialize sum at 0
- scan input lines for numbers
- based on the starting index length of the number, determine which indices in the rows above and below could make the
  number valid if they contain a symbol
- check those indices for symbols
- if there's a symbol,
'''

import sys
import re

schematic = sys.stdin.readlines()
line_length = len(schematic[0])

idx = 0
num_sum = 0
while idx < len(schematic):
    current_line = schematic[idx]
    previous_line = '.' * line_length if idx == 0 else schematic[idx - 1]
    next_line = '.' * line_length if idx == len(schematic) - 1 else schematic[idx + 1]

    for number in re.finditer(r'\d+', current_line):
        start, end = number.span()
        start = int(start)
        end = int(end)
        start = start - 1 if start > 0 else start
        if (re.search(r'[@#$%\^&\*/\-=\+]', previous_line[start:end+1]) or 
            re.search(r'[@#$%\^&\*/\-=\+]', next_line[start:end+1]) or
            re.search(r'[@#$%\^&\*/\-=\+]', current_line[start]) or
            re.search(r'[@#$%\^&\*/\-=\+]', current_line[end])
        ):
            num_sum += int(number.group())

    idx += 1

print(num_sum)