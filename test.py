import bisect
n=map(int,raw_input().strip().split(' '))
k=int(raw_input().strip())
'''m=n[1:5]
bisect.insort(m,k)'''
n.remove(k)
bisect.insort(n,10)
print n
