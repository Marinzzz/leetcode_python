intervals = [[1,5]]
newInterval = [5,7]
flag = 1
for i in intervals:
    if i[1] > newInterval[0]:
        intervals.insert(intervals.index(i) + 1, newInterval)
        flag = 0
        break
if flag == 1:
    intervals.append(newInterval)
ret = []
if len(intervals) == 0:
    ret.append(newInterval)
    print(ret)
ret.append(intervals[0])
for i in intervals[1:]:
    if i[0] > ret[-1][1]:
        ret.append(i)
        continue
    elif i[0] <= ret[-1][1]:
        if i[1] > ret[-1][1]:
            ret[-1][1] = i[1]
        else:
            continue
print(ret)