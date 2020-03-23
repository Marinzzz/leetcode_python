def test(n):
    print(n)
    yield n - 1
    print("nm")

a = test(10)
print(next(a))
#print(next(a))
