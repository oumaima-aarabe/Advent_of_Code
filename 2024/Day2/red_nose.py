
with open("ext_poly.txt", 'r') as f:
    lines = f.readlines()

unsafe = 0
for line in lines:
    nums = line.replace('\n', '').split(' ')
    tmp = 0
    for i in range(1, len(nums)):
        diff = int(nums[i]) - int(nums[i - 1])
        if abs(diff) > 3 or abs(diff) < 1 or diff * tmp < 0 :
            unsafe += 1
            break
        tmp = diff

print(len(lines) - unsafe)

