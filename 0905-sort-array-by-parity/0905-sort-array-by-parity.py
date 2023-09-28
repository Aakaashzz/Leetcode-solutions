class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        l1=[]
        for i in nums:
            if (i%2==0):
                l1.append(i)
        for i in nums:
            if (i%2!=0):
                l1.append(i)
        return(l1)