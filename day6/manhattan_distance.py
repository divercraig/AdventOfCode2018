from typing import Tuple


def manhattan_distance(point_1: Tuple[int, int], point_2: Tuple[int, int]):
    distance = 0
    x1 = point_1[0]
    x2 = point_2[0]

    y1 = point_1[1]
    y2 = point_2[1]

    if x1 > x2:
        distance = distance + (x1 - x2)
    else:
        distance = distance + (x2 - x1)

    if y1 > y2:
        distance = distance + (y1 - y2)
    else:
        distance = distance + (y2 - y1)

    return distance