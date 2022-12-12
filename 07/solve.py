from functools import cache
from collections import deque


class aoc_file:
    def __init__(self, name, size):
        self.name = name
        self._size = size

    def size(self):
        return self._size
    
    def print(self, indent=0):
        print(f"{indent * ' '}{self.name}: {self._size}")

class aoc_dir: 
    def __init__(self, name, parent):
        self.name = name
        self.children = {}
        self.parent = parent
        self._size = 0
    
    def append(self, name, child):
        self.children[name] = child

    def size(self):
        self._size = sum([c.size() for c in self.children.values()])
        return self._size

    def print(self, indent=0):
        print(f"{indent * ' '}{self.name} +")
        for c in self.children.values():
            c.print(indent=indent + 2)


@cache
def _get_lines(input_file):
    with open(input_file, "r") as f:
        return f.readlines()
        

@cache 
def _get_input(input_file):
    lines = _get_lines(input_file)
    i = 1
    tree = aoc_dir("/", None)
    current_location = tree
    while i < len(lines):
        line = lines[i].split()
        if line[0] == "$":
            if line[1] == "cd":
                if line[2] == "..":
                    current_location = current_location.parent
                    i += 1 
                else: 
                    current_location = current_location.children[line[2]]
                    i += 1
            elif line[1] == "ls":
                i += 1
                while i < len(lines):
                    line = lines[i].split()
                    if line[0] == "dir":
                        current_location.append(line[1], aoc_dir(line[1], current_location))
                        i += 1
                    elif line[0] == "$":
                        break
                    else: 
                        current_location.append(line[1], aoc_file(line[1], int(line[0])))
                        i += 1
            else: 
                raise Exception("unknown command")
        else: 
            raise Exception("unknown line")
    
    tree.print()
    tree.size()

    return tree


def part_1(input_file):
    tree = _get_input(input_file)

    stack = deque([tree])
    total = 0
    while stack:
        f = stack.pop()
        if isinstance(f, aoc_file):
            continue
        if f._size <= 100000:
            print(f.name, f._size)
            total += f._size
        stack.extend(f.children.values())

    return total


def part_2(input_file):
    tree = _get_input(input_file)
    reqd = 30000000 - (70000000 - tree._size)
    smallest = tree._size

    stack = deque([tree])
    
    while stack:
        f = stack.pop()
        if isinstance(f, aoc_file):
            continue
        if f._size >= reqd:
            if f._size < smallest:
                print(f.name, f._size)
                smallest = f._size
        stack.extend(f.children.values())

    return smallest


if __name__=="__main__":
    # print(part_1("sample.txt"))
    # print(part_1("input.tx t"))
    print(part_2("sample.txt"))
    print(part_2("input.txt"))
