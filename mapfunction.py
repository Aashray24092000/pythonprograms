l=[1,2,3,4,5]
def test(l):
    l1=[]
    for i in l:
        l1.append(i**2)
    return l1 

#using map keyword

def sq(x):
    return x**2
list(map(sq,l))
