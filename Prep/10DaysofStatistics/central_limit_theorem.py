# Central Limit Theorem

import math

def less_than_boundary_cdf(x, mean, std):
    return round(0.5 * (1 + math.erf((x - mean)/ (std * math.sqrt(2)))), 4)

print less_than_boundary_cdf(9800, 49 * 205, math.sqrt(49) * 15)

