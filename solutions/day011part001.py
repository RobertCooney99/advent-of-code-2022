# ADVENT OF CODE 2022: DAY 001 PART 001
# 
# puzzle input: input is a text file of elves' inventories
# containing the number of calories of food items, each
# elves inventory (if any) separated by a blank line.
#
# puzzle output: the number of calories of the elf
# with the highest number of calories.

from utils import aochelper
import math

input = aochelper.text_to_string("11")

monkeys = input.split("Monkey ")[1:]

class MonkeyManager():
    def __init__(self):
        self.monkeys = {}

    def add_monkey(self, monkey):
        self.monkeys[monkey.id] = monkey

    def print_monkeys(self):
        for monkey in self.monkeys.values():
            monkey.print_monkey()

    def execute_multiple_rounds(self, number_of_rounds):
        for i in range(number_of_rounds):
            print(f"ROUND {i + 1}")
            self.execute_round()
            for monkey in self.monkeys.values():
                print(f"{monkey.id} : {monkey.items}")
            print("\n\n")

    def get_monkey_inspection_counts(self):
        counts = []
        for monkey in self.monkeys.values():
            counts.append(monkey.inspection_count)
        return counts

    def execute_round(self):
        print("\n Executing round")
        for monkey in self.monkeys:
            print(monkey)
            self.monkeys[monkey].take_turn()

    def throw_item(self, monkey_to_id, item):
        self.monkeys[monkey_to_id].catch_item(item)

class Monkey():
    def __init__(self, id, details, monkey_manager):
        self.monkey_manager = monkey_manager
        self.id = id
        self.items = []
        self.populate_details(details)
        self.inspection_count = 0

    def print_monkey(self):
        print(f"Monkey ID: {self.id}")
        print(f"Items: {self.items}")
        print(f"Worry operation: {self.operation}")
        print(f"Test val: {self.test_value}")
        print(f"True monkey: {self.true_monkey}")
        print(f"False monkey: {self.false_monkey}")

    def catch_item(self, item):
        self.items.append(item)

    def populate_details(self, details):
        details = details.split("\n")

        details_mapping = {
            "Starting items": self.populate_starting_items,
            "Operation": self.populate_operation,
            "Test": self.populate_test,
            "If true": self.populate_true,
            "If false": self.populate_false
        }

        for detail in details:
            command, values = detail.strip().split(":")
            values = values.strip()
            # print(f"COMMAND {command} VALUES {values}")
            details_mapping[command](values)

    def populate_starting_items(self, values):
        for value in values.split(","):
            # print(f"ADDING ITEM {value.strip()}")
            self.items.append(int(value.strip()))

    def populate_operation(self, values):
        # print(f"OP {values}")
        operation = values.split("=")[1].strip().replace("old", "worry")
        # print(f"OP NEW {operation}")
        self.operation = operation

    def populate_test(self, values):
        test_value = values.split("by")[1].strip()
        self.test_value = int(test_value)
        # print(f"TEST DIV BY {test_value}")

    def populate_true(self, values):
        monkey_id = values.split("monkey")[1].strip()
        self.true_monkey = monkey_id
        # print(f"TRUE MONKEY {monkey_id}")

    def populate_false(self, values):
        monkey_id = values.split("monkey")[1].strip()
        self.false_monkey = monkey_id
        # print(f"FALSE MONKEY {monkey_id}")

    def take_turn(self):
        while (self.items):
            self.inspection_count += 1
            worry = item = self.items.pop(0)
            new_worry = eval(self.operation)
            # print(f"NEW WORRY: {new_worry}")
            after_worry = math.floor(new_worry / 3)
            # print(f"AFTER {after_worry}")
            divisible = after_worry % self.test_value
            if divisible == 0:
                # print("TRUE MONKEY")
                self.monkey_manager.throw_item(self.true_monkey, after_worry)
            else:
                # print("FALSE MONKEY")
                self.monkey_manager.throw_item(self.false_monkey, after_worry)

monkey_manager = MonkeyManager()

for monkey in monkeys:
    monkey_id, monkey_details = monkey[0], monkey[2:].strip()
    monkey = Monkey(monkey_id, monkey_details, monkey_manager)
    monkey_manager.add_monkey(monkey)

print("\n\n\n\n")
monkey_manager.print_monkeys()

monkey_manager.execute_multiple_rounds(20)

counts = monkey_manager.get_monkey_inspection_counts()
print(counts)
print("\n")
top_two = sorted(counts)[-2:]
total = top_two[0] * top_two[1]
print(total)