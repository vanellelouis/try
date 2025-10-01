
def divise(L):
    return (L[:len(L)//2],L[len(L)//2:])

def fusion(l1,l2):
    res=[]
    i1=0
    i2=0
    while i1<len(l1) and i2<len(l2):
        if l1[i1]<l2[i2]:
            res.append(l1[i1])
            i1+=1
        else:
            res.append(l2[i2])
            i2+=1
    for i in range(i1,len(l1)):
        res.append(l1[i])
    for i in range(i2,len(l2)):
        res.append(l2[i])
    return res

def tri_fusion(L):
    if len(L)<=1:
        return L
    (l1,l2)=divise(L)
    return fusion(tri_fusion(l1),tri_fusion(l2))


#print(tri_fusion([12,7,2,3,6,25,1,35,4,85,456,45]))
def recherche_dico(x,l):
    l=tri_fusion(l)
    g=0
    d=len(l)-1
    while d!=g:
        m=(g+d)//2
        if l[m]==x:
            return True
        elif l[m]<x:
            g=m+1
        else:
            d=m
    return False

print(recherche_dico(2,[20,13,1,5,45,48,89,8,68,468,68,2]))

def dyn_fibo(n):
    l=[0,1]
    while len(l)<=n:
        l.append(l[-1]+l[-2])
    return l[n]

def fibo_malin(n):
    l=[0,1]
    for i in range(2,n+1):
        l[i%2]=l[-1]+l[-2]
    return l[n%2]


print(dyn_fibo(300)==fibo_malin(300))


