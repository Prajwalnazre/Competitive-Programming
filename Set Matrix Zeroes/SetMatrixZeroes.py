class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = []
        cols = []
        for i in range(len(matrix)) :
            for j in range(len(matrix[0])) :
                if matrix[i][j] == 0 :
                    rows.append(i)
                    cols.append(j)
        
        # print(rows)
        # print(cols)
        
        for i in range(len(matrix)) :
            for j in range(len(matrix[0])) :
                print(j)
                if i in rows :
                    matrix[i][j] = 0
                if j in cols :
                    matrix[i][j] = 0
        
        return matrix
        
