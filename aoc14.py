from collections import defaultdict
from copy import deepcopy
import math

robots = []
with open("input.txt") as f:
    for li in f.readlines():
        row = li.strip()
        bot = {}
        px, py = row.split(" ")[0].split("=")[1].split(",")
        vx, vy = row.split(" ")[1].split("=")[1].split(",")

        bot["pos"] = (int(px), int(py))
        bot["vel"] = (int(vx), int(vy))
        robots.append(bot)

h, w = 103, 101
# h, w = 7, 11
ts = 100

for i in range(ts):
    for bot in robots:
        pos = bot["pos"]
        vel = bot["vel"]
        px=(pos[0]+vel[0])%w
        py=(pos[1]+vel[1])%h
        bot["pos"] = (px,py)

qx = (w-1)//2
qy = (h-1)//2

quads = [0]*4
for bot in robots:
    pos = bot["pos"]
    if pos[0]<qx and pos[1]<qy:
        quads[0]+=1
    if pos[0]>qx and pos[1]<qy:
        quads[1]+=1
    if pos[0]<qx and pos[1]>qy:
        quads[2]+=1
    if pos[0]>qx and pos[1]>qy:
        quads[3]+=1
s=1

for q in quads:
    s*=q
print(f"Answer1: {s}")

# ==================

robots = []
with open("input.txt") as f:
    for li in f.readlines():
        row = li.strip()
        bot = {}
        px, py = row.split(" ")[0].split("=")[1].split(",")
        vx, vy = row.split(" ")[1].split("=")[1].split(",")

        bot["pos"] = (int(px), int(py))
        bot["vel"] = (int(vx), int(vy))
        robots.append(bot)

h, w = 103, 101
# h, w = 7, 11
ts = 100

def show_line(w):
    for i in range(w+2):
        print("-", end="")
    print()

def show_grid(robots, h, w):
    grid = []
    for i in range(h):
        l=[]
        for j in range(w):
            l.append(0)
        grid.append(l)

    for bot in robots:
        pos = bot["pos"]
        grid[pos[1]][pos[0]] = 1

    show_line(w)
    for i in range(h):
        print("|", end="")
        for j in range(w):
            if grid[i][j]==1:
                print('*', end='')
            else:
                print(' ', end='')
        print("|", end="")
        print()
    show_line(w)

ts=10000
for i in range(ts):
    if i >= 5000:
        print(f"Seconds: {i}")
        show_grid(robots, h, w)
        s = input()

    for bot in robots:
        pos = bot["pos"]
        vel = bot["vel"]
        px=(pos[0]+vel[0])%w
        py=(pos[1]+vel[1])%h
        bot["pos"] = (px,py)
