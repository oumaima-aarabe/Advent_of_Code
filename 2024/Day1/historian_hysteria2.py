from collections import defaultdict
from sortedcontainers import SortedList
with open("lol.txt", 'r') as f:
    lines = f.readlines()
num1 = SortedList()
num2 = SortedList()
for line in lines:
    nums = line.replace('\n', '').split('   ')
    num1.add(nums[0])
    num2.add(nums[1])
sum = 0
for i in range(len(num1)):
    sum += abs(int(num1[i]) - int(num2[i]))
print(sum)


