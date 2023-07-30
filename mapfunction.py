l=[1,2,3,4,5]
def test(l):
    l1=[]
    for i in l:
        l1.append(i**2)
    return l1 

#using map and lambda function

list(map(lambda x:x**2,l ))

#another code for map and lambda

l1=[1,2,3,4,5,6]
l2=[1,2,3,4,5,6]
list(map(lambda  x,y:x+y,l1,l2))
