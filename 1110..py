n=int(input())
k=n
cnt=0
while True:
    ten=n//10
    one=int(n%10)
    n=one*10+int((ten+one)%10)
    cnt+=1
    if n==k:
        break
print(cnt)
