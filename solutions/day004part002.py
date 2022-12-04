# ADVENT OF CODE 2022: DAY 004 PART 002
# 
# puzzle input: text file
#
# puzzle output: number of assignment pairs with overlapping ranges

from utils import aochelper

input = aochelper.text_to_string("4")

def split_pair_to_ints(pair):
    return [[int(val) for val in assignment.split("-")] for assignment in pair.split(",")]

assignment_pairs = list(map(lambda pair: split_pair_to_ints(pair), input.split("\n")))

total_pairs = 0
for pair in assignment_pairs:
    if pair[0][0] >= pair[1][0] and pair[0][0] <= pair[1][1]:
        total_pairs += 1
    elif pair[1][0] >= pair[0][0] and pair[1][0] <= pair[0][1]:
        total_pairs += 1

print(f"Total pairs: {total_pairs}")
