def solve_add(equation):
    print(equation)
    var_list = equation.split()
    var1,var2 = int(var_list[2]),int(var_list[4])
    return 'x = ' + str(var2-var1)

print(solve_add('x + 10 = 5'))


