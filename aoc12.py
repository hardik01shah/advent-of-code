from collections import defaultdict
from copy import deepcopy
import math

grid = []
with open("input.txt") as f:
    for li in f.readlines():
        row = li.strip()
        grid.append(row)

areas = defaultdict(int)
positions = defaultdict(list)
h, w = len(grid), len(grid[0])
for i in range(h):
    for j in range(w):
        areas[grid[i][j]]+=1
        positions[grid[i][j]].append((i,j))

def get_neighs(i,j):
    neighs = []

    neighs.append((i+1,j))
    neighs.append((i,j+1))
    neighs.append((i-1,j))
    neighs.append((i,j-1))

    return neighs

def dfs(cur_node, grid, vis, a, p):
    if vis[cur_node]:
        return a, p

    vis[cur_node] = True
    a+=1
    i, j = cur_node
    neighs = get_neighs(i, j)

    for neigh in neighs:
        if not(0<=neigh[0]<h and 0<=neigh[1]<w):
            p+=1
        elif grid[neigh[0]][neigh[1]]!=plant:
            p+=1
        else:
            a, p = dfs(neigh, grid, vis, a, p)
    
    return a, p

s=0
for plant, pos_list in positions.items():
    
    vis = defaultdict(bool)
    for pos in pos_list:
        a, p = dfs(pos, grid, vis, 0, 0)
        s+=a*p
        # if a!=0:
        #     print(f"Plant: {plant}, perimeter: {p}, area: {a}")

print(f"Answer1: {s}")

# ==================


grid = []
with open("input.txt") as f:
    for li in f.readlines():
        row = li.strip()
        grid.append(row)

areas = defaultdict(int)
positions = defaultdict(list)
h, w = len(grid), len(grid[0])
for i in range(h):
    for j in range(w):
        areas[grid[i][j]]+=1
        positions[grid[i][j]].append((i,j))

def get_neighs(i,j):
    neighs = []

    neighs.append((i+1,j,0))
    neighs.append((i,j+1,1))
    neighs.append((i-1,j,2))
    neighs.append((i,j-1,3))

    return neighs

def dfs(cur_node, grid, vis, a, p):
    if vis[cur_node]:
        return a, p

    vis[cur_node] = True
    a+=1
    i, j = cur_node
    neighs = get_neighs(i, j)

    for neigh in neighs:
        if not(0<=neigh[0]<h and 0<=neigh[1]<w):
            p.append((i,j,neigh[2]))
        elif grid[neigh[0]][neigh[1]]!=plant:
            p.append((i,j,neigh[2]))
        else:
            a, p = dfs((neigh[0],neigh[1]), grid, vis, a, p)
    
    return a, p

s=0
for plant, pos_list in positions.items():
    
    vis = defaultdict(bool)
    for pos in pos_list:
        a, p = dfs(pos, grid, vis, 0, [])

        if a==0:
            continue

        f = 0
        per = len(p)
        while len(p)>0:
            cur_s = p[0]
            p.pop(0)
            i, j, dir = cur_s
            if (dir%2)==1:   
                it = 1 
                while (i+it,j,dir) in p:
                    p.remove((i+it,j,dir))
                    it+=1
                it = -1
                while (i+it,j,dir) in p:
                    p.remove((i+it,j,dir))
                    it-=1
            else:
                it = 1 
                while (i,j+it,dir) in p:
                    p.remove((i,j+it,dir))
                    it+=1
                it = -1
                while (i,j+it,dir) in p:
                    p.remove((i,j+it,dir))
                    it-=1
            f+=1
        s+=a*f
        # if a!=0:
        #     print(f"Plant: {plant}, sides: {f}, perimeter: {per}, area: {a}")

print(f"Answer2: {s}")
