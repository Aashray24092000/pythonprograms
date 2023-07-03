def fab():
    a,b=0,1
    while True:
        yield a
        a,b=b,a+b
fib=fab()
for i in range(10):
    print(next(fib))
