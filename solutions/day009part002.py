# ADVENT OF CODE 2022: DAY 009 PART 002
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
        self.positions = [[0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0]]

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
            for i in range(1, len(self.positions)):
                self.calculate_knot_position(self.positions[i-1], self.positions[i], i)

    def move_head(self, movement):
        self.positions[0] = self.position_addition(self.positions[0], movement)
        
    def move_knot(self, movement, index):
        self.positions[index] = self.position_addition(self.positions[index], movement)
        if (index == 9) and self.positions[9] not in self.tail_history:
            self.tail_history.append(self.positions[9])

    def get_tail_history_count(self):
        return len(self.tail_history)

    def position_addition(self, list_one, list_two):
        return [list_one[0] + list_two[0], list_one[1] + list_two[1]]

    def calculate_knot_position(self, head, tail, index):
        if (head[1] == tail[1] and (head[0] - tail[0] == 2)):
            self.move_knot(self.instruction_mapping["R"], index)
            return
        elif(head[1] == tail[1] and (head[0] - tail[0] == -2)):
            self.move_knot(self.instruction_mapping["L"], index)
            return
        elif(head[0] == tail[0] and (head[1] - tail[1] == 2)):
            self.move_knot(self.instruction_mapping["U"], index)
            return
        elif(head[0] == tail[0] and (head[1] - tail[1] == -2)):
            self.move_knot(self.instruction_mapping["D"], index)
            return

        if (self.distance_between_points(head, tail) > 1):
            x_distance = head[0] - tail[0]
            y_distance = head[1] - tail[1]

            if (x_distance == 1 and y_distance == 2):
                self.move_knot(self.instruction_mapping["UR"], index)
                return
            elif (x_distance == -1 and y_distance == 2):
                self.move_knot(self.instruction_mapping["UL"], index)
                return
            elif (x_distance == -1 and y_distance == -2):
                self.move_knot(self.instruction_mapping["DL"], index)
                return
            elif (x_distance == 1 and y_distance == -2):
                self.move_knot(self.instruction_mapping["DR"], index)
                return
            elif (x_distance == 2 and y_distance == 1):
                self.move_knot(self.instruction_mapping["UR"], index)
                return
            elif (x_distance == 2 and y_distance == -1):
                self.move_knot(self.instruction_mapping["DR"], index)
                return
            elif (x_distance == -2 and y_distance == 1):
                self.move_knot(self.instruction_mapping["UL"], index)
                return
            elif (x_distance == -2 and y_distance == -1):
                self.move_knot(self.instruction_mapping["DL"], index)
                return
            elif (x_distance == -2 and y_distance == -2):
                self.move_knot(self.instruction_mapping["DL"], index)
                return
            elif (x_distance == -2 and y_distance == 2):
                self.move_knot(self.instruction_mapping["UL"], index)
                return
            elif (x_distance == 2 and y_distance == -2):
                self.move_knot(self.instruction_mapping["DR"], index)
                return
            elif (x_distance == 2 and y_distance == 2):
                self.move_knot(self.instruction_mapping["UR"], index)
                return

    def distance_between_points(self, point_one, point_two):
        x1, y1 = point_one
        x2, y2 = point_two
        return ( (x2 - x1)**2 + (y2 - y1)**2 )**(1/2)



model_manager = ModelManager()

for instruction in instructions:
    model_manager.execute_instruction(instruction)

print(model_manager.get_tail_history_count())
