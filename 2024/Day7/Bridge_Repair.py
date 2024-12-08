# 3267: [81 40 27]
from itertools import product

dic = {}
def bridge_repair(value, L) :
    operators_needed = len(L) - 1
    number_of_operators = 2**operators_needed
    operators = [0, 1]
    if number_of_operators not in dic:
        dic[number_of_operators] = list(product(operators, repeat=operators_needed))
    options = dic[number_of_operators]
    if value < sum(L): 
        return [0, 1]
    res = 1
    for e in L:
        res = res * e
    if value > res: return [0, 1]
    for option in options:
        solution = L[0]
        for i in range(1, len(L)):
            if not option[i - 1]:
                solution += L[i]
            else:  solution *= L[i]
        if solution == value:
            return [value, 0]
    return [0, 0]


with open("input.txt", 'r') as file:
    lines = file.readlines()

summ = 0
b = 0
for line in lines:
    value_str, list_str = line.split(": ")
    s = bridge_repair(int(value_str), list(map(int, list_str.split())))
    summ += s[0]
    b += s[1]
print(summ, b)
