def insertion_sort(ar,n):
    for i in range(1,n):
        j = i-1
        num=ar[i]
        while(j>=0 and ar[j]>num):
            ar[j+1]=ar[j]
            j = j-1
        ar[j+1]=num
    return ar
n = int(raw_input().strip())
ar = map(int, raw_input().strip().split(' '))
ar = insertion_sort(ar,n)
print ar
