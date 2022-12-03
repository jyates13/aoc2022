def _get_input(input_file):
    with open(input_file, "r") as f:
        return [sum([int(l) for l in lines.split("\n") if l != ""]) for lines in f.read().split("\n\n")]


def part_1(input_file):
    return max(_get_input(input_file))


def part_2(input_file):
    return sum(sorted(_get_input(input_file))[-3:])


if __name__=="__main__":
    print(part_1("input.txt"))
    print(part_2("input.txt"))
