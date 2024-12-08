# 3267: [81 40 27]
from itertools import product

dic = {}
def bridge_repair(value, L) :
    operators_needed = len(L) - 1
    number_of_operators = 2**operators_needed
    operators = [0, 1, 2]
    if number_of_operators not in dic:
        dic[number_of_operators] = list(product(operators, repeat=operators_needed))
    options = dic[number_of_operators]
    if value < sum(L): return 0
    s = ''
    for e in L:
        s = s + str(e)
    if int(s) < value: 
        return 0
    for option in options:
        solution = L[0]
        for i in range(1, len(L)):
            if not option[i - 1]:
                solution += L[i]
            elif  option[i - 1] == 1 : solution *= L[i]
            else:
                solution = int(str(solution) + str(L[i]))
        if solution == value:
            return value
    return 0


with open("input.txt", 'r') as file:
    lines = file.readlines()

summ = 0
for line in lines:
    value_str, list_str = line.split(": ")
    summ += bridge_repair(int(value_str), list(map(int, list_str.split())))
print(summ)
