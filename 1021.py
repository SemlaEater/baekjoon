from collections import deque
import sys
n,m=map(int,sys.stdin.readline().rstrip().split(" "))
dq=deque()
for i in range(n):
    dq.append(i+1)
wish=list(map(int,sys.stdin.readline().rstrip().split(" ")))
cnt=0
for w in wish:
    while True:
        if dq[0]==w:
            dq.popleft()
            break
        else:
            if dq.index(w)<len(dq)/2:
                while dq[0]!=w:
                    dq.append(dq.popleft())
                    cnt+=1
            else:
                while dq[0]!=w:
                    dq.appendleft(dq.pop())
                    cnt+=1
print(cnt)