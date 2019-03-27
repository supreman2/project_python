def merge(a:list, b:list):
    c=[0]*(len(a)+len(b))
    i=k=n=0
    while i<len(a) and k<len(b):
        if a[i]<=b[k]:
            c[n]=a[i]; i+=1; n+=1
        else:
            c[n]=b[k]; k+=1; n+=1
    while i<len(a):
        c[n]=a[i]; i+=1; n+=1
    while k<len(b):
        c[n]=b[k]; k+=1; n+=1
    return c

def merge_sort(a:list):
    if len(a)<=1:
        return
    middle = len(a)//2
    L=[a[i] for i in range(0, middle)]
    R=[a[i] for i in range(middle, len(a))]
    print("***")
    print(L)
    print(R)
    merge_sort(L)
    merge_sort(R)
    print(L)
    print(R)
    c=merge(L,R)
    for i in range(len(a)):
        a[i]=c[i]

res = [4,2,3,5,1]
merge_sort(res)
print(res)
