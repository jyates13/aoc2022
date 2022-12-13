from functools import cache


@cache
def _get_input(input_file):
    with open(input_file, "r") as f:
        return [line.split() for line in f.readlines() if line != ""]


def part_1(input_file):
    signals = _get_input(input_file)
    targets = [20, 60, 100, 140, 180, 220]
    
    cycle = 0
    x = 1

    total = 0 

    for s in signals: 
        if s[0] == "noop":
            cycle += 1
            if cycle in targets: 
                print(x, cycle)
                total += x * cycle 
        else:
            cycle += 1
            if cycle in targets: 
                print(x, cycle)
                total += x * cycle
            cycle += 1
            if cycle in targets: 
                print(x, cycle)
                total += x * cycle
            x += int(s[1])

    return total


def part_2(input_file):
    signals = _get_input(input_file)
    
    cycle = 1
    x = 1

    def do_cycle(cycle, x):
        if (cycle % 40) in (x, x+1, x+2):
            print("#", end="")
        else: 
            print(".", end="")
        if (cycle % 40 == 0): 
            print("")

    for s in signals: 
        do_cycle(cycle, x)
        cycle += 1

        if s[0] != "noop":
            do_cycle(cycle, x)
            cycle += 1
            x += int(s[1])
        
        # print(cycle, x)

    return ""


if __name__=="__main__":
    # print(part_1("sample.txt"))
    # print(part_1("input.txt"))
    print(part_2("sample.txt"))
    print(part_2("input.txt"))
