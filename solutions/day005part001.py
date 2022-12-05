# ADVENT OF CODE 2022: DAY 005 PART 001
# 
# puzzle input: input is a text file containing two
# parts. the first part is number of stacked crates,
# the second part is instructions on how to move the
# crates. in this part of the puzzle crates are moved
# one by one from the top of a stack onto the top of
# another.
#
# puzzle output: after completing all the instructions
# list the crates (letters) at the top of the stacks.

from utils import aochelper

input = aochelper.text_to_string("5")

crates, instructions = input.split("\n\n")
crates = crates.split("\n")
crates.reverse()

stacks = {k: [] for k in range(1,10)}

for crate in crates[1:]:
    for x in range(0, int(len(crate) / 4) + 1):
        value = crate[x*4:(x*4)+3].strip()
        if value:
            stacks[x+1].append(value[1])

for instruction in instructions.split("\n"):
    details = instruction.split(" ")
    amount_to_move, section_from, section_to = int(details[1]), int(details[3]), int(details[5])
    for i in range(amount_to_move):
        stacks[section_to].append(stacks[section_from].pop())

top_crates = "".join(map(lambda stack: stack[-1], stacks.values()))
print(f"Crates at top of stacks: {top_crates}")