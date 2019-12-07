from day7.instructions import Instructions

instructions = Instructions(file_name='input.txt')

print(''.join(instructions.step_order()))