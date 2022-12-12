from functools import cache
import re

@cache
def _get_input(input_file):
    with open(input_file, "r") as f:
        stacklines, movelines = f.read().split("\n\n")

        stacks = []
        for line in stacklines.split("\n")[::-1]: 
            if line == "": 
                continue

            if re.match("(\s[0-9])+", line):
                last = int(line.split()[-1])
                stacks = [[] for i in range(last)]
                continue

            for i in range(0, (len(line) + 1)//4):
                stack = line[4*i:4*i+4]
                if stack.strip() != "":
                    stacks[i].append(stack.strip(" []"))

        moves = [list(map(int, re.findall("[0-9]+", line))) for line in movelines.split("\n") if line.strip() != ""]

        return stacks, moves


def part(input_file, move_func):
    print("-----")
    stacks, moves = _get_input(input_file)
    [print(stack) for stack in stacks]
    print("-->")

    for move in moves:
        move_func(stacks, move)
    
    [print(stack) for stack in stacks]
    return "".join(stack[-1] for stack in stacks if stack)


def part_1(input_file):
    def move_func(stacks, move):
        count, source, dest = move
        movestack = stacks[source - 1][-1:-count-1:-1]
        del stacks[source -1][-1:-count-1:-1]
        stacks[dest - 1].extend(movestack)    
    
    return part(input_file, move_func)


def part_2(input_file):
    def move_func(stacks, move):
        count, source, dest = move
        movestack = stacks[source - 1][-count:]
        del stacks[source -1][-count:]
        stacks[dest - 1].extend(movestack)
    
    return part(input_file, move_func)


if __name__=="__main__":
    # print(part_1("sample.txt"))
    # print(part_1("input.txt"))
    print(part_2("sample.txt"))
    print(part_2("input.txt"))
