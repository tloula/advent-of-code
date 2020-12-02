# ********************************************* #
# Advent of Code Day 1                          #
# Trevor Loula                                  #
# Cedarville University Leaderboard             #
# ********************************************* #

# Given a list of numbers, find two and three numbers such that
# their sum is equal to the target integer 2020.

nums = set(int(line.strip()) for line in open('input/day-1.txt'))

def twoSum(nums, target):
    for num in nums:
        complement = int(target) - int(num)
        if complement in nums: return [num, complement]

def threeSum(nums, target):
    for i in range(0, len(nums)):
        for j in range(i, len(nums)):
            for k in range(j, len(nums)):
                if (nums[i] + nums[j] + nums[k] == target):
                    return [nums[i], nums[j], nums[k]]

ans1 = twoSum(nums, 2020)
print("Two Sum:", ans1)
print("Two Sum Multiplied:", ans1[0]*ans1[1])

ans2 = threeSum(list(nums), 2020)
print("Three Sum:", ans2)
print("Three Sum Multiplied:", ans2[0]*ans2[1]*ans2[2])
