from functools import cache
import numpy as np
from collections import deque
import matplotlib.pyplot as plt

np.set_printoptions(threshold=np.inf)


@cache
def _get_input(input_file):
    start = None
    end   = None
    output = []
    with open(input_file, "r") as f:
        for i, line in enumerate(f.readlines()):
            if line.strip() == "": 
                continue

            height = lambda o: ord(o) - ord("a")

            l = list(map(height, line.strip()))
            for j, val in enumerate(l): 
                if val == height("S"): 
                    l[j] = height("a")
                    start = i, j
                elif val == height("E"):
                    l[j] = height("z")
                    end = i, j
            output.append(l)
    return start, end, np.array(output)


def part_1(input_file):
    start, end, heightmap = _get_input(input_file)
    
    costs = {start: 0}
    parents = {}
    unvisited = [start]

    while unvisited: 
        node = unvisited.pop()
        cost = costs[node]
        print(f"({node[0]:4}, {node[1]:4}): {cost}, {heightmap[node]}")

        if node == end: 
            break
        
        x, y = node
        for dx, dy in (0, 1), (1, 0), (0, -1), (-1, 0):
            neighbour = (x + dx, y + dy)
            if neighbour[0] < 0 or neighbour[1] < 0: 
                continue 
            try: 
                height = heightmap[neighbour]
            except IndexError:
                continue

            if height - heightmap[node] > 1:
                continue
            
            if neighbour in costs: 
                if costs[neighbour] < cost + 1: 
                    continue 
            else: 
                unvisited.append(neighbour)

            costs[neighbour] = cost + 1
            parents[neighbour] = node
        
        unvisited = sorted(unvisited, key=lambda n: costs[n], reverse=True)

    return cost

def part_2(input_file):
    start, end, heightmap = _get_input(input_file)
    
    costs = {end: 0}
    parents = {}
    unvisited = [end]

    while unvisited: 
        node = unvisited.pop()
        cost = costs[node]
        print(f"({node[0]:4}, {node[1]:4}): {cost}, {heightmap[node]}")

        if heightmap[node] == 0: 
            break
        
        x, y = node
        for dx, dy in (0, 1), (1, 0), (0, -1), (-1, 0):
            neighbour = (x + dx, y + dy)
            if neighbour[0] < 0 or neighbour[1] < 0: 
                continue 
            try: 
                height = heightmap[neighbour]
            except IndexError:
                continue

            if height - heightmap[node] < -1:
                continue
            
            if neighbour in costs: 
                if costs[neighbour] < cost + 1: 
                    continue 
            else: 
                unvisited.append(neighbour)

            costs[neighbour] = cost + 1
            parents[neighbour] = node
        
        unvisited = sorted(unvisited, key=lambda n: costs[n], reverse=True)

    return cost


if __name__=="__main__":
    # print(part_1("sample.txt"))
    # print(part_1("input.txt"))
    print(part_2("sample.txt"))
    print(part_2("input.txt"))
