from day6.manhattan_distance import manhattan_distance

points = []
lowest_x = None
highest_x = None
lowest_y = None
highest_y = None

for line in open('input.txt'):
    x, y = line.split(', ')
    x = int(x)
    y = int(y)
    points.append((x, y))

    if lowest_x is None or x < lowest_x:
        lowest_x = x

    if highest_x is None or x > highest_x:
        highest_x = x

    if lowest_y is None or y < lowest_y:
        lowest_y = y

    if highest_y is None or y > highest_y:
        highest_y = y

safe_area = 0
for x in range(lowest_x, highest_x + 1):
    for y in range(lowest_y, highest_y + 1):
        evaluation_point = (x, y)
        sum_of_distances_to_points = 0

        for point in points:
            sum_of_distances_to_points = sum_of_distances_to_points + manhattan_distance(point, evaluation_point)
        if sum_of_distances_to_points < 10000:
            safe_area += 1

print("The safe region is {} large".format(safe_area))