# ADVENT OF CODE 2022: DAY 008 PART 001
# 
# puzzle input: input is a text file of tree heights
# in a forest. a tree is visible if in any direction
# (up, down, left or right) all the trees between it
# and the edge are shorter.
#
# puzzle output: how many trees visible from outside
# of the forest.

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

inner_visible_count = 0

for row_index in range(1, row_length - 1):
    for column_index in range(1, column_length - 1):
        height = int(tree_rows[row_index][column_index])

        visible = [True, True, True, True]

        for left_column_index in range(0, column_index):
            if int(tree_rows[row_index][left_column_index]) >= height:
                visible[0] = False
        for right_column_index in range(column_index + 1, column_length):
            if int(tree_rows[row_index][right_column_index]) >= height:
                visible[1] = False
        for up_row_index in range(0, row_index):
            if int(tree_rows[up_row_index][column_index]) >= height:
                visible[2] = False
        for down_row_index in range(row_index + 1, column_length):
            if int(tree_rows[down_row_index][column_index]) >= height:
                visible[3] = False

        if visible[0] or visible[1] or visible[2] or visible[3]:
            inner_visible_count += 1

outer_visible_count = (row_length * 2) + (column_length * 2) - 4
total_visible_count = inner_visible_count + outer_visible_count

print(f"Total number of visible trees: {total_visible_count}")