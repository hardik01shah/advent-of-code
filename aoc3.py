import re

with open("input.txt") as f:
    str = f.read()

muls = re.findall('mul\(\d{1,3},\d{1,3}\)', str)
s = 0

for expr in muls:
    o = expr.index('(')
    cl = expr.index(')')
    
    nums = expr[o+1:cl].split(',')
    assert len(nums) == 2

    s += int(nums[0]) * int(nums[1])

print(f"Answer1: {s}")

# =========================

def get_muls(str):
    muls = re.findall('mul\(\d{1,3},\d{1,3}\)', str)
    s = 0

    for expr in muls:
        o = expr.index('(')
        cl = expr.index(')')
        
        nums = expr[o+1:cl].split(',')
        assert len(nums) == 2

        s += int(nums[0]) * int(nums[1])

    return s

do_idx = [m.start(0) for m in re.finditer("do\(\)", str)]
dont_idx = [m.start(0) for m in re.finditer("don't\(\)", str)]
do_idx.sort()
dont_idx.sort()

do_idx = [0] + do_idx
dont_idx = dont_idx + [len(str)]

i = 0
j = 0
s = 0
while i < len(do_idx) and j < len(dont_idx):
    s+=get_muls(str[do_idx[i]: dont_idx[j]])

    while i < len(do_idx) and do_idx[i]<dont_idx[j]:
        i+=1
    j+=1
    while j < len(dont_idx) and do_idx[i]>dont_idx[j]:
        j+=1


print(f"Answer2: {s}")