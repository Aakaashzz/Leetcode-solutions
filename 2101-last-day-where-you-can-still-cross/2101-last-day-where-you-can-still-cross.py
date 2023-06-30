class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:

        

        dp = {}
        matrix = [[0]*col for i in range(row)]
        def isEnd(r,c):
            if (r+1,c,"end") in dp or (r-1,c,"end") in dp or (r,c+1,"end") in dp or (r,c-1,"end") in dp or (r+1,c+1,"end") in dp or (r+1,c-1,"end") in dp or (r-1,c-1,"end") in dp or (r-1,c+1,"end") in dp:
                return True
            return False
        
        def isStart(r,c):
            if (r+1,c,"start") in dp or (r-1,c,"start") in dp or (r,c+1,"start") in dp or (r,c-1,"start") in dp or (r+1,c+1,"start") in dp or (r+1,c-1,"start") in dp or (r-1,c-1,"start") in dp or (r-1,c+1,"start") in dp:
                return True
            return False
        
        def updateCheck(r,c,start,end):
            if r >= 0 and r < row and c >= 0 and c < col and matrix[r][c] == 1:
                if start and (r,c,"start") not in dp:
                    dp[(r,c,"start")] = True
                    updateStatus(r,c,True,False)
                if end and (r,c,"end") not in dp:
                    dp[(r,c,"end")] = True
                    updateStatus(r,c,False,True)

        def updateStatus(r,c,start,end):
            updateCheck(r+1,c,start,end)
            updateCheck(r-1,c,start,end)
            updateCheck(r,c+1,start,end)
            updateCheck(r,c-1,start,end)
            updateCheck(r+1,c+1,start,end)
            updateCheck(r-1,c-1,start,end)
            updateCheck(r-1,c+1,start,end)
            updateCheck(r+1,c-1,start,end)
            


        ans = 0
        for i in cells:
            r,c = i[0]-1,i[1]-1
            matrix[r][c] = 1
            if isEnd(r,c):
                dp[(r,c,"end")] = True
            if isStart(r,c):
                dp[(r,c,"start")] = True
            if c == col-1:
                dp[(r,c,"end")] = True
            if c == 0:
                dp[(r,c,"start")] = True
            
            if (r,c,"end") in dp and (r,c,"start") in dp:
                break
            if (r,c,"end") in dp or (r,c,"start") in dp:
                updateStatus(r,c,dp.get((r,c,"start"),False),dp.get((r,c,"end"),False))
            ans += 1

        return ans
