# Nonogram Solver with CSP
# Leonard Christopher Limanjaya
# Artificial Intelligence HW2 - Number 2

from itertools import combinations


class NonogramSolver():
    def __init__(self):
        self.nonogram = []
        self.row = {}
        self.col = {}
        self.opts_row = {}
        self.opts_col = {}
        self.union_row = {}
        self.union_col = {}
        self.union = []
            
        self.get_input()
        self.generate_combinations()
        
        while self.check_num_of_possibilities() > (self.col_size + self.row_size):
            self.cross_validate()
            
        self.cross_validate()
        self.print()
    
    def get_input(self):
        size = input("").split(" ")
        self.row_size = int(size[0])
        self.col_size = int(size[1])
        for i in range(self.row_size):
            self.row[i]=[int(num) for num in input().split(" ")]
            
        for i in range(self.col_size):
            self.col[i]=[int(num) for num in input().split(" ")]
            
        for _ in range(self.col_size):
            self.nonogram.append(["0"] * self.col_size)
            self.union.append([0] * self.col_size)
            
    def get_combinations(self, input_l, max_length):
        empty = max_length - (sum(input_l) + len(input_l) - 1)
        opts = combinations(range(len(input_l) + empty), len(input_l))
        opt_lists = []
        for opt in opts:
            opt_list = []
            for p in opt:
                opt_list.append(p)
            opt_lists.append(opt_list)
            
        return opt_lists
        
    def generate_actual_combinations(self, combs, lists, size):
        all_of_it = []
        for c in combs:
            actual = [0] * size
            start = 0
            for n in range(len(c)):
                for k in range(lists[n]):
                    actual[start+c[n]+k] = 1
                start = start + lists[n]
            all_of_it.append(actual)
            
        return all_of_it
    
    def generate_combinations(self):
        for row in self.row:
            self.opts_row[row]=self.generate_actual_combinations(self.get_combinations(self.row[row], self.row_size), self.row[row], self.row_size)
        for col in self.col:
            self.opts_col[col]=self.generate_actual_combinations(self.get_combinations(self.col[col], self.col_size), self.col[col], self.col_size)    
    
    def check_overlap(self, combs, ovrlp):
        threshold = len(combs)
        return [1 if i >= threshold else -1 if i == 0 else 0 for i in ovrlp]
    
    def cross_validate(self):
        for row in range(self.row_size):
            self.union_row[row]=self.check_overlap(self.opts_row[row], [sum(i) for i in zip(*self.opts_row[row])])
            for opts in self.opts_row[row]:
                for col in range(self.col_size):
                    if self.union[row][col] == 0:
                        continue
                    if self.union[row][col] == 1 and opts[col] != 1:
                        self.opts_row[row].remove(opts)
                        break
                    
                    elif self.union[row][col] == -1 and opts[col] != 0:
                        self.opts_row[row].remove(opts)
                        break
            
            for col in range(len(self.union_row[row])):
                if self.union_row[row][col] == 1:
                    self.nonogram[row][col] = "*"
                    self.union[row][col] = 1
                if self.union_row[row][col] == -1:
                    self.nonogram[row][col] = " "
                    self.union[row][col] = -1
                   
        for col in range(self.col_size):
            self.union_col[col]=self.check_overlap(self.opts_col[col], [sum(i) for i in zip(*self.opts_col[col])])    
            
            for opts in self.opts_col[col]:
                for row in range(self.row_size):
                    if self.union[row][col] == 0:
                        continue
                    if self.union[row][col] == 1 and opts[row] != 1:
                        self.opts_col[col].remove(opts)
                        break
                    elif self.union[row][col] == -1 and opts[row] != 0:
                        self.opts_col[col].remove(opts)
                        break
            
            for row in range(len(self.union_col[col])):
                if self.union_col[col][row] == 1:
                    self.nonogram[row][col] = "*"
                    self.union[row][col] = 1
                if self.union_col[col][row] == -1:
                    self.nonogram[row][col] = " "
                    self.union[row][col] = -1
                    
    def print(self):
        for y in self.nonogram:
            for x in y:
                print(x, end="")
            print("")
        
    def check_num_of_possibilities(self):
        num = 0
        for opt in self.opts_row:
            num += len(self.opts_row[opt])
        for opt in self.opts_col:
            num += len(self.opts_col[opt])
            
        return num
        
if __name__ == '__main__':
    nonogramsolver = NonogramSolver()