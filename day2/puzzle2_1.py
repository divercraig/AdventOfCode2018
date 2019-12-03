box_with_two = 0
box_with_three = 0

for box_id in open('input.txt'):
    char_count = {}
    found_two = False
    found_three = False

    for char in box_id:
        if char in char_count:
            char_count[char] = char_count[char] + 1
        else:
            char_count[char] = 1

    for count in char_count.values():
        if not found_two and count == 2:
            found_two = True
            box_with_two += 1
        if not found_three and count == 3:
            found_three = True
            box_with_three += 1

print("checksum = {} * {} = {}".format(box_with_two, box_with_three, box_with_two * box_with_three))


