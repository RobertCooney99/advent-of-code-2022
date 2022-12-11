# ADVENT OF CODE 2022: DAY 010 PART 002
# 
# puzzle input: input is a text file
#
# puzzle output: x

from utils import aochelper
import math

input = aochelper.text_to_string("10")

commands = input.split("\n")

class CPU:
    def __init__(self):
        print("CPU")
        self.crt = CRT()
        self.register = 1
        self.cycles = 0

        self.instruction_mapping = {
            "addx": self.addx_process,
            "noop": self.noop_process
        }
        self.instruction_counter = 0

    def execute_instruction(self, instruction, values):
        self.instruction_counter += 1
        self.instruction_mapping[instruction](values)

    def addx_process(self, values):
        increment = int(values[0])
        for i in range(2):
            self.increment_cycles()
            if i == 1:
                self.register += increment
            
    def noop_process(self, values):
        self.increment_cycles()

    def increment_cycles(self):
        self.cycles += 1
        if self.cycles < 420:
            self.crt.draw(self.cycles, self.register)

class CRT:
    def __init__(self):
        print("CRT")
        self.screen = [["."] * 40 for _ in range(6)]

    def draw(self, cycle, register):
        row = math.floor((cycle - 41) / 40) + 1
        column = (((cycle % 40) - 1) % 40)

        pixels = [register - 1, register, register + 1]
        print(f"{cycle} {row} {column} {pixels}")

        if column in pixels:
            # print("DRAWING")
            self.screen[row][column] = "#"
            # self.render_screen()
        
    def render_screen(self):
        for row in self.screen:
            print("".join(row))

cpu = CPU()

for command in commands:
    instruction, *values = command.split(" ")
    cpu.execute_instruction(instruction, values)

cpu.crt.render_screen()