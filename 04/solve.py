from functools import cache

@cache
def _get_input(input_file):
    with open(input_file, "r") as f:
        output = [[list(map(int, pair.split("-"))) for pair in line.split(",")] for line in f.read().split("\n") if line != ""]
        return output


def part_1(input_file):
    assignments = _get_input(input_file)
    subsets = 0 
    for a in assignments: 
        if ((a[0][0] >= a[1][0]) and (a[0][1] <= a[1][1])):
            subsets += 1
            print(f"{a}: ({a[0][0]} >= {a[1][0]}) and ({a[0][1]} <= {a[1][1]}))")
        elif ((a[1][0] >= a[0][0]) and (a[1][1] <= a[0][1])):
            subsets += 1
            print(f"{a}: ({a[1][0]} >= {a[0][0]}) and ({a[1][1]} <= {a[0][1]}))")
    return subsets

def within_bound(a, ba, bb):
    return (a >= ba) and (a <= bb)

def part_2(input_file):
    assignments = _get_input(input_file)
    subsets = 0 
    for a in assignments: 
        if (within_bound(a[0][0], *a[1]) or \
            within_bound(a[0][1], *a[1]) or \
            within_bound(a[1][0], *a[0]) or \
            within_bound(a[1][1], *a[0])): 
            subsets += 1
    return subsets


if __name__=="__main__":
    # print(part_1("sample.txt"))
    # print(part_1("input.txt"))
    print(part_2("sample.txt"))
    print(part_2("input.txt"))
