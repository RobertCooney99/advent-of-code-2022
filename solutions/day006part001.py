# ADVENT OF CODE 2022: DAY 006 PART 001
# 
# puzzle input: input is a text file containing a
# communication stream of characters. a section
# of 4 distinct letters marks the start of the
# communication packet.
#
# puzzle output: the number of characters processed
# before the first start-of-packet marker is detected

from utils import aochelper

input = aochelper.text_to_string("6")

characters_processed = 0
for index in range(0, len(input) - 3):
    if len(set(input[index:index+4])) == 4:
        characters_processed = index + 4
        break

print(f"Found 4 distinct characters after {characters_processed} characters")

