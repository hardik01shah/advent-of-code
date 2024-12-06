from collections import defaultdict

ordering = defaultdict(list)
updates = []
br = False
with open("input.txt") as f:
    for li in f.readlines():
        if li == '\n':
            br = True
            continue
        if not br:
            nums = li.strip()
            nums = nums.split('|')
            ordering[int(nums[0])].append(int(nums[1]))

        else:
            nums = li.strip().split(',')
            update = [int(n) for n in nums]
            updates.append(update)

s = 0
for update in updates:
    val = True
    for i in range(len(update)):
        if update[i] in ordering:
            j = i-1
            while j >= 0:
                if update[j] in ordering[update[i]]:
                    val = False
                    break
                j-=1
        if not val:
            break
    if val:
        s+=update[len(update)//2]


print(f"Answer1: {s}")

# ==================
ordering = defaultdict(list)
updates = []
br = False
with open("input.txt") as f:
    for li in f.readlines():
        if li == '\n':
            br = True
            continue
        if not br:
            nums = li.strip()
            nums = nums.split('|')
            ordering[int(nums[0])].append(int(nums[1]))

        else:
            nums = li.strip().split(',')
            update = [int(n) for n in nums]
            updates.append(update)

s = 0
for update in updates:
    val = True
    for i in range(len(update)):
        if update[i] in ordering:
            j = i-1
            while j >= 0:
                if update[j] in ordering[update[i]]:
                    val = False
                    break
                j-=1
        if not val:
            break
    if val:
        continue

    nu = [update[0]]
    for i in range(1, len(update)):
        idx = 0
        cur = update[i]
        for j in range(len(nu)):
            if cur in ordering[nu[j]]:
                idx = j+1
        nu.insert(idx, cur)
    print()
    print(update)
    print(nu)
    s+=nu[len(nu)//2]



print(f"Answer2: {s}")