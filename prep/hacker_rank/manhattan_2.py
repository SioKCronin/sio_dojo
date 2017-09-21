# Manhattan 2

N, M, T = [int(i) for i in raw_input()]

crossroads = []
for row in range(N):
    crossroads.append([int(i) for i in raw_input()])

counter = T
total_candies = 0
necessary_moves = (N-1) + (M-1)

x = 0
y = 0

while T >= 0:
    if x == N and y == M:
        print total_candies
    elif necessary_moves > T:
        print 'Too late'
    elif crossroads[x + 1] and crossroads[y + 1]:
        if crossroads[x + 1] > crossroads[y + 1]:
            x = x + 1
            total_candies = total_candies + crossroads[x + 1]
        else:
            y = y + 1
            total_candies = total_candies + crossroads[y + 1]
    elif crossroads[x + 1]:
            total_candies = total_candies + crossroads[x + 1]
    elif crossroads[y + 1]:
            total_candies = total_candies + crossroads[y + 1]
    T += 1

