from collections import defaultdict
from copy import deepcopy
import heapq

def validate_pos(pos, grid, h, w):
    if (0<=pos[0]<h and 0<=pos[1]<w) and grid[pos[0]][pos[1]]!='#':
        return True
    else:
        return False
    
def get_neighs(cur_node, grid, h, w):
    neighs = []
    i, j, dir = cur_node
    for d in range(1,4):
        new_dir = (dir+d)%4
        neighs.append(((i,j,new_dir), 1000))

    if dir==0 and validate_pos((i,j+1), grid, h, w):
        neighs.append(((i,j+1,dir), 1))
    
    if dir==1 and validate_pos((i-1,j), grid, h, w):
        neighs.append(((i-1,j,dir), 1))

    if dir==2 and validate_pos((i,j-1), grid, h, w):
        neighs.append(((i,j-1,dir), 1))

    if dir==3 and validate_pos((i+1,j), grid, h, w):
        neighs.append(((i+1,j,dir), 1))

    return neighs

grid = []

with open("input.txt") as f:
    for line in f.readlines():
        grid.append(list(line.strip()))

h, w = len(grid), len(grid[0])
cur_pos = (h-2, 1, 0)   # x,y,dir
goal_pos = (1, w-2)
    
assert grid[cur_pos[0]][cur_pos[1]] == 'S'
assert grid[goal_pos[0]][goal_pos[1]] == 'E'
pq = []
pq.append((0, cur_pos))
heapq.heapify(pq)

vis = defaultdict(bool)

s = 0
while len(pq)>0:
    score, cur_pos = heapq.heappop(pq)
    i,j,dir = cur_pos
    if vis[cur_pos]:
        continue
    vis[cur_pos] = True
    if (i,j) == goal_pos:
        s = score
        break

    for neigh, weight in get_neighs(cur_pos, grid, h, w):
        if vis[neigh]==False:
            heapq.heappush(pq, (score+weight, neigh))

print(f"Answer 1: {s}")
    
# ===========


def validate_pos(pos, grid, h, w):
    if (0<=pos[0]<h and 0<=pos[1]<w) and grid[pos[0]][pos[1]]!='#':
        return True
    else:
        return False
    
def get_neighs(cur_node, grid, h, w):
    neighs = []
    i, j, dir = cur_node
    for d in range(1,4):
        new_dir = (dir+d)%4
        neighs.append(((i,j,new_dir), 1000))

    if dir==0 and validate_pos((i,j+1), grid, h, w):
        neighs.append(((i,j+1,dir), 1))
    
    if dir==1 and validate_pos((i-1,j), grid, h, w):
        neighs.append(((i-1,j,dir), 1))

    if dir==2 and validate_pos((i,j-1), grid, h, w):
        neighs.append(((i,j-1,dir), 1))

    if dir==3 and validate_pos((i+1,j), grid, h, w):
        neighs.append(((i+1,j,dir), 1))

    return neighs

grid = []

with open("input.txt") as f:
    for line in f.readlines():
        grid.append(list(line.strip()))

h, w = len(grid), len(grid[0])
cur_pos = (h-2, 1, 0)   # x,y,dir
goal_pos = (1, w-2)
    
assert grid[cur_pos[0]][cur_pos[1]] == 'S'
assert grid[goal_pos[0]][goal_pos[1]] == 'E'
pq = []
pq.append((0, cur_pos, []))
heapq.heapify(pq)

vis = defaultdict(bool)
score_reach = defaultdict(int)
best_nodes = set()

s = 0
while len(pq)>0:

    score, cur_pos, history = heapq.heappop(pq)
    i,j,dir = cur_pos

    if vis[cur_pos] and score > score_reach[cur_pos]:
        continue

    vis[cur_pos] = True
    score_reach[cur_pos] = score

    if (i,j) == goal_pos:
        for node in history:
            best_nodes.add(node)

    for neigh, weight in get_neighs(cur_pos, grid, h, w):
        if vis[neigh]==False or score_reach[neigh]==score+weight:
            new_history = history + [(neigh[0], neigh[1])]
            heapq.heappush(pq, (score+weight, neigh, new_history))

s = len(best_nodes)
print(f"Answer 2: {s}")
