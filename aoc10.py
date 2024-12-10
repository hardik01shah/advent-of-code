from collections import defaultdict
from copy import deepcopy
import math


grid = []
with open("input.txt") as f:
    for li in f.readlines():
        row = li.strip()
        grid.append([int(n) for n in row])

queue = []
h, w = len(grid), len(grid[0])
for i in range(h):
    for j in range(w):
        if grid[i][j]==0:
            queue.append([(0,(i,j))])

def get_neighs(i,j,h,w):
    neighs = []
    if 0<=i+1<h:
        neighs.append((i+1,j))
    if 0<=j+1<w:
        neighs.append((i,j+1))
    if 0<=i-1<h:
        neighs.append((i-1,j))
    if 0<=j-1<w:
        neighs.append((i,j-1))

    return neighs

trails = defaultdict(set)
s=0
while len(queue)>0:
    cur_path = queue.pop(0)
    cur_node = cur_path[-1][0]
    cur_pos = cur_path[-1][1]

    neighs = get_neighs(cur_pos[0], cur_pos[1], h, w)
    for neigh in neighs:
        if grid[neigh[0]][neigh[1]] == cur_node+1:
            if cur_node+1==9:
                trails[cur_path[0]].add(neigh)
                continue

            new_path = cur_path + [(cur_node+1, neigh)]
            queue.append(new_path)

for k, v in trails.items():
    s+=len(v)

print(f"Answer1: {s}")

# ==================

grid = []
with open("input.txt") as f:
    for li in f.readlines():
        row = li.strip()
        grid.append([int(n) for n in row])

queue = []
h, w = len(grid), len(grid[0])
for i in range(h):
    for j in range(w):
        if grid[i][j]==0:
            queue.append([(0,(i,j))])

def get_neighs(i,j,h,w):
    neighs = []
    if 0<=i+1<h:
        neighs.append((i+1,j))
    if 0<=j+1<w:
        neighs.append((i,j+1))
    if 0<=i-1<h:
        neighs.append((i-1,j))
    if 0<=j-1<w:
        neighs.append((i,j-1))

    return neighs

trails = defaultdict(dict)
s=0
while len(queue)>0:
    cur_path = queue.pop(0)
    cur_node = cur_path[-1][0]
    cur_pos = cur_path[-1][1]

    neighs = get_neighs(cur_pos[0], cur_pos[1], h, w)
    for neigh in neighs:
        if grid[neigh[0]][neigh[1]] == cur_node+1:
            if cur_node+1==9:
                s+=1
                continue

            new_path = cur_path + [(cur_node+1, neigh)]
            queue.append(new_path)

print(f"Answer2: {s}")
