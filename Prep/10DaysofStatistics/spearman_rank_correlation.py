# Spearman Rank Correlation

import math

def spearman_rank_correlation_unique(n, x, y):
    n = float(n)
    x_seq = sorted(x)
    x_rank= [x_seq.index(v) + 1 for v in x]

    y_seq = sorted(y)
    y_rank = [y_seq.index(w) + 1 for w in y]

    squared_differences = [ (y - x) **2 for x, y in zip(y_rank, x_rank)]
    print squared_differences

    return round(1.0 - ((sum(squared_differences) * 6) / (n * (n**2 - 1))), 3)

print spearman_rank_correlation_unique(10, [10, 9.8, 8, 7.8, 7.7, 7, 6, 5, 4, 2],[200, 44, 32, 24, 22, 17, 15, 12, 8, 4 ] )
print spearman_rank_correlation_unique(10, [10, 9.8, 8, 7.8, 7.7, 7, 6, 15, 4, 2],[200, 414, 32, 24, 212, 17, 15, 12, 8, 4 ] )

'''

if __name__ == '__main__':
    n = int(raw_input())
    array_x = [int(x) for x in raw_input().split(" ")]
    array_y = [int(x) for x in raw_input().split(" ")]
    print spearman_rank_correlation_unique(n, array_x, array_y)

'''
