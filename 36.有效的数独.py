class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col = defaultdict(set)  #表示建立一个字典（哈希结构），其value是一个集合  ,也可以放一个列表，一样的
        row = defaultdict(set)
        sqrt = defaultdict(set)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == ".":
                    continue
                point = (i//3)*3 + j//3
                if board[i][j] not in row[i] and board[i][j] not in col[j] and board[i][j] not in sqrt[point]:
                    row[i].add(board[i][j])
                    col[j].add(board[i][j])
                    sqrt[point].add(board[i][j])
                else:    
                    return False
        return True