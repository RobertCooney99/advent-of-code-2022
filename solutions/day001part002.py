# ADVENT OF CODE 2022: DAY 001 PART 002
# 
# puzzle input: input is a text file of elves' inventories
# containing the number of calories of food items, each
# elves inventory (if any) by a blank line.
#
# puzzle output: the total number of calories carried by
# the three elves with the highest number of calories.

from utils import aochelper

input = aochelper.text_to_string("1")

elves = list(map(lambda basket: sum(map(int, basket.split("\n"))), input.split("\n\n")))
print(f"Calorie total for top 3 elves combined:{sum(sorted(elves, reverse=True)[:3])}")