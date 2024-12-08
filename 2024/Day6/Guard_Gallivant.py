import re

with open("input.txt", 'r') as file:
    content = file.read()

first = content.find("don/'t()")
print(first)
# L = re.findall(r"mul\(\d+,\d+\)", content)
# total_sum = 0

# #'mul(317,745)'
# for element in L:
#     element = element[4:-1]
#     s = element.split(',')
#     total_sum += int(s[0]) * int(s[1])
# print(total_sum)
    