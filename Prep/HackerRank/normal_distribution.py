# Normal Disribution

import math

def less_than_boundary_cdf(x, mean, std):
    return round(0.5 * (1 + math.erf((x - mean)/ (std * math.sqrt(2)))), 3)

def between_boundaries_cdf(x_low, x_high, mean, std):
    low = 0.5 * (1 + math.erf((x_low - mean)/ (std * math.sqrt(2))))
    high = 0.5 * (1 + math.erf((x_high - mean)/ (std * math.sqrt(2))))
    return round(high - low, 3)

print less_than_boundary_cdf(19.5, 20, 2)
print between_boundaries_cdf(20, 22, 20, 2)

