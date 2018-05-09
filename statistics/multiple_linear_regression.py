# Multiple Linear Regression

def multiple_linear_regression(m, n, training_f, training_o, q, testing):

    from sklearn import linear_model
    lm = linear_model.LinearRegression()
    lm.fit(training_f, training_o)
    a = lm.intercept_.tolist[0]
    b = lm.coef_.tolist()[0]

    for i in testing:
        print a + i[0] * b[0] + i[1] * b[1]

if __name__ == '__main__':
    m, n = [int(i) for i in raw_input().strip().split(' ')]
    training_f = []
    training_o = []
    for i in range(n):
        data = map(float, raw_input().strip().split(' '))
        training_f.append(data[:m])
        training_o.append(data[m:]
    q = int(raw_input())
    testing = []
    for i in range(q):
        testing.append(map(float, raw_input().strip().split(' ')))

    multiple_linear_regression(m, n, training_f, training_o, q, testing)

