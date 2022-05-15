import random

class lifegameLogic:
    def __init__(self, row, column):
        self.mp = [[0 for i in range(column)] for j in range(row)]
        self.nxtmp = [[0 for i in range(column)] for j in range(row)]
        self.isStart = 0
        self.Row = row
        self.Column = column

    def rand(self):
        for i in range(self.Row):
            for j in range(self.Column):
                self.mp[i][j] = random.choice([0, 1])

    def get_neighbor(self, x, y):
        num = 0
        for i in range(3):
            for j in range(3):
                if i == j and i == 1:
                    continue
                else:
                    num += self.mp[(x - 1 + i) % self.Row][(y - 1 + j) % self.Column]
        return num

    def play(self):
        for i in range(self.Row):
            for j in range(self.Column):
                num = self.get_neighbor(i, j)
                if num == 3:
                    self.nxtmp[i][j] = 1
                elif num != 2:
                    self.nxtmp[i][j] = 0
                else:
                    self.nxtmp[i][j] = self.mp[i][j]
        for i in range(self.Row):
            for j in range(self.Column):
                self.mp[i][j] = self.nxtmp[i][j]

    def reset(self):
        for i in range(self.Row):
            for j in range(self.Column):
                self.mp[i][j] = 0