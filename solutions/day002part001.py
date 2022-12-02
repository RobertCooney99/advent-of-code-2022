# ADVENT OF CODE 2022: DAY 002 PART 001
#
# puzzle context: playing a game of rock, paper, scissors
# against an elf.
# 
# puzzle input: input is a text file of lines separated
# by a line break, each line contains two characters 
# with a space inbetween. the first character (A, B or C)
# indicates the move of the elf (rock, paper scissors
# respectively), the second character is the move you
# have been told to make (X, Y or Z which again is rock,
# paper, scissors respectively).
#
# in this game you get 1, 2 and 3 points for rock, paper
# and scissors respectively, plus 3 and 6 points for a draw
# and win respectively.

# puzzle output: your total score using puzzle input

from utils import aochelper

input = aochelper.txtToString("2")

def replaceFromDict(list, dict):
    for k, v in dict.items():
        list = list.replace(k, v)
    return list

numberMapping = {"A": "1", "B": "2", "C": "3", "X": "1", "Y": "2", "Z": "3", " ": ""}

rounds = map(lambda round: list(map(int, replaceFromDict(round.strip(), numberMapping))), input.split("\n"))

def calcRoundPoints(round):
    elfsTurn, myTurn = round
    result = (myTurn - elfsTurn) * (myTurn ** 2)
    if result in [9, 4, -2]:
        return (6 + myTurn)
    elif result == 0:
        return (3 + myTurn)
    else:
        return myTurn

total = sum(list(map(lambda round: calcRoundPoints(round), rounds)))
print(f"Points total: {total}")