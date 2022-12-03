from functools import cache

@cache
def _get_input(input_file):
    with open(input_file, "r") as f:
        output = [tuple(line.split()) for line in f.read().split("\n") if line != ""]
        return output

scores = {
        "A": 1,
        "B": 2,
        "C": 3,
}

to_defeat = {
    "A": "B",
    "B": "C",
    "C": "A",
}

defeated_by = {
    "B": "A",
    "C": "B",
    "A": "C",
}

p1_transform = {
    "X": "A",
    "Y": "B",
    "Z": "C",
}


@cache
def game_p1(pair):
    right = p1_transform[pair[1]]
    left = pair[0]
    score = 0
    if left == right:
        score = 3
    elif to_defeat[left] == right:
        score = 6
    score += scores[right]
    return score


@cache
def game_p2(pair):
    if pair[1] == "Z":
        return 6 + scores[to_defeat[pair[0]]]
    if pair[1] == "Y":
        return 3 + scores[pair[0]]
    if pair[1] == "X":
        return     scores[defeated_by[pair[0]]]


def part_1(input_file):
    games = _get_input(input_file)
    return sum([game_p1(g) for g in games])


def part_2(input_file):
    games = _get_input(input_file)
    return sum([game_p2(g) for g in games])


if __name__=="__main__":
    print(part_1("sample.txt"))
    print(part_1("input.txt"))
    print(part_2("sample.txt"))
    print(part_2("input.txt"))
