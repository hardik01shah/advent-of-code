from collections import defaultdict
from copy import deepcopy
import math

s = defaultdict(int)
antennas = defaultdict(list)
grid = []
with open("input.txt") as f:
    for li in f.readlines():
        row = li.strip()
        grid.append(row)

h = len(grid)
w = len(grid[0])

for i in range(h):
    for j in range(w):
        if grid[i][j]!='.':
            antennas[grid[i][j]].append((i,j))

for an, locs in antennas.items():
    for i in range(len(locs)):
        for j in range(len(locs)):
            if i==j:
                continue
            pos1 = locs[i]
            pos2 = locs[j]

            offsetx = pos1[0]-pos2[0]
            offsety = pos1[1]-pos2[1]
            nposx = pos1[0] + offsetx
            nposy = pos1[1] + offsety

            if not(0<=nposx<h and 0<=nposy<w):
                continue
            s[(nposx,nposy)]+=1

print(f"Answer1: {len(list(s.keys()))}")

# ==================


s = defaultdict(int)
antennas = defaultdict(list)
grid = []
with open("input.txt") as f:
    for li in f.readlines():
        row = li.strip()
        grid.append(row)

h = len(grid)
w = len(grid[0])

for i in range(h):
    for j in range(w):
        if grid[i][j]!='.':
            antennas[grid[i][j]].append((i,j))

for an, locs in antennas.items():
    for i in range(len(locs)):
        for j in range(len(locs)):
            if i==j:
                continue
            pos1 = locs[i]
            pos2 = locs[j]

            nposx = pos1[0]
            nposy = pos1[1]
            offsetx = pos1[0]-pos2[0]
            offsety = pos1[1]-pos2[1]

            m=0
            while (0<=nposx<h and 0<=nposy<w):
                
                nposx = pos1[0] + m*offsetx
                nposy = pos1[1] + m*offsety

                if not(0<=nposx<h and 0<=nposy<w):
                    break
                s[(nposx,nposy)]+=1
                m+=1

print(f"Answer2: {len(list(s.keys()))}")
