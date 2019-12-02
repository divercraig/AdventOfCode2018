def compare_box_ids(box1:str, box2:str) -> bool:
    diffs = 0
    for i in range(0, len(box1)):
        if box1[i] != box2[i]:
            diffs += 1
            if diffs > 1:
                break

    if diffs == 1:
        return True

    return False


def matching_chars(box1:str, box2:str) -> str:
    matching = ''
    for c in range(0, len(box1)):
        if box1[c] == box2[c]:
            matching += box1[c]

    return matching


box_ids = []

for box_id in open('input.txt'):
    box_ids.append(box_id)

for i in range(0, len(box_ids)):
    for j in range(i+1, len(box_ids)):
        if compare_box_ids(box_ids[i], box_ids[j]):
            print("{} and {} are pretty close".format(box_ids[i], box_ids[j]))
            print("Matching chars are {}".format(matching_chars(box_ids[i], box_ids[j])))
