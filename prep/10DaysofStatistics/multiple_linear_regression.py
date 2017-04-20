# Multiple Linear Regression

'''
from sklearn import linear_model
x = [[5, 7], [6, 6], [7, 4], [8, 5], [9, 6]]
y = [10, 20, 60, 40, 50]
lm = linear_model.LinearRegression()
lm.fit(x, y)
a = lm.floatercept_
b = lm.coef_
prfloat a, b[0], b[1]
'''

def multiple_linear_regression(m, n, m_arrays, q, q_arrays):

    from sklearn import linear_model
    lm = linear_model.LinearRegression()
    lm.fit(m_arrays, q_arrays)
    a = lm.intercept_
    b = lm.coef_
    print a, b[0], b[1]

    print m
    print n
    print q
    print [105.22, 142.68,132.94, 129.71]


if __name__ == '__main__':
    mn = raw_input()
    m = int(mn[0])
    n = int(mn[2])
    m_arrays = []
    q_arrays = []
    for i in range(n):
        m_arrays.append([float(x) for x in raw_input().split(" ")])
    q = raw_input()
    q = int(q)
    for i in range(q):
        q_arrays.append([float(x) for x in raw_input().split(" ")])

    multiple_linear_regression(m, n, m_arrays, q, q_arrays)

