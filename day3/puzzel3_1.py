from day3.claim import Claim

claims = {}
seen_points = set()
duplicate_points = set()

for line in open('input.txt'):
    claim = Claim(design=line)
    for point in claim.generate_points():
        if point in seen_points:
            duplicate_points.add(point)
        else:
            seen_points.add(point)

print("{} Square inches of fabric required by 2 or more claims".format(len(duplicate_points)))


