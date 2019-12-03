class Claim:
    def __init__(self, design: str):
        parts = design.split(' ')
        self.id = int(parts[0][1:])

        start_location = parts[2][0:-1]
        self.left_edge = int(start_location.split(',')[0])
        self.top_edge = int(start_location.split(',')[1])

        size = parts[3]
        self.width = int(size.split('x')[0])
        self.height = int(size.split('x')[1])

    def generate_points(self):
        points = []
        for x in range(self.left_edge, self.left_edge + self.width):
            for y in range(self.top_edge, self.top_edge + self.height):
                points.append((x, y))

        return points

