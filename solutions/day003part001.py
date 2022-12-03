# ADVENT OF CODE 2022: DAY 003 PART 001
# 
# puzzle input: text file
#
# puzzle output: priority total

from utils import aochelper

input = aochelper.txtToString("3")

def deduplicateChars(string):
    return "".join(set(string))

def splitStringAndDeduplicteChars(string):
    return [deduplicateChars(string[:int(len(string)/2)]), deduplicateChars(string[int(len(string)/2):])]

rucksacks = list(map(lambda rucksack: splitStringAndDeduplicteChars(rucksack), input.split("\n")))

allCommonItems = []
for rucksack in rucksacks:
    commonItems = []
    for item in rucksack[0]:
        if item not in commonItems and item in rucksack[1]:
            commonItems += item
    allCommonItems += commonItems

alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
priorityTotal = sum(list(map(lambda letter: alphabet.index(letter) + 1, allCommonItems)))

print(f"Priority total: {priorityTotal}")
