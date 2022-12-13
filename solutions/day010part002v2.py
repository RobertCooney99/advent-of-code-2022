# ADVENT OF CODE 2022: DAY 010 PART 002
# 
# puzzle input: input is a text file
#
# puzzle output: x

from utils import aochelper
import math
from PIL import Image, ImageDraw, ImageEnhance
from pytesseract import pytesseract

input = aochelper.text_to_string("10")

commands = input.split("\n")

class CPU:
    def __init__(self):
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
        self.screen = [[" "] * 40 for _ in range(6)]

    def draw(self, cycle, register):
        row = math.floor((cycle - 41) / 40) + 1
        column = (((cycle % 40) - 1) % 40)

        pixels = [register - 1, register, register + 1]

        if column in pixels:
            self.screen[row][column] = "X"
        
    def render_screen(self):
        for row in self.screen:
            print("".join(row))

    def get_screen(self):
        screen = ""
        for row in self.screen:
            screen += "".join(row) + "\n"
        return screen

cpu = CPU()

for command in commands:
    instruction, *values = command.split(" ")
    cpu.execute_instruction(instruction, values)

cpu.crt.render_screen()

def binarize(image):
  thresh=60

  image=image.convert('L') 

  width,height=image.size

  for x in range(width):
    for y in range(height):
      if image.getpixel((x,y)) < thresh:
        image.putpixel((x,y),0)
      else:
        image.putpixel((x,y),255)

  return image

def jumble_image_size(image):
    image = image.resize((100, 15))
    image = image.resize((400, 60))
    image = image.resize((100, 15))
    image = image.resize((400, 60))

    return image

image = Image.new('RGB', (260, 120))
draw = ImageDraw.Draw(image)

draw.text((15, 15), cpu.crt.get_screen(), align ="left") 

image = jumble_image_size(image)

contrast_enhancer = ImageEnhance.Contrast(image)
image = contrast_enhancer.enhance(3)

image = jumble_image_size(image)

sharpness_enhancer = ImageEnhance.Sharpness(image)
image = sharpness_enhancer.enhance(10)

image = binarize(image)

image = jumble_image_size(image)

text = pytesseract.image_to_string(image, lang='eng', config='--psm 6')
print(f"\nCharacters on the CRT: {text[:-1]}")