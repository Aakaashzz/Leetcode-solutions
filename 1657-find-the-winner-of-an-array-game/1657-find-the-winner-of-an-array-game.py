class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        a = arr[0]
        win = 0
        for i in arr[1:]:
            if a < i:
                a = i
                win = 1
            elif a > i:
                win = win + 1
            
            if win >= k:
                return a

        return a  
