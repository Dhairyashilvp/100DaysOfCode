class Solution:
    def judgeCircle(self, moves: str) -> bool:
        # U = moves.count("U")
        # D = moves.count("D")
        # R = moves.count("R")
        # L = moves.count("L")
        # if U == D and R == L:
        #     return True
        # else:
        #     return False
        x = y = 0
        for move in moves:
            if move == 'U': 
                y -= 1 
                print("|")
            elif move == 'D': 
                y += 1 
                print("|")
            elif move == 'L': 
                x -= 1
                print("--")
            elif move == 'R': 
                x += 1
                print("--")

        return x == y == 0
                