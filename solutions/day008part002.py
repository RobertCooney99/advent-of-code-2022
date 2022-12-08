# ADVENT OF CODE 2022: DAY 008 PART 002
# 
# puzzle input: input is a text file of tree heights.
# a tree has a 'scenic score' which is calculated by
# multiplying the number of trees which can be seen
# from that given tree in all 4 directions.
# (i.e. up * down * left * right = scenic score)
#
# puzzle output: the highest scenic score in the
# forest

from utils import aochelper

input = aochelper.text_to_string("8")

tree_rows = input.split("\n")

class Tree:
    def __init__(self, height, index):
        self.height = height
        self.index = index

# TODO: implement cache for tree visibility

row_length = len(tree_rows[0])
column_length = len(tree_rows)

highest = 0
for row_index in range(1, row_length - 1):
    for column_index in range(1, column_length - 1):
        height = int(tree_rows[row_index][column_index])

        visible = [0, 0, 0, 0]

        for left_column_index in reversed(range(0, column_index)):
            visible[0] += 1
            if int(tree_rows[row_index][left_column_index]) >= height:
                break
        for right_column_index in range(column_index + 1, column_length):
            visible[1] += 1
            if int(tree_rows[row_index][right_column_index]) >= height:
                break
        for up_row_index in reversed(range(0, row_index)):
            visible[2] += 1
            if int(tree_rows[up_row_index][column_index]) >= height:
                break
        for down_row_index in range(row_index + 1, column_length):
            visible[3] += 1
            if int(tree_rows[down_row_index][column_index]) >= height:
                break

        scenic_score = visible[0] * visible[1] * visible[2] * visible[3]
        if scenic_score > highest:
            highest = scenic_score


print(f"Highest scenic score: {highest}")