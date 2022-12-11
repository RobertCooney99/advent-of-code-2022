# ADVENT OF CODE 2022: DAY 009 PART 001
# 
# puzzle input: input is a text file
#
# puzzle output: x

from utils import aochelper

input = aochelper.text_to_string("9")

lines = input.split("\n")
instructions = list(map(lambda line: line.split(" "), lines))

class ModelManager():
    def __init__(self):
        self.head_position = [0, 0]
        self.tail_position = [0, 0]

        self.tail_history = [[0,0]]

        self.instruction_mapping = {
            "R": [1,0],
            "L": [-1,0],
            "U": [0,1],
            "D": [0,-1],
            "UR": [1,1],
            "UL": [-1,1],
            "DR": [1,-1],
            "DL": [-1,-1]
        }

    def execute_instruction(self, instruction):
        direction, steps = instruction
        for i in range(int(steps)):
            self.move_head(self.instruction_mapping[direction])
            self.calculate_tail_position()

    def move_head(self, movement):
        self.head_position = self.position_addition(self.head_position, movement)
        
    def move_tail(self, movement):
        self.tail_position = self.position_addition(self.tail_position, movement)
        if self.tail_position not in self.tail_history:
            self.tail_history.append(self.tail_position)

    def get_tail_history_count(self):
        return len(self.tail_history)

    def position_addition(self, list_one, list_two):
        return [list_one[0] + list_two[0], list_one[1] + list_two[1]]

    def calculate_tail_position(self):
        tail = self.tail_position
        head = self.head_position
        if (head[1] == tail[1] and (head[0] - tail[0] == 2)):
            self.move_tail(self.instruction_mapping["R"])
            return
        elif(head[1] == tail[1] and (head[0] - tail[0] == -2)):
            self.move_tail(self.instruction_mapping["L"])
            return
        elif(head[0] == tail[0] and (head[1] - tail[1] == 2)):
            self.move_tail(self.instruction_mapping["U"])
            return
        elif(head[0] == tail[0] and (head[1] - tail[1] == -2)):
            self.move_tail(self.instruction_mapping["D"])
            return

        if (self.distance_between_points(self.head_position, self.tail_position) > 1):
            x_distance = self.head_position[0] - self.tail_position[0]
            y_distance = self.head_position[1] - self.tail_position[1]

            if (x_distance == 1 and y_distance == 2):
                self.move_tail(self.instruction_mapping["UR"])
                return
            elif (x_distance == -1 and y_distance == 2):
                self.move_tail(self.instruction_mapping["UL"])
                return
            elif (x_distance == -1 and y_distance == -2):
                self.move_tail(self.instruction_mapping["DL"])
                return
            elif (x_distance == 1 and y_distance == -2):
                self.move_tail(self.instruction_mapping["DR"])
                return
            elif (x_distance == 2 and y_distance == 1):
                self.move_tail(self.instruction_mapping["UR"])
                return
            elif (x_distance == 2 and y_distance == -1):
                self.move_tail(self.instruction_mapping["DR"])
                return
            elif (x_distance == -2 and y_distance == 1):
                self.move_tail(self.instruction_mapping["UL"])
                return
            elif (x_distance == -2 and y_distance == -1):
                self.move_tail(self.instruction_mapping["DL"])
                return

    def distance_between_points(self, point_one, point_two):
        x1, y1 = point_one
        x2, y2 = point_two
        return ( (x2 - x1)**2 + (y2 - y1)**2 )**(1/2)



model_manager = ModelManager()

for instruction in instructions:
    model_manager.execute_instruction(instruction)

print(model_manager.get_tail_history_count())
