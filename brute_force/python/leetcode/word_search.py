from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        len_x, len_y = len(board), len(board[0])
        visited = [[False for _ in range(len_y)] for _ in range(len_x)]
        dxs, dys = [0, 0, 1, -1], [1, -1, 0, 0]

        def search(x, y, w_index, visited):
            word_char = word[w_index]
            if not visited[x][y] and board[x][y] == word_char:
                if w_index == len(word) - 1:
                    return True
            
                visited[x][y] = True
                flag = False

                for dx, dy in zip(dxs, dys):
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < len_x and 0 <= ny < len_y:
                        flag = search(nx, ny, w_index+1, visited)
                        if flag:
                            return True

                visited[x][y] = False
                return flag

            return False

        for i in range(len_x):
            for j in range(len_y):
                if search(i, j, 0, visited):
                    return True
        
        return False

if __name__ == '__main__':
    solution = Solution()
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "ABCCED"
    ans: bool = solution.exist(board=board, word=word)
    print(ans)
