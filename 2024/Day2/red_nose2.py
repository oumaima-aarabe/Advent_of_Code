def is_safe(nums):
    tmp = 0
    for i in range(1, len(nums)):
        diff = nums[i] - nums[i - 1]
        if abs(diff) > 3 or abs(diff) < 1 or diff * tmp < 0 :
            return(False)
        tmp = diff
    return(True)



def can_be_made_safe(nums):
    for j in range(0, len(nums) - 1):
        if is_safe(nums[:j] + nums[j + 1:]):
            return True
    return False

with open("a", 'r') as f:
    lines = f.readlines()

safe = 0
b = 0
for line in lines:
    nums = list(map(int, line.strip().split()))
    if is_safe(nums): safe += 1
    elif can_be_made_safe(nums): safe += 1

print(safe)




