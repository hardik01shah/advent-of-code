
t = 0
reports = []
with open("input.txt") as f:
    for li in f.readlines():
        t+=1
        nums = li.strip().split(' ')
        nums = [int(a) for a in nums]
        
        reports.append(nums)

print(f"Total reports: {t}")
s=0

for i in range(t):
    cur_report = reports[i]
    if len(cur_report) < 2:
        s+=1
        continue

    elif len(cur_report) == 2:
        s+=int(1<=abs(cur_report[1]-cur_report[0])<=3)
        continue


    flag = cur_report[1] > cur_report[0]
    val = True
    for j in range(0, len(cur_report)-1):
        diff = cur_report[j+1] - cur_report[j]
        if not (1<=abs(diff)<=3):
            val = False
            break
        if diff > 0 and not flag:
            val = False
            break
        if diff < 0 and flag:
            val = False
            break
    
    if val:
        s+=1

print(f"Answer1: {s}")

# ========================
def status(cur_report, diffs, mags, scs):
    print(cur_report)
    print(diffs)
    print(mags)
    print(scs)
    print()

t = 0
reports = []
with open("input.txt") as f:
    for li in f.readlines():
        t+=1
        nums = li.strip().split(' ')
        nums = [int(a) for a in nums]
        
        reports.append(nums)

print(f"Total reports: {t}")
s=0

def check_array_i(a, idx):
    orig = a.copy()
    if idx >= 0:
        a.pop(idx)
    diffs = []
    mags = []
    scs = []
    for j in range(len(a)-1):
        diff = a[j+1] - a[j]
        diffs.append(diff)
        mags.append(int(not (1<=abs(diff)<=3)))
        scs.append(int(diff > 0))
    
    magsum = sum(mags)
    scssum = sum(scs)

    # valid
    if magsum==0 and (scssum==0 or scssum==len(scs)):
        if not len(orig) == len(a):
            print(orig)
            status(a, diffs, mags, scs)
        return True
    else:
        return False
    
for i in range(t):
    cur_report = reports[i]    
    if check_array_i(cur_report.copy(), -1):
        s+=1
        continue
    for j in range(len(cur_report)):
        if check_array_i(cur_report.copy(), j):
            s+=1
            break
print(f"Answer2: {s}")

exit()

def check_idx(idx, diffs, mags, scs):
    if idx!=0 and 1<=abs(diffs[idx-1]+diffs[idx])<=3:
        flag = diffs[idx-1] > 0
        if not(flag ^ ((diffs[idx-1]+diffs[idx])>0)):
            return True
    if idx!=len(diffs)-1 and 1<=abs(diffs[idx]+diffs[idx+1])<=3:
        flag = diffs[idx+1] > 0
        if not(flag ^ ((diffs[idx]+diffs[idx+1])>0)):
            return True
        
for i in range(t):
    cur_report = reports[i]
    if len(cur_report) <= 2:
        s+=1
        continue

    diffs = []
    mags = []
    scs = []
    for j in range(len(cur_report)-1):
        diff = cur_report[j+1] - cur_report[j]
        diffs.append(diff)
        mags.append(int(not (1<=abs(diff)<=3)))
        scs.append(int(diff > 0))
    
    magsum = sum(mags)
    scssum = sum(scs)

    # already valid
    if magsum==0 and (scssum==0 or scssum==len(scs)):
        s+=1
        continue

    # one invalid
    idxm = None
    idxs0 = None
    idxs1 = None
    if magsum == 1:
        idxm = mags.index(1)
    elif magsum>1:
        # status(cur_report, diffs, mags, scs)
        continue
    
    if scssum == 1:
        idxs1 = scs.index(1)
        # status(cur_report, diffs, mags, scs)
        if len(scs) == 2:
            # status(cur_report, diffs, mags, scs)
            if scssum == len(scs)-1:
                idxs0 = scs.index(0)
    
    elif scssum == len(scs)-1:
        idxs0 = scs.index(0)

    else:
        if not ((scssum==0) or (scssum==len(scs))):
            continue

    # not possible to make safe
    if not((idxm is not None) or (idxs0 is not None) or (idxs1 is not None)):
        continue

    if idxm is not None:
        if idxs0 is not None:
            if idxm == idxs0:
                if check_idx(idxm, diffs, mags, scs):
                    s+=1
                    # status(cur_report, diffs, mags, scs)
                    continue
        elif idxs1 is not None:
            if idxm == idxs1:
                if check_idx(idxm, diffs, mags, scs):
                    s+=1
                    # status(cur_report, diffs, mags, scs)
                    continue
        else:
            if check_idx(idxm, diffs, mags, scs):
                s+=1
                # status(cur_report, diffs, mags, scs)
                continue
    else:
        if idxs0 is not None:
            if check_idx(idxs0, diffs, mags, scs):
                s+=1
                # status(cur_report, diffs, mags, scs)
                continue
        if idxs1 is not None:
            if check_idx(idxs1, diffs, mags, scs):
                s+=1
                status(cur_report, diffs, mags, scs)
                continue
print(f"Answer2: {s}")