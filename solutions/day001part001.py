# ADVENT OF CODE 2022: DAY 001 PART 001
# 
# puzzle input: input is a text file of elves' inventories
# containing the number of calories of food items, each
# elves inventory (if any) separated by a blank line.
#
# puzzle output: the number of calories of the elf
# with the highest number of calories.

from utils import aochelper

input = aochelper.txtToString("1")

elves = list(map(lambda basket: sum(map(int, basket.split("\n"))), input.split("\n\n")))
print(f"Highest calories: {sorted(elves)[-1]}")