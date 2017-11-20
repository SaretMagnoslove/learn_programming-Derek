print(list(map((lambda x: x * 2), range(1, 11))))
print([x * 2 for x in range(1, 11)])

print(list(filter((lambda x: x % 2 != 0), range(1, 11))))
print([x for x in range(1, 11) if x % 2 != 0])

# generate 50 values raise to the power of 2 and print muliples of 8
print([x**2 for x in range(1, 50) if x % 8 == 0])
# multiple two lists
print([x * y for x in range(1, 3) for y in range(11, 16)])
# generate 10 number multiple by 2 and print multiple of 8
print([x for x in[ii * 2 for ii in range(10) if x % 8 == 0]])
