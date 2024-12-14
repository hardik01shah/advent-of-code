from collections import defaultdict
from copy import deepcopy
import math


stones = []
with open("input.txt") as f:
    li = f.read().strip().split(" ")
    stones = [int(n) for n in li]

blinks = 25
n_stones = []
for i in range(blinks):
    for j in range(len(stones)):
        if stones[j]==0:
            n_stones.append(1)
        elif (len(str(stones[j]))%2) == 0:
            digs = str(stones[j])
            n_stones.append(int(digs[:len(digs)//2]))
            n_stones.append(int(digs[len(digs)//2:]))
        else:
            n_stones.append(stones[j]*2024)

    stones = n_stones
    n_stones = []

print(f"Answer1: {len(stones)}")

# ==================

stones = []
with open("input.txt") as f:
    li = f.read().strip().split(" ")
    stones = [int(n) for n in li]

total_blinks = 75

s = 0
freqs = {}

def get_stones(freqs, cur_stone, blinks):
    if blinks == 0:
        return 1
    
    if (cur_stone, blinks) in freqs:
        return freqs[(cur_stone, blinks)]

    if cur_stone==0:
        cur_s = get_stones(freqs, 1, blinks-1)
    elif (len(str(cur_stone))%2) == 0:
        digs = str(cur_stone)
        ns1 = int(digs[:len(digs)//2])
        ns2 = int(digs[len(digs)//2:])

        cur_s = get_stones(freqs, ns1, blinks-1) + get_stones(freqs, ns2, blinks-1)
    else:
        cur_s = get_stones(freqs, cur_stone*2024, blinks-1)
    freqs[(cur_stone, blinks)] = cur_s
    return cur_s

s = 0
for j in range(len(stones)):
    s += get_stones(freqs, stones[j], total_blinks)

print(f"Answer2: {s}")