class Solution(object):
    def putMarbles(self, weights, k):
        n = len(weights)
        candidates = []
        for i in range(0,n-1):
            candidates.append(weights[i] + weights[i+1])

        candidates.sort()
        min_sum, max_sum = 0, 0
        for i in range(0,k-1):
            min_sum += candidates[i]
            max_sum += candidates[n-2-i]

        return max_sum - min_sum