arr = []
with open("input.txt") as f:
    for li in f.readlines():
        nums = li.strip()
        arr.append(nums)

s = 0
dir_x = [-1, 0, 1]
dir_y = [-1, 0, 1]
for i in range(len(arr)):
    for j in range(len(arr[i])):
        
        for x in dir_x:
            for y in dir_y:
                if x == y == 0:
                    continue
                curs = ""
                for l in range(4):
                    if not(0 <= i + x*l < len(arr)):
                        continue
                    if not(0 <= j + y*l < len(arr[0])):
                        continue
                    curs += arr[i + x*l][j + y*l]
                if curs == "XMAS":
                    s+=1
print(f"Answer1: {s}")

# ==================
arr = []
with open("input.txt") as f:
    for li in f.readlines():
        nums = li.strip()
        arr.append(nums)

s = 0
vals = ["SM", "MS"]
for i in range(len(arr)):
    for j in range(len(arr[i])):
        
        if arr[i][j]!='A':
            continue
        if not(0 <= i-1 < len(arr)) or not(0 <= i+1 < len(arr)):
            continue
        if not(0 <= j-1 < len(arr[i])) or not(0 <= j+1 < len(arr[i])):
            continue
        d1, d2 = "", ""
        d1 += arr[i-1][j-1]
        d1 += arr[i+1][j+1]
        d2 += arr[i-1][j+1]
        d2 += arr[i+1][j-1]

        if d1 in vals and d2 in vals:
            s+=1

print(f"Answer2: {s}")