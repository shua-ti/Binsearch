#-*-coding=utf-8-*-
#/usr/bin/env python
"²éÕÒÓÒ¼ä¸ô"
import bisect

intervals=[[3,4],[2,3],[1,1.2]]


def findRightInterval(intervals):
    intvl = sorted([(x[0], i) for i, x in enumerate(intervals)], key=lambda x: x[0])
    starts, idx = [x[0] for x in intvl], [x[1] for x in intvl]
    res = []
    for x in intervals:
       pos = bisect.bisect_left(starts, x[1])#start[pos]>=x[1]
       print pos,
       if pos == len(starts):
           res.append(-1)
       else:
           res.append(idx[pos])
    return res

if __name__=="__main__":
    print findRightInterval(intervals)
