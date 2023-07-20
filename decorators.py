import time 

def timer_test(func):
    def timer():
        start=time.time()
        func()
        end=time.time()
        print(end-start)
        print("welcome baby")
    return timer
@timer_test
def test1():
    print(564+32)
    print(10*10)
test1()
