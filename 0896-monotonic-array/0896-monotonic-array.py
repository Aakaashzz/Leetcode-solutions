class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        o=False
        k=[]
        for i in nums:
            k.append(i)
        k.sort()
        if(k[0]==nums[-1]):
            for i in range(len(nums)-1):
                print(1)
                if nums[i]>=nums[i+1]:
                    o=True
                else:
                    o=False
                    break
        else:
            for i in range(len(nums)-1):
                print(nums[i])
                if nums[i]<=nums[i+1]:
                    o=True
                else:
                    o=False
                    break
        if(len(nums)==1):
            o=True
        return(o)