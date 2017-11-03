double = (x*2 for x in range(50))

print(next(double))
print(next(double))
print(next(double))
print(next(double))

for num in double:
    print(num)