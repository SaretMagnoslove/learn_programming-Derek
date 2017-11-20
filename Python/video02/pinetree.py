hight = eval(input('how tall is the tree '))
spaces = hight 
hashes = -1
for raw in range(1,hight+1):
    spaces -= 1
    hashes +=2
    print(' ' * spaces, end="")
    print('#' * hashes)
print(' ' * (hight-1),end='')
print('#')