import numpy as np
from math import pow


class Cubic:

    def __init__(self, a0, a1, a2, a3):
        self.a0 = a0
        self.a1 = a1
        self.a2 = a2
        self.a3 = a3

    def calculate(self, x):
        return self.a0 + self.a1 * x + self.a2 * (x ** 2) + self.a3 * (x ** 3)


class CubicSpline:
    def __init__(self, cubics, x_consts):
        self.cubics = cubics
        self.x_consts = x_consts

    def calculate_all(self, x):
        result = []
        for i in x:
            result.append(self.calculate(i))
        return result

    def calculate(self, x):
        cubic = self.cubics[self.get_p_number(x)]
        return cubic.calculate(x)

    def get_p_number(self, x):
        for i in range(1, len(self.x_consts)):
            if self.x_consts[i - 1] <= x <= self.x_consts[i]:
                return i - 1
        return None

def build_cubic_spline(x, y, start):
    assert len(x) == len(y)
    assert len(start) >= 2
    s1 = start[0]
    s2 = start[1]
    m = [[0] * 4 * (len(x) - 1)]
    m[0][0] = 1
    m[0][1] = x[0]
    m[0][2] = x[0] ** 2
    m[0][3] = x[0] ** 3

    for i in range(1, len(x) - 1):
        a1 = [0] * 4 * (len(x) - 1)
        a2 = a1[:]
        a1[(i - 1) * 4] = 1
        a1[(i - 1) * 4 + 1] = x[i]
        a1[(i - 1) * 4 + 2] = x[i] ** 2
        a1[(i - 1) * 4 + 3] = x[i] ** 3
        a2[i * 4] = 1
        a2[i * 4 + 1] = x[i]
        a2[i * 4 + 2] = x[i] ** 2
        a2[i * 4 + 3] = x[i] ** 3
        m.append(a1)
        m.append(a2)

    a = [0] * 4 * (len(x) - 1)
    a[-4] = 1
    a[-3] = x[-1]
    a[-2] = x[-1] ** 2
    a[-1] = x[-1] ** 3
    m.append(a)

    for i in range(1, len(x) - 1):
        a1 = [0] * 4 * (len(x) - 1)
        a2 = a1[:]
        a1[(i - 1) * 4 + 1] = 1
        a1[(i - 1) * 4 + 2] = 2 * x[i]
        a1[(i - 1) * 4 + 3] = 3 * x[i] ** 2
        a1[i * 4 + 1] = -1
        a1[i * 4 + 2] = -2 * x[i]
        a1[i * 4 + 3] = -3 * x[i] ** 2
        a2[(i - 1) * 4 + 2] = 2
        a2[(i - 1) * 4 + 3] = 6 * x[i]
        a2[i * 4 + 2] = -2
        a2[i * 4 + 3] = -6 * x[i]
        m.append(a1)
        m.append(a2)
    a = [0] * 4 * (len(x) - 1)
    a[1] = 1
    a[2] = 2 * x[0]
    a[3] = 3 * x[0] ** 2
    m.append(a)
    a = [0] * 4 * (len(x) - 1)
    a[-3] = 1
    a[-2] = 2 * x[-1]
    a[-1] = 3 * x[-1] ** 2
    m.append(a)

    r = [y[0]]
    for i in range(1, len(y) - 1):
        r.append(y[i])
        r.append(y[i])
    r.append(y[-1])

    for i in range(1, len(x) - 1):
        r.append(0)
        r.append(0)
    r.append(s1)
    r.append(s2)

    print(np.array(m))
    print(r)

    result = __evaluate_linear_system(m, r)

    cubics = []
    for i in range(0, len(result), 4):
        cubics.append(Cubic(result[i], result[i + 1], result[i + 2], result[i + 3]))
    cubic_spline = CubicSpline(cubics, x)

    return cubic_spline


def __evaluate_linear_system(matrix, result):
    A = np.array(matrix)
    B = np.array(result)
    X = np.linalg.solve(A, B)
    return X


if __name__ == '__main__':
    import matplotlib.pyplot as plt
    import numpy as np
    x = [0, 1, 2, 3, 4, 5, 6,  7, 8, 9, 10]
    y = [0, 2, 1, 3, 7, 8, 10, 6, 9, 3, 4]
    # build_cubic_spline(x, y, (2, -1))
    m = [[4, 3, 8, 9],
         [7, 6, 7, 4],
         [4, 3, 6, 5],
         [5, 2, 4, 9]]
    r = [5, 4, 7, 2]
    X = __evaluate_linear_system(m, r)
    # print(X)
    # plt.plot(x, y)
    # plt.show()

    x = [0, 1, 2, 3]
    y = [0, 2, 1, 3]
    # plt.plot(x, y)
    # plt.show()
    cubic_spline = build_cubic_spline(x, y, (2, 3))
    x = np.arange(0, 3.05, .05)
    y = cubic_spline.calculate_all(x)
    plt.plot(x, y)
    plt.show()

    # x = np.arange(0, 1.05, .05)
    # y = []
    # for i in x:
    #     y.append(cubics[0].calculate(i))
    # plt.plot(x, y)
    # # plt.show()
    #
    # x = np.arange(1, 2.05, .05)
    # y = []
    # for i in x:
    #     y.append(cubics[1].calculate(i))
    # plt.plot(x, y)
    # # plt.show()
    #
    # x = np.arange(2, 3.05, .05)
    # y = []
    # for i in x:
    #     y.append(cubics[2].calculate(i))
    # plt.plot(x, y)
    # plt.show()
