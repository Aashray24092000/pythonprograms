class validateage(Exception):
    
    def __init__(self,msg):
        self.msg=msg
def validateage(age):
    if age<0:
        raise validateage("enterd age is negative")
    elif age>200:
        raise validateage("enter age is out of range")
    else:
        print("age is valid")
try:
    age=int(input("enter your age"))
    validateage(age)
except validateage as e:
    print(e)
