from collections import defaultdict
from sortedcontainers import SortedList

try:

    with open("input.txt", 'r') as f:
        lines = f.readlines()
    num1 = []
    num2 = defaultdict(int)
    for line in lines:
        nums = line.replace('\n', '').split('   ')
        num1.append(nums[0])
        num2[nums[1]] += 1
    sum = 0
    for i in range(len(num1)):
        sum += int(num1[i]) * num2[num1[i]]
    print(sum)
except:
    