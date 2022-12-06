# ADVENT OF CODE 2022: DAY 006 PART 002
# 
# puzzle input: input is a text file containing a
# communication stream of characters. a section
# of 14 distinct letters marks the start of the
# message.
#
# puzzle output: the number of characters processed
# before the first start-of-message marker is detected

from utils import aochelper

input = aochelper.text_to_string("6")

characters_processed = 0
for index in range(0, len(input) - 13):
    if len(set(input[index:index+14])) == 14:
        characters_processed = index + 14
        break

print(f"Found 14 distinct characters after {characters_processed} characters")

