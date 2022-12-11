# ADVENT OF CODE 2022: DAY 010 PART 001
# 
# puzzle input: input is a text file
#
# puzzle output: x

from utils import aochelper

input = aochelper.text_to_string("10")

commands = input.split("\n")

class CPU:
    def __init__(self):
        print("CPU")
        self.register = 1
        self.cycles = 0

        self.instruction_mapping = {
            "addx": self.addx_process,
            "noop": self.noop_process
        }

        self.special_signal_strength = 0
        self.instruction_counter = 0

    def execute_instruction(self, instruction, values):
        self.instruction_counter += 1
        print(f"{self.instruction_counter} {instruction} {values}")
        self.instruction_mapping[instruction](values)

    def addx_process(self, values):
        increment = int(values[0])
        for i in range(2):
            self.cycles += 1
            self.check_cycles()
            if i == 1:
                self.register += increment
            
    def noop_process(self, values):
        self.cycles += 1
        self.check_cycles()

    def check_cycles(self):
        if (self.cycles == 20) or (self.cycles > 20 and (self.cycles - 20) % 40 == 0):
            print(f"SPECIAL SIGNAL {self.cycles} {self.cycles} * {self.register} = {self.cycles * self.register}")
            self.special_signal_strength += self.cycles * self.register

cpu = CPU()
print(cpu)

for command in commands:
    instruction, *values = command.split(" ")
    cpu.execute_instruction(instruction, values)

print(cpu.special_signal_strength)