class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        # store { word : maxlen } in dp
        # word will be used to track predecessor later on
        dp = {}
        W = sorted(words, key = len) 
        # sorting based on length

        for w in W:
            dp[w] = 1
            # initialize
            for i in range(len(w)):
                # for each position of w, skip one
                # (to find its possible predecessor)
                # and check if it is available in dp.
                prv = w[:i] + w[i+1:]
                if prv in dp:
                    # predecessor of w was found!!
                    # update dp value
                    dp[w] = max(dp[prv] + 1, dp[w])
        
        # return max of all possible values in dp
        return max(dp.values())