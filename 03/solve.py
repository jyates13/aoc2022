from functools import cache

@cache
def _get_input(input_file):
    with open(input_file, "r") as f:
        output = [line for line in f.read().split("\n") if line != ""]
        return output


@cache
def priority(letter):
    if ord(letter) < ord("a"):
        return ord(letter) - ord("A") + 27
    return ord(letter) - ord("a") + 1


def part_1(input_file):
    packs = _get_input(input_file)
    total = 0
    for pack in packs: 
        size = len(pack)//2
        letter = (set(pack[:size]) & set(pack[size:])).pop()
        total += priority(letter)
    return total

def part_2(input_file):
    packs = _get_input(input_file)
    total = 0
    packset = 0
    while packset < len(packs):
        pa, pb, pc = packs[packset:packset+3]
        letter = (set(pa) & set(pb) & set(pc)).pop()
        packset += 3
        total += priority(letter)
    return total


if __name__=="__main__":
    print(part_1("sample.txt"))
    print(part_1("input.txt"))
    print(part_2("sample.txt"))
    print(part_2("input.txt"))
