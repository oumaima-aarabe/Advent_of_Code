import re

with open("v", 'r') as file:
    content = file.read()
mul_matches = []
first = content.find("don't()")
if first != -1:
    mul_matches = re.findall(r"mul\(\d+,\d+\)", content[:first])

    content = content[first:]
    sections = re.findall(r'do\(\)(.*?)don\'t\(\)', content, re.DOTALL)

    d = content.rfind("do()")
    if d > content.rfind("don't()"):
        sections.append(content[d + 4:])

else : sections = [content]

# print(sections)
for section in sections:
    matches = re.findall(r'mul\(\d+,\d+\)', section)
    if matches : mul_matches.extend(matches)

total_sum = 0

#'mul(317,745)'
for element in mul_matches:
    element = element[4:-1]
    s = element.split(',')
    total_sum += int(s[0]) * int(s[1])
print(total_sum)

# 73096093
