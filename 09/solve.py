from functools import cache
from collections import deque


class RopeHead:
    def __init__(self, position, tail=None):
        self.head = position
        if tail is None: 
            self.tail = RopeTail(position)
        else:
            self.tail = tail

    def move(self, move):
        if move == "U":
            x, y = self.head
            self.head = (x, y + 1)
        elif move == "L":
            x, y = self.head
            self.head = (x - 1, y)
        elif move == "D":
            x, y = self.head
            self.head = (x, y - 1)
        elif move == "R":
            x, y = self.head
            self.head = (x + 1, y)
        self.tail.move_head(self.head)
    
    def __str__(self):
        return f"{self.head}, {self.tail}"


class RopeTail: 
    def __init__(self, position, tail=None):
        self.head = position
        self.tail = tail
    
    def move_head(self, position):
        hx, hy = position
        x, y = self.head

        xd = hx - x
        yd = hy - y
        if (abs(xd * yd) > 1): 
            x += 1 if xd >= 1 else -1
            y += 1 if yd >= 1 else -1
        elif (abs(xd) > 1):
            x += 1 if xd >= 1 else -1
        elif (abs(yd) > 1):
            y += 1 if yd >= 1 else -1
        
        self.head = (x, y)

        if self.tail is not None:
            self.tail.move_head(self.head)

    def __str__(self):
        if self.tail is not None: 
            return f"{self.head}, {self.tail}"
        return f"{self.head}"
        


@cache
def _get_input(input_file):
    with open(input_file, "r") as f:
        return [l.split() for l in f.readlines() if l.strip != ""]


def part_1(input_file):
    moves = _get_input(input_file)
    tail_visited = set()
    
    rope = RopeHead((0,0))

    for move in moves: 
        print(move)
        count = int(move[1])
        for _ in range(count):
            rope.move(move[0])
            print(rope)
            tail_visited.add(rope.tail.head)
    
    return len(tail_visited)


def part_2(input_file):
    moves = _get_input(input_file)
    tail_visited = set()
    
    t9 = RopeTail((0,0))
    t8 = RopeTail((0,0), t9)
    t7 = RopeTail((0,0), t8)
    t6 = RopeTail((0,0), t7)
    t5 = RopeTail((0,0), t6)
    t4 = RopeTail((0,0), t5)
    t3 = RopeTail((0,0), t4)
    t2 = RopeTail((0,0), t3)
    t1 = RopeTail((0,0), t2)
    h  = RopeHead((0,0), t1)

    for move in moves: 
        # print(move)
        count = int(move[1])
        for _ in range(count):
            h.move(move[0])
            # print(h)
            tail_visited.add(t9.head)
    
    return len(tail_visited)


if __name__=="__main__":
    # print(part_1("sample.txt"))
    # print(part_1("input.txt"))
    print(part_2("sample.txt"))
    print(part_2("sample2.txt"))
    print(part_2("input.txt"))
