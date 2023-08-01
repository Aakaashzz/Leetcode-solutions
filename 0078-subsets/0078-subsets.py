class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]

        mask = 2**len(nums) - 1

        while mask:
            copy = mask
            new = []
            i = 0
            while copy:
                if copy & 1:
                    new.append(nums[i])
                copy >>= 1
                i += 1
            ans.append(new)

            mask -= 1
        
        return ans