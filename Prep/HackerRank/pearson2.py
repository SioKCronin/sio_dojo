# Pearson Correlation

import math

def pearson_correlation(n, array_x, array_y):
    x_mean = sum(array_x) / n
    y_mean = sum(array_y) / n
    x_variance = map(lambda x: (x - x_mean)**2, array_x)
    y_variance = map(lambda y: (y - y_mean)**2, array_y)
    x_std = math.sqrt(sum(x_variance) / n)
    y_std = math.sqrt(sum(y_variance) / n)
    difference_products = [(x - x_mean) * (y - y_mean) for x, y in zip(array_x, array_y)]
    return round(sum(difference_products)/(n * x_std * y_std), 3)

if __name__ == '__main__':
    n = int(raw_input())
    array_x = [float(x) for x in raw_input().rsplit().split(" ")]
    array_y = [float(x) for x in raw_input().rsplit().split(" ")]
    print pearson_correlation(n, array_x, array_y)

