PIXEL = 30

class Beign:
    type = ""
    costs = []
    costT = 0
    x = 0
    y = 0

    def __init__(self, type, x, y, costs):
        self.type = type
        self.x = x
        self.y = y

        for i in range(len(costs)):
            if costs[i][0] == type:
                self.costs = costs[i]
                break

    def setX(self, x):
        self.x = x

    def setY(self, y):
        self.y = y

    def setCostT(self, valor):
        self.costT = int(valor)

    @property
    def getX(self):
        return self.x

    @property
    def getY(self):
        return self.y

    @property
    def getCostT(self):
        return self.costT



    def UP(self, map, flag):
        if self.costs[int(map) + 1] != 'X':
            if flag == 1:
                self.y = self.y-PIXEL
                self.costT = self.costT + int(self.costs[int(map) + 1])
            elif flag == 0:
                return 1
        return 0

    def DOWN(self, map, flag):
        if self.costs[int(map) + 1] != 'X':
            if flag == 1:
                self.y += PIXEL
                self.costT = self.costT + int(self.costs[int(map) + 1])
            elif flag == 0:
                return 1
        return 0

    def RIGHT(self, map, flag):
        if self.costs[int(map) + 1] != 'X':
            if flag == 1:
                self.x = self.x+PIXEL
                self.costT = self.costT + int(self.costs[int(map) + 1])
            elif flag == 0:
                return 1
        return 0

    def LEFT(self, map, flag):
        if self.costs[int(map) + 1] != 'X':
            if flag == 1:
                self.x = self.x-PIXEL
                self.costT = self.costT + int(self.costs[int(map) + 1])
            elif flag == 0:
                return 1
        return 0
