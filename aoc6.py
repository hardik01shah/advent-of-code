from collections import defaultdict
from copy import deepcopy

vis = defaultdict(bool)
grid = []
with open("input.txt") as f:
    for li in f.readlines():
        row = li.strip()
        grid.append(row)

h = len(grid)
w = len(grid[0])
g_pos = None
# get start pos
for i in range(h):
    for j in range(w):
        if grid[i][j] == '^':
            g_pos = (i,j)
            break
    if g_pos:
        break

s = 0
dirs = [
    [-1,0],
    [0,1],
    [1,0],
    [0,-1]
]
cur_dir = 0
while 0<=g_pos[0]<h and 0<=g_pos[1]<w:
    if not vis[g_pos]:
        s+=1
    vis[g_pos]=True

    npx = g_pos[0] + dirs[cur_dir][0]
    npy = g_pos[1] + dirs[cur_dir][1]

    if not(0<=npx<h and 0<=npy<w):
        break

    if grid[npx][npy] == '#':
        cur_dir+=1
        cur_dir%=len(dirs)
    
        npx = g_pos[0] + dirs[cur_dir][0]
        npy = g_pos[1] + dirs[cur_dir][1]

    g_pos = (npx, npy)
    

print(f"Answer1: {s}")

# ==================

visdir = defaultdict(list)
grid = []
with open("input.txt") as f:
    for li in f.readlines():
        row = li.strip()
        grid.append(list(row))

h = len(grid)
w = len(grid[0])
g_pos = None
# get start pos
for i in range(h):
    for j in range(w):
        if grid[i][j] == '^':
            g_pos = (i,j)
            break
    if g_pos:
        break

s = 0
dirs = [
    [-1,0],
    [0,1],
    [1,0],
    [0,-1]
]

def check_loop(pos, dir, dirs, grid):
    vis = defaultdict(bool)
    visdir = defaultdict(list)

    h = len(grid)
    w = len(grid[0])

    while 0<=pos[0]<h and 0<=pos[1]<w:
        if vis[pos] and (dir in visdir[pos]):
            return True
        
        vis[pos] = True
        visdir[pos].append(dir)

        npx = pos[0] + dirs[dir][0]
        npy = pos[1] + dirs[dir][1]

        if not(0<=npx<h and 0<=npy<w):
            break

        if grid[npx][npy] == '#':
            dir+=1
            dir%=len(dirs)

            npx = pos[0]
            npy = pos[1]

        pos = (npx, npy)
    
    return False

def show(grid):
    print("===============")
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            print(grid[i][j], end="")
        print()

# print(check_loop(g_pos, 0, dirs, grid))
# exit()
cur_dir = 0
g_posb = (g_pos[0],g_pos[1])
counted = defaultdict(bool)
while 0<=g_pos[0]<h and 0<=g_pos[1]<w:

    npx = g_pos[0] + dirs[cur_dir][0]
    npy = g_pos[1] + dirs[cur_dir][1]

    if not(0<=npx<h and 0<=npy<w):
        break

    if grid[npx][npy] == '#':
        cur_dir+=1
        cur_dir%=len(dirs)
    
        npx = g_pos[0]
        npy = g_pos[1]

    elif not ((npx,npy) == g_posb):
        ppos = (g_posb[0], g_posb[1])
        dgrid = deepcopy(grid)
        dgrid[npx][npy] = '#'
        if not counted[(npx, npy)]:
            if check_loop(ppos, 0, dirs, dgrid):
                s+=1
                counted[(npx, npy)] = True

    g_pos = (npx, npy)

print(f"Answer2: {s}")
