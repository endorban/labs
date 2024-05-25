# база 1
import numpy as np
import matplotlib.pyplot as plt

class figure:
    def __init__(self, dot_centr_x, dot_centr_y, P = None, S = None):
        self.dot_centr_x = dot_centr_x
        self.dot_centr_y = dot_centr_y
        self.P = P
        self.S = S

class circle(figure):
    def __init__(self, dot_centr_x, dot_centr_y, r):
        figure.__init__(self, dot_centr_x, dot_centr_y)
        self.r = r
        self.area = np.pi * self.r**2
        self.length = 2 * np.pi * r

class triangle:
    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3
    def Mass(self):
        return [self.x1, self.x2, self.x3, self.x1], [self.y1, self.y2, self.y3, self.y1]

class rectangle(triangle):
    def __init__(self, x1, y1, x2, y2, x3, y3, x4, y4):
        triangle.__init__(self, x1, y1, x2, y2, x3, y3)
        self.x4 = x4
        self.y4 = y4
    def Mass(self):
        return [self.x1, self.x2, self.x3, self.x4, self.x1], [self.y1, self.y2, self.y3, self.y4, self.y1]
def Circle_Draw(x, y, r):
    figure, axes = plt.subplots()

    cc = plt.Circle((x, y), SuperCircle.r, color='blue', fill=False)

    plt.ylim(y + r + (r // 2), y - r - (r // 2))
    plt.xlim(x + r + (r // 2), x - r - (r // 2))
    axes.set_aspect(1)
    axes.add_artist(cc)
    plt.show()

def Triangle_Draw(Mass):
    plt.plot(Mass[0], Mass[1])
    plt.show()
def Rectangle_Draw(Mass):
    plt.plot(Mass[0], Mass[1])
    plt.show()

print('Выберите цифру рисунка:\n1) Треугольник\n2) Круг\n3) Прямоугольник')
Draw = input()
if Draw == '1':
    Triangle1 = triangle(0, 0, 1, 1, 2, 0)
    Triangle_Draw(Triangle1.Mass())
elif Draw == '2':
    SuperCircle = circle(0, 0, 2)
    Circle_Draw(SuperCircle.dot_centr_x, SuperCircle.dot_centr_y, SuperCircle.r)
elif Draw == '3':
    Rectangle1 = rectangle(0, 0, 0, 1, 2, 1, 2, 0)
    Rectangle_Draw(Rectangle1.Mass())
else:
    print('Данная операция отсутствует')

# база 2
import numpy as np


class Matrix:
    def __init__(self, matrix):
        self.matrix = np.array(matrix)

    def __str__(self):
        S = ''
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                S += str(self.matrix[i][j]) + '\t'
            S = S[:-1]
            S += '\n'
        return S[:-1]

    def size(self):
        return (len(self.matrix), len(self.matrix[0]))

    def __add__(self1, self2):
        if self1.size() != self2.size():
            raise ValueError("Размеры не совпадают")
            return None
        else:
            return Matrix(self1.matrix + self2.matrix)

    def __mul__(self1, self2):
        if type(self1) is int:
            return Matrix(self1 * self2.matrix)
        elif type(self2) is int:
            return Matrix(self2 * self1.matrix)
        elif len(self1.matrix[0]) != len(self2.matrix):
            raise ValueError("Матрицы нельзя умножить")
            return None
        else:
            return Matrix(np.dot(self1.matrix, self2.matrix))

    __rmul__ = __mul__

    def transposed(self):
        M = Matrix([])
        M.matrix = np.transpose(self.matrix)
        return M

m = Matrix([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
n = Matrix([[1, 5, 9]])
print('Сумма двух одинаковых матриц m равна\n' + str(m + m))
print('Произведение матриц n и m равно\n' + str(n * m))
print('Матрица m - это\n' + str(m) + '\nа транспонированная ей - \n' + str(Matrix.transposed(m)))
print('Произведение матрицы m на число 2 равно\n' + str(2 * m))

# база 3
import numpy as np
class Matrix:
    def __init__(self, matrix):
        self.matrix = np.array(matrix)

    def __str__(self):
        S = ''
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                S += str(self.matrix[i][j]) + '\t'
            S = S[:-1]
            S += '\n'
        return S[:-1]

    def size(self):
        return (len(self.matrix), len(self.matrix[0]))

    def __add__(self1, self2):
        if self1.size() != self2.size():
            raise ValueError("Размеры не совпадают")
            return None
        else:
            return Matrix(self1.matrix + self2.matrix)

    def __mul__(self1, self2):
        if type(self1) is int:
            return Matrix(self1 * self2.matrix)
        elif type(self2) is int:
            return Matrix(self2 * self1.matrix)
        elif len(self1.matrix[0]) != len(self2.matrix):
            raise ValueError("Матрицы нельзя умножить")
            return None
        else:
            return Matrix(np.dot(self1.matrix, self2.matrix))

    __rmul__ = __mul__

    def transposed(self):
        M = Matrix([])
        M.matrix = np.transpose(self.matrix)
        return M

class Vector(Matrix):
    def __init__(self, dot1, dot2):
        self.begin = dot1
        self.end = dot2
        super().__init__([[self.end[a] - self.begin[a] for a in range(len(self.begin))]])

    def __add__(self1, self2):
        m = super().__add__(self1, self2)
        if m == None:
            return None
        return Vector([self1.begin[a] for a in range(len(self1.begin))], m.matrix)

    def __sub__(self1, self2):
        return Vector([self1.begin[a] for a in range(len(self1.begin))],
                      [[(self1.end[a] - self2.matrix[a]) for a in range(len(self1.matrix))]])

    def __mul__(self1, self2):
        if type(self1) is not int and type(self2) is not int:
            self2t = self2.transposed()
        m = Matrix.__mul__(self1, self2t)
        if m.matrix.shape == (1, 1):
            return m.matrix[0][0]
        return m.matrix

    __rmul__ = __mul__

    def getLength(self):
        l2 = 0
        for a in range(len(self.matrix[0])):
            l2 += (self.matrix[0][a]) ** 2
        l = l2 ** 0.5
        return l

    def getCos(self1, self2):
        return self1 * self2 / (self1.getLength() * self2.getLength())

    def about(self):
        print('Вектор №%i:' % id(self))
        print('\tКоординаты вектора:', self.matrix)
        print('\tКоординаты начальной точки:', self.begin)
        print('\tКоординаты конечной точки:', self.end)
        print('\tДлина вектора:', self.getLength())

    def getVectMul(self1, self2):
        if not 2 <= len(self1.matrix[0]) <= 3:
            return Vector([0, 0, 0], [0, 0, 0])
        else:
            return Vector([0, 0, 0], np.cross(self1.matrix.reshape(-1), self2.matrix.reshape(-1)))

b = Vector([1, 2, 3, 4, 5], [0, -1, -2, -3, -4])
b.about()
a = Vector([12, 18, 5, 63, 8], [1, -21, -53, -16, -8])
print('Скалярное произведение:', a * b)
print('Косинус угла:', Vector.getCos(a, b))
