# ADVENT OF CODE 2022: DAY 003 PART 002
# 
# puzzle input: text file
#
# puzzle output: priority total

from utils import aochelper

input = aochelper.text_to_string("3")

rucksacks = list(map(lambda rucksack: "".join(set(rucksack)), input.split("\n")))
grouped_rucksacks = [rucksacks[x:x+3] for x in range(0, len(rucksacks), 3)]

badges = []
for rucksack_group in grouped_rucksacks:
    for item in rucksack_group[0]:
        if item in rucksack_group[1] and item in rucksack_group[2]:
            badges += item

alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
priority_total = sum(list(map(lambda letter: alphabet.index(letter) + 1, badges)))

print(f"Priority total: {priority_total}")
    