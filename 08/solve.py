from functools import cache
from collections import deque
import numpy as np


@cache 
def _get_input(input_file):
    with open(input_file, "r") as f:
        return np.array([list(map(int, line.strip())) for line in f.readlines() if line.strip() != ""])



def part_1(input_file):
    tree = _get_input(input_file)
    seen = np.zeros_like(tree)

    nothing   = lambda t: t
    reverse   = lambda t: t[::-1]
    transpose = lambda t: t.transpose()
    ops = deque([reverse, transpose, reverse, nothing])

    while ops:
        op = ops.pop()
        tree = op(tree)
        seen = op(seen)
        print(tree)

        for col in range(tree.shape[1]):
            index = 0
            seen[index, col] = 1
            current = tree[index, col]
            for index in range(1, tree.shape[0]):
                if tree[index, col] > current: 
                    seen[index, col] = 1
                    current = tree[index, col]
        print(seen)
        print("===")
    
    return np.sum(seen)


def part_2(input_file):
    tree = _get_input(input_file)
    seen = np.zeros_like(tree)
    best = 0
    print(tree)

    for i in range(1, tree.shape[1] - 1):
        for j in range(1, tree.shape[0] - 1):
            stop = tree[i,j]
            
            # print(f"{i}, {j}: ", end="")
            dirs = [0, 0, 0, 0]
            los = [tree[i+1::1,j], 
                   tree[i-1::-1,j],
                   tree[i,j+1::1],
                   tree[i,j-1::-1]]

            for d in range(len(dirs)):
                curr = -1
                for t in los[d]:
                    dirs[d] += 1
                    if t >= stop: 
                        break

            # print(dirs)
            
            b = np.product(dirs)
            seen[i,j] = b
            if b > best: 
                best = b

    print(seen)
    return best

if __name__=="__main__":
    # print(part_1("sample.txt"))
    # print(part_1("input.txt"))
    print(part_2("sample.txt"))
    print(part_2("input.txt"))
