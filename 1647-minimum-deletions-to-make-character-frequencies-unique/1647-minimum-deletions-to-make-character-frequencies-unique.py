from sortedcontainers import SortedDict

class Solution:
    def minDeletions(self, s: str) -> int:
        freqToCnt = SortedDict(Counter(Counter(s).values()))
        deletions = 0
        i = -1
        while i >= -len(freqToCnt):
            freq, cnt = freqToCnt.peekitem(i)
            if cnt > 1:
                deletions += cnt - 1
                if freq > 1:
                    freqToCnt[freq-1] = freqToCnt.get(freq-1, 0) + cnt - 1

            i -= 1
        
        return deletions