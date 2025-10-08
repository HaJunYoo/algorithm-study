from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        len_x, len_y = len(board), len(board[0])
        visited = [[False for _ in range(len_y)] for _ in range(len_x)]
        print(visited)
        dxs, dys = [0, 0, 1, -1], [1, -1, 0, 0]

        def valid_in_range(x, y):
            if 0 <= x < len_x and 0 <= y < len_y:
                return True
            else:
                return False

        def search(x: int, y: int, path: int, visited: List[List[bool]]):

            if not visited[x][y] and board[x][y] == word[path]:
                if path == len(word) - 1:
                    # print(path)
                    return True

                visited[x][y] = True
                flag = False

                for dx, dy in zip(dxs, dys):
                    nx, ny = x + dx, y + dy
                    if valid_in_range(nx, ny):
                        if search(nx, ny, path+1, visited):
                            flag = True
                            return flag

                visited[x][y] = False
                return flag

        for x in range(len_x):
            for y in range(len_y):
                # print(f'{x}, {y}')
                if search(x, y, 0, visited):
                    return True

        return False


if __name__ == '__main__':
    solution = Solution()
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "ABCCED"
    ans: bool = solution.exist(board=board, word=word)
    print(ans)
