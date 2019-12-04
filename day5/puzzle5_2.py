from day5.polymer import trigger_polymer
import sys

original_polymer = None
sys.setrecursionlimit(5000)

with open('input.txt') as file:
    original_polymer = [char for char in file.readline().strip()]

shortest_polymer_length = None

for char in 'abcdefghijklmnopqrstuvwxyz':
    print("Testing with {}".format(char))
    sample = list(filter(lambda a: a != char and a != char.upper(), original_polymer))
    processed_polymer = trigger_polymer(sample)
    if not shortest_polymer_length or len(processed_polymer) < shortest_polymer_length:
        shortest_polymer_length = len(processed_polymer)

print("The shortest processed polymer is {} units long".format(shortest_polymer_length))