import threading
def test(id):
    print("%d"%id)
thread=[threading.Thread(target=test,args=(i,)) for i in range(10)]
for t in thread:
    t.start()
