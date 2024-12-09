from collections import defaultdict
from copy import deepcopy
import math


with open("input.txt") as f:
    dm = f.read()

dm = [int(c) for c in dm]

blocks = []
id = 0
for i in range(len(dm)):
    if i%2:
        for j in range(dm[i]):
            blocks.append(".")
    else:
        for j in range(dm[i]):
            blocks.append(id)
        id+=1

def get_ptrs(block_map):
    n = len(block_map)
    lptr = block_map.index(".")
    rptr = n - 1
    for j in range(n):
        if block_map[n-1-j]!=".":
            rptr = n-1-j
            break

    return lptr, rptr

lptr, rptr = get_ptrs(blocks)
while lptr < rptr:
    blocks[lptr] = blocks[rptr]
    blocks[rptr] = "."
    lptr, rptr = get_ptrs(blocks)

s=0
for j in range(len(blocks)):
    if blocks[j] == ".":
        break
    s+=j*blocks[j]


print(f"Answer1: {s}")

# ==================

with open("input.txt") as f:
    dm = f.read()

dm = [int(c) for c in dm]

blocks = []
id = 0
ids_f = defaultdict(int)
ids = []
for i in range(len(dm)):
    if i%2:
        for j in range(dm[i]):
            blocks.append(".")
    else:
        ids.append(id)
        for j in range(dm[i]):
            blocks.append(id)
        ids_f[id]=dm[i]
        id+=1

ptr = len(ids)-1
while ptr>0:
    cur_val = ids[ptr]
    if ids_f[cur_val]==0:
        continue

    fd = blocks.index(".")
    cur_val_idx = blocks.index(cur_val)

    for j in range(fd, len(blocks)):
        clen = 0
        st_idx = j
        while(j < cur_val_idx and blocks[j]=="."):
            clen+=1
            j+=1
        if clen >= ids_f[cur_val]:
            for k in range(ids_f[cur_val]):
                blocks[st_idx+k] = blocks[cur_val_idx+k]
                blocks[cur_val_idx+k] = "."
            break

    ptr-=1

s=0
for j in range(len(blocks)):
    if blocks[j] == ".":
        continue
    s+=j*blocks[j]


print(f"Answer1: {s}")