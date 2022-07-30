class Solution:
    def rotate(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        size = len(matrix)
        i = 0
        j = 0
        for z in range(size-1, 0,-2):
            for k in range(z):
                self.rotate_loop(matrix, i, j)
                j += 1
            i += 1
            j = i
           
    def rotate_loop(self, matrix, i, j):
        size = len(matrix)
        store = matrix[size-j-1][i]
        for k in range(4):
            matrix[i][j], store = store, matrix[i][j]
            i, j = j, size-i-1