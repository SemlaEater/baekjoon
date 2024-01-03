cnt=1
while True:
    l,p,v=map(int,input().split())
    if l==0 & p==0 & v==0:
        break
    else:       
        day=(v//p)*l
        day+=min((v%p),l)
        print("Case %d: %d" %(cnt, day))
        cnt+=1