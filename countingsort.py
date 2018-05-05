def counting_sort(ar,n,d):
    sort=[0]*(d+1)
    for i in ar:
        sort[i]+=1
    j =0
    for i in range(d+1):
        while(sort[i]>0):
            ar[j]=i
            sort[i]=sort[i]-1
            j= j+1
    return ar

n = int(raw_input().strip())
d = int(raw_input().strip())
ar = map(int, raw_input().strip().split(' '))
ar = counting_sort(ar,n,d)
print ar
