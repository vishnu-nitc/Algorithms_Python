def partition(ar,p,r):
  x=ar[r]
  i=p-1
  for j in range(p,r):
    if (ar[j]<=x):
      i +=1
      l = ar[j]
      ar[j]=ar[i]
      ar[i]=l
  l = ar[r]
  ar[r]=ar[i+1]
  ar[i+1]=l
  return i+1
def quicksort(ar,p,r):
  if (p<r):
    q=partition(ar,p,r)
    quicksort(ar,p,q-1)
    quicksort(ar,q+1,r)
  return ar
def binarysearch(ar,strt,end,k):
    if(strt>end):
        return -1
    i = (strt+end)/2
    if(ar[i]== k):
        return i
    if (k<ar[i]):
        return binarysearch(ar,strt,i-1,k)
    return binarysearch(ar,i+1,end,k)

def bsearch(ar,k):
  return binarysearch(ar,0,len(ar)-1,k)
n = int(raw_input().strip())
k = int(raw_input().strip())
ar = map(int, raw_input().strip().split(' '))
ar=quicksort(ar,0,n-1)
print ar
key = bsearch(ar,k)
if (key<0):
  print "Not found"
else:
  print "Found in %d" %key
