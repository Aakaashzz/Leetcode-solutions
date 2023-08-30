class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        n = len(nums)  # Get the length of the array
        operations = 0  # Initialize the operations counter

        prev_value = nums[n - 1]  # Initialize prev_value with the last element of the array

        # Iterate through the array in reverse order
        for i in range(n - 2, -1, -1):
            if nums[i] > prev_value:
                # Calculate how many times prev_value should be added to get nums[i]
                k = (nums[i] + prev_value - 1) // prev_value
                # Increment operations by k - 1
                operations += k - 1
                # Update prev_value to be nums[i] divided by k
                prev_value = nums[i] // k
            else:
                # If nums[i] is not greater than prev_value, update prev_value to nums[i]
                prev_value = nums[i]
        
        return operations  # Return the total number of operations

