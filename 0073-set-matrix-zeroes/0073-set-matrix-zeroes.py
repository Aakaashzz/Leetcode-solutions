class Solution(object):
    def setZeroes(self, matrix):
        col=[]
        row = []

        for x in range(len(matrix)):
            if 0 in matrix[x]:
                row.append(x)
            for y in range(len(matrix[0])):
                if matrix[x][y]==0:
                    col.append(y)

        for x in range(len(matrix)):
            for y in range(len(matrix[0])):
                if y in col or x in row:
                    matrix[x][y]=0

        return(matrix)