# ADVENT OF CODE 2022: DAY 002 PART 001
#
# puzzle context: playing a game of rock, paper, scissors
# against an elf.
# 
# puzzle input: input is a text file of lines separated
# by a line break, each line contains two characters 
# with a space inbetween. the first character (A, B or C)
# indicates the move of the elf (rock, paper scissors
# respectively), the second character is the how the round
# needs to end (X, Y or Z) which is a loss, draw and win
# respectively).
#
# in this game you get 1, 2 and 3 points for playing rock,
# paper and scissors respectively, plus 3 and 6 points
# for a draw and win respectively.

# puzzle output: your total score using puzzle input

from utils import aochelper

input = aochelper.txtToString("2")

def replaceFromDict(item, dict):
    for k, v in dict.items():
        item = item.replace(k, v)
    return item

characterMapping = {"A": "1", "B": "2", "C": "3", "X": "loss", "Y": "draw", "Z": "win"}

rounds = list(map(lambda round: replaceFromDict(round.strip(), characterMapping).split(" "), input.split("\n")))
pointCalculators = {"loss": lambda x: (((x - 1 ) + 2) % 3) + 1, "draw": lambda x: 3 + x, "win": lambda x: 6 + (((x - 1) - 2) % 3) + 1}

def calculatePoints(round):
    elfMove, outcome = round
    return pointCalculators[outcome](int(elfMove))

total = sum(list(map(lambda round: calculatePoints(round), rounds)))
print(f"Points total: {total}")