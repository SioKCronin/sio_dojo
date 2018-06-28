# Regression

data = [(95, 85), (85, 95), (80, 70), (70, 65), (60, 70)]

n  = len(data)

x = [d[0] for d in data]
y = [d[1] for d in data]

x_sum = sum(x)
y_sum = sum(y)

x_mean = sum(x)/len(x)
y_mean = sum(y)/len(y) 

x_squared = [i**2 for i in x]
x_squared = sum(x_squared)
xy = [i * j for (i, j) in data]
xy = sum(xy)

b = float(n * xy - x_sum * y_sum) / float(n * x_squared - (x_sum**2)) 

a = y_mean -  b * x_mean

y_hat = a + b * 80 

print round(y_hat, 3)
