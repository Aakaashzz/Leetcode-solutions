class Solution(object):
    def twoSum(self, nums, target):
       numToIndex = {}
       for i in range(len(nums)):
           diff = target - nums[i]
           if diff in numToIndex:
               return [numToIndex[diff], i]
           else:
                numToIndex[nums[i]] = i