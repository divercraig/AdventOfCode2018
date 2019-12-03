from day3.claim import Claim

claims = {}
seen_points = set()
duplicate_points = set()
claims_with_no_overlap = []

for line in open('input.txt'):
    claim = Claim(design=line)
    for point in claim.generate_points():
        if point in seen_points:
            duplicate_points.add(point)
        else:
            seen_points.add(point)

for line in open('input.txt'):
    claim = Claim(design=line)
    overlap = False

    for point in claim.generate_points():
        if point in duplicate_points:
            overlap = True
            break

    if not overlap:
        claims_with_no_overlap.append(claim.id)

print(claims_with_no_overlap)


