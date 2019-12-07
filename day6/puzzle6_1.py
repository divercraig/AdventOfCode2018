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

point_areas = {}

for x in range(lowest_x, highest_x + 1):
    for y in range(lowest_y, highest_y + 1):
        evaluation_point = (x, y)
        closest_danger = None
        closest_danger_distance = None

        for danger_point in points:
            distance = manhattan_distance(evaluation_point, danger_point)

            if closest_danger_distance is not None and distance == closest_danger_distance:
                closest_danger = None

            if closest_danger_distance is None or distance < closest_danger_distance:
                closest_danger = danger_point
                closest_danger_distance = distance

        if closest_danger is not None:
            if closest_danger in point_areas.keys():
                point_areas[closest_danger] = point_areas[closest_danger] + 1
            else:
                point_areas[closest_danger] = 1


largest_area = 0
for danger_point in point_areas.keys():
    area = point_areas[danger_point]
    if area > largest_area:
        largest_area = area


print("The largest area is {}".format(largest_area))


