class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def isvalid(row, col, target): #判断是否合法
            
            for idx in range(len(board)):
                #行
                if board[row][idx] == target:
                    return False
                #列
                if board[idx][col] == target:
                    return False
                #九宫格
                row_get, col_get = (row//3)*3 + idx//3, (col//3)*3 + idx%3
                if board[row_get][col_get] == target:
                    return False
            return True

        
        def getplace():
            for row in range(len(board)):
                for col in range(len(board)):
                    if board[row][col] == ".":
                        return [row, col]
            return [-1, -1] 
        
        def solveNumber():
            if getplace() == [-1, -1]:
                return True
            aim_list = getplace()
            for i in range(1, 10):
                if isvalid(aim_list[0], aim_list[1], str(i)):
                    board[aim_list[0]][aim_list[1]] = str(i)
                    if solveNumber():
                        return True
                    board[aim_list[0]][aim_list[1]] = "."
            return False
        
        solveNumber()
        return board