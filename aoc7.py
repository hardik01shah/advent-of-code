from collections import defaultdict
from copy import deepcopy
import math

s = 0
with open("input.txt") as f:
    for li in f.readlines():
        alln = li.strip().split(':')
        target = int(alln[0])
        nums = alln[1].strip().split(" ")

        vals = [int(n) for n in nums]

        num_v = len(vals)
        num_o = num_v - 1
        pos_seq = 2**num_o
        for i in range(pos_seq):
            binn = i
            bits = []
            while binn>0:
                bits.append(binn%2)
                binn = binn//2
            bits.reverse()
            bits = [0]*(num_o - len(bits)) + bits

            curp = vals[0]
            for i in range(len(bits)):
                if bits[i] == 0:
                    curp+=vals[i+1]
                else:
                    curp*=vals[i+1]
            if curp == target:
                s+=target
                break
print(f"Answer1: {s}")

# ==================

def get_num_digits(a):
    d = 0
    while(a>0):
        d+=1
        a=a//10
    return d

s = 0
with open("input.txt") as f:
    for li in f.readlines():
        alln = li.strip().split(':')
        target = int(alln[0])
        nums = alln[1].strip().split(" ")

        vals = [int(n) for n in nums]

        num_v = len(vals)
        num_o = num_v - 1
        pos_seq = 3**num_o

        for i in range(pos_seq):
            binn = i
            bits = []
            while binn>0:
                bits.append(binn%3)
                binn = binn//3
            bits.reverse()
            bits = [0]*(num_o - len(bits)) + bits

            curp = vals[0]
            assert len(bits) == len(vals)-1
            for i in range(len(bits)):
                if bits[i] == 0:
                    curp+=vals[i+1]
                elif bits[i] == 1:
                    curp*=vals[i+1]
                elif bits[i] == 2:
                    curp = int(f"{curp}{vals[i+1]}")

                if curp>target:
                    break

            if curp == target:
                s+=target
                break

print(f"Answer2: {s}")