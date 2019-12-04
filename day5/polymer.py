def unit_destruction(unit_1:str, unit_2:str):
    if (unit_1.isupper() != unit_2.isupper()) and (unit_1.upper() == unit_2.upper()):
        return True
    else:
        return False


def trigger_polymer(polymer:[str]):
    output_polymer = []
    reduced = False
    skip = False

    for i in range(0, len(polymer)-1):
        unit_1 = polymer[i]
        unit_2 = polymer[i+1]
        if skip:
            skip = False
        else:
            if unit_destruction(unit_1, unit_2):
                reduced = True
                skip = True
            else:
                output_polymer.append(unit_1)

    if not skip:
        output_polymer.append(polymer[-1])

    if not reduced:
        return output_polymer
    else:
        return trigger_polymer(output_polymer)