class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Initialize a hashmap where the keys and values can be a set
        seen_r = collections.defaultdict(set) # For rows
        seen_c = collections.defaultdict(set) # For cols
        seen_squares = collections.defaultdict(set)
        for row in range(9):
            for col in range(9):
                if board[row][col] == '.': # basically means if the value is null then continue
                    continue
                if (board[row][col] in seen_r[row] or board[row][col] in seen_c[col] or board[row][col] in seen_squares[(row//3,col//3)]):
                    return False
                seen_r[row].add(board[row][col])
                seen_c[col].add(board[row][col])
                seen_squares[(row//3,col//3)].add(board[row][col])
        return True
        




        