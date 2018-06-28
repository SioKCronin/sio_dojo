# Highlight Landmarks

D = [i for i in raw_input().strip().split(' ')]
n = int(raw_input())
L = [i for i in raw_input().strip().split(' ')]

def bold_target_words(D, n, L):
    for i in range(n):
        if i in D:
            value = '<br>' + i + '<br>'
                D[D.index(i)] = value
                output = ' '.join(D)

        print output

        bold_target_words(D, n, L)

