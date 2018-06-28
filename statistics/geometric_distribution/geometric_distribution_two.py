# Geometric Distribution Two

defective_prob = 1 / 3.0
inspection = 5

def neg_bernoulli(n, p):
    return p * (1-p)**(n-1)

prob = sum(neg_bernoulli(i, defective_prob) for i in range(1, 6))

print(round(prob, 3))

