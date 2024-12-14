from collections import defaultdict
from copy import deepcopy
import math

flag=0
s=0
ax, ay, bx, by = 0, 0, 0, 0
X, Y = 0, 0
with open("input.txt") as f:
    for li in f.readlines():
        row = li.strip()
        if flag%4==0:
            config = row.split(":")[1].strip().split(',')
            ax=int(config[0].split('+')[1])
            ay=int(config[1].split('+')[1])
        elif flag%4==1:
            config = row.split(":")[1].strip().split(',')
            bx=int(config[0].split('+')[1])
            by=int(config[1].split('+')[1])
        elif flag%4==2:
            config = row.split(":")[1].strip().split(',')
            X=int(config[0].split('=')[1])
            Y=int(config[1].split('=')[1])

            d = 0
            for i in range(1,101):
                for j in range(1,101):
                    curx = i*ax + j*bx
                    cury = i*ay + j*by
                    if curx==X and cury==Y:
                        s+=i*3+j
                        d=1
                        break
                if d:
                    break
        else:
            pass

        flag+=1

print(f"Answer1: {s}")

# ==================
s=0
ax, ay, bx, by = 0, 0, 0, 0
X, Y = 0, 0
with open("input.txt") as f:
    for flag, li in enumerate(f.readlines()):
        row = li.strip()
        if flag%4==0:
            config = row.split(":")[1].strip().split(',')
            ax=int(config[0].split('+')[1])
            ay=int(config[1].split('+')[1])
        elif flag%4==1:
            config = row.split(":")[1].strip().split(',')
            bx=int(config[0].split('+')[1])
            by=int(config[1].split('+')[1])
        elif flag%4==2:
            config = row.split(":")[1].strip().split(',')
            X=int(config[0].split('=')[1])
            Y=int(config[1].split('=')[1])

            X += 10000000000000
            Y += 10000000000000

            # determinant
            if ax*by - bx*ay ==0:
                continue
            
            beta = (ay*X - ax*Y) / (bx*ay - by*ax)
            alpha = (by*X - bx*Y) / (by*ax - bx*ay)
            if math.ceil(alpha) == math.floor(alpha) and alpha>0:
                if math.ceil(beta) == math.floor(beta) and beta>0:
                    s+=int(alpha)*3 + int(beta)
            
        else:
            pass


print(f"Answer2: {s}")
