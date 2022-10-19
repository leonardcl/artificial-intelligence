# Sudoku Solver with CSP
# Leonard Christopher Limanjaya
# Artificial Intelligence HW2 - Number 1

class SudokuSolver():
    def __init__(self):
        self.matrix = []
        self.get_input()
        self.solver()
        self.print_result()
        
    def get_input(self):
        """Getting Input from terminal 
        Convert into list
        returns list of input
        """
        # print("Input Sudoku Problem:")
        self.matrix = []
        for _ in range(9):
            self.matrix.append([int(num) for num in input().split(" ")])

    def check_columns(self, col, num):
        for row in range(9):
            if self.matrix[row][col] == num:
                return False
        return True

    def check_rows(self, row, num):
        for col in range(9):
            if self.matrix[row][col] == num:
                return False
        return True
            
    def check_box(self, col, row, num):
        box_col = col - col%3
        box_row = row - row%3
        for c in range(box_col, box_col+3):
            for r in range(box_row, box_row+3):
                if self.matrix[r][c] == num:
                    return False
        return True 

    def check_value(self, col , row, num):
        if self.check_box(col, row, num) and self.check_columns(col, num) and self.check_rows(row, num):
            return True
        return False

    def find_zero(self):
        for x in range(9):
            for y in range(9):
                if self.matrix[x][y] == 0:
                    return x, y
        return -1, -1

    def solver(self):
        x, y = self.find_zero()
        if x == -1 and y == -1:
            return True
        for n in range(1, 10):
            if self.check_value(y, x, n):
                self.matrix[x][y] = n
                if self.solver():
                    return True
                self.matrix[x][y] = 0
        return False
    
    def print_result(self):
        for x in range(9):
            for y in range(9):
                print(self.matrix[x][y], end=" ")
            print("\n", end="")
                        
                        
if __name__ == '__main__':
    matrixsolver = SudokuSolver()