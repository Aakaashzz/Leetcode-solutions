class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        # Sort the input list of integers
        nums.sort()
        n = len(nums)
        
        # Define the minimum and maximum possible values for the maximum difference
        min_max_diff = 0
        max_max_diff = nums[-1] - nums[0]
        
        # Binary search for the smallest maximum difference that satisfies the given condition
        while min_max_diff < max_max_diff:
            mid_max_diff = (min_max_diff + max_max_diff) // 2
            
            # Count the number of pairs of adjacent integers with a difference less than or equal to mid_max_diff
            pair_count = 0
            i = 1
            while i < n:
                if nums[i] - nums[i-1] <= mid_max_diff:
                    pair_count += 1
                    i += 1
                i += 1
            
            # If the number of such pairs is greater than or equal to p, decrease the maximum possible value of the maximum difference
            if pair_count >= p:
                max_max_diff = mid_max_diff
            # Otherwise, increase the minimum possible value of the maximum difference
            else:
                min_max_diff = mid_max_diff + 1
        
        # Return the smallest maximum difference that satisfies the given condition
        return min_max_diff