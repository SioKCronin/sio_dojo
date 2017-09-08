# Manhattan

# Visiting Manhattan

# Load in data

X, Y, L, H  = [int(i) for i in raw_input().strip().split(' ')]

landmarks, hotels = [], []

for l in range(L):
    landmarks.append(tuple(int(i) for i in raw_input().strip().split(' ')))

for h in range(H):
    hotels.append(tuple(int(i) for i in raw_input().strip().split(' ')))

# Calculate hotel distances from each landmark 

    totals = {}

    for i in range(len(hotels)):
        for l in landmarks:
            totals[i] = 0
            totals[i] = totals[i] + abs(hotels[i][0] - l[0]) + abs(hotels[i][1] - l[1])

# Guard for more than one hotel with the same value

minimum = min(totals, key=totals.get) + 1

