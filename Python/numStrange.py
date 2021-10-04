#Strange number: A number is considered as Strange if  and only if:
# -> X is devisible by len(X)
# ->  the number X/len(X), recursiveley strange
# e.g. in the range of[7,25] there are 10 such numbers They are 7 8 9 10 12 14 16 18 20 24

import heapq as hq
from collections import defaultdict
import bisect as bs

DMAX = 18

work = [(1,i) for i in range(10)]
# strange = defaultdict(set)
strange = set()
hq.heapify(work)

while work:
    d,n = hq.heappop(work)
    if d>DMAX: break
    # strange[d].add(n)
    strange.add(n)
    for k in range(max(2,d),DMAX+1): # exclude d=1 and n=0
        if len(str(n*k)) == k:
            hq.heappush(work,(k,n*k))

strange = sorted(strange)

def solve(a,b):
    return bs.bisect_right(strange,b) - bs.bisect_left(strange,a)
