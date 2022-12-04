# ADVENT OF CODE 2022: DAY 003 PART 001
# 
# puzzle input: text file
#
# puzzle output: priority total

from utils import aochelper

input = aochelper.text_to_string("3")

def deduplicate_chars(string):
    return "".join(set(string))

def split_string_and_deduplicate_chars(string):
    return [deduplicate_chars(string[:int(len(string)/2)]), deduplicate_chars(string[int(len(string)/2):])]

rucksacks = list(map(lambda rucksack: split_string_and_deduplicate_chars(rucksack), input.split("\n")))

all_common_items = []
for rucksack in rucksacks:
    common_items = []
    for item in rucksack[0]:
        if item not in common_items and item in rucksack[1]:
            common_items += item
    all_common_items += common_items

alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
priority_total = sum(list(map(lambda letter: alphabet.index(letter) + 1, all_common_items)))

print(f"Priority total: {priority_total}")
