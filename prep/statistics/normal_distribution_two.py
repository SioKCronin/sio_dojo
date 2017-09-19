# Normal Disribution Two

import math

def less_than_boundary_cdf(x, mean, std):
    return round(0.5 * 100 * (1 + math.erf((x - mean)/ (std * math.sqrt(2)))), 3)

def between_boundaries_cdf(x_low, x_high, mean, std):
    low = 0.5 * (1 + math.erf((x_low - mean)/ (std * math.sqrt(2))))
    high = 0.5 * (1 + math.erf((x_high - mean)/ (std * math.sqrt(2))))
    result = (high - low) * 100
    return round(result, 3)

print round(100 - less_than_boundary_cdf(80, 70, 10), 2)
print round(100 - less_than_boundary_cdf(60, 70, 10), 2)
print round(less_than_boundary_cdf(60, 70, 10), 2)


