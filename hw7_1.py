class Matrix:
    def __init__(self, myMatrix):
        self.myMatrix = myMatrix

    def __str__(self):
        text = "Super Mega Matrix Pro Max S:"
        for line in self.myMatrix:
            text += "\n" + str(line)[1:-1]
        return text

    def __add__(self, other):
        test = self.myMatrix
        for i in range(len(self.myMatrix)):
            for j in range(len(self.myMatrix[i])):
                test[i][j] = self.myMatrix[i][j] + other.myMatrix[i][j]
        return test


myMatrix = [[31, 22], [37, 43], [51, 86]]
a = Matrix(myMatrix)
print(a)
b = Matrix(myMatrix)
c = a + b
print(Matrix(c))
