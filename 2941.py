alp=['c=','c-','dz=','d-','lj','nj','s=','z=']
import sys
s=sys.stdin.readline().rstrip()
length=len(s)
for a in alp:
    if a in s:
        cnt=s.count(a)
        length-=cnt
print(length)