from day5.polymer import trigger_polymer

original_polymer = None

with open('input.txt') as file:
    original_polymer = [char for char in file.readline().strip()]

print("The original polymer is {} units long".format(len(original_polymer)))
processed_polymer = trigger_polymer(original_polymer)

print("The processed polymer is {} units long".format(len(processed_polymer)))
