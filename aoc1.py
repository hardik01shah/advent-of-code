
t = 0
l = []
r = []
with open("input.txt") as f:
    for li in f.readlines():
        t+=1
        a, b = li.strip().split("  ")
        a = int(a)
        b = int(b)

        l.append(a)
        r.append(b)

l.sort()
r.sort()

s = 0
for i in range(t):
    s+=abs(l[i]-r[i])


print(f"Answer1: {s}")
# ==================================


from collections import defaultdict
t = 0
l = defaultdict(int)
r = defaultdict(int)
with open("input.txt") as f:
    for li in f.readlines():
        t+=1
        a, b = li.strip().split("  ")
        a = int(a)
        b = int(b)

        l[a]+=1
        r[b]+=1

s = 0
for k in l.keys():
    s+=k*l[k]*r[k]


print(f"Answer2: {s}")