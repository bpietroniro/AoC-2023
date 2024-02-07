'''
Part 1

initialize sum at 0
read lines of input file into `games`
for each line of games:
  grab the game number and save it as an int
  initialize a dictionary with the keys "red", "green", "blue" and values 0
  after the colon, split the rest of the line by , and ;
  for each of the resulting strings:
    split by space
    convert the first item to int
    if the int is greater than the dictionary value of the second item, replace the value with the int
  if any of the dictionary values exceed 12, 13, or 14, respectively, continue
  sum += game number
return sum

Part 2

collect minimums in another dictionary that initializes the same as in Part 1
draw the rest of the flipping owl
'''

import sys
import re

games = sys.stdin.readlines()

def cube_game_sum(games):
  maximums = {'red': 12, 'green': 13, 'blue': 14}
  possible_game_id_sum = 0
  power_sum = 0

  for line in games:
    possible = True
    power = 1
    game_id, cubes = line.split(':')
    game_id = int(game_id.split(' ')[1])

    handfuls = minimums = {'red': 0, 'green': 0, 'blue': 0}

    for handful in re.split(',|;', cubes):
      amount, color = handful.strip().split(' ')
      amount = int(amount)

      if amount > minimums[color]:
        minimums[color] = amount
      if amount > maximums[color]:
        possible = False
      elif amount > handfuls[color]:
        handfuls[color] = amount
    
    print('\nHandfuls:')
    print(handfuls)
    print('Minimums:')
    print(minimums)

    for amount in minimums.values():
      power *= amount
    power_sum += power

    if not possible:
      continue

    possible_game_id_sum += game_id
  
  return (possible_game_id_sum, power_sum)


print(cube_game_sum(games))