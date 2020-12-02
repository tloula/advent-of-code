nums = set(int(line.strip()) for line in open('day-1-input.txt'))

def twoSum(nums, target):
    for n in nums:
        c = int(target) - int(n)
        if c in nums: return [n, c]

# Guess who doesn't care about runtime
def threeSum(nums, target):
    for i in range(0, len(nums)):
        for j in range(i, len(nums)):
            for k in range(j, len(nums)):
                if (nums[i] + nums[j] + nums[k] == target):
                    return [nums[i], nums[j], nums[k]]

ans1 = twoSum(nums, 2020)
print("Two Sum:", ans1)
print("Two Sum Code:", ans1[0]*ans1[1])

ans2 = threeSum(list(nums), 2020)
print("Three Sum:", ans2)
print("Three Sum Code:", ans2[0]*ans2[1]*ans2[2])
