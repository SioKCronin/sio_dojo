def a(x):
    return 10


def b():
    x = 2
    try:
        return a(x)
    except ValueError:
        print("Different errors")
        return 0


def c():
    v = 0
    try:
        v = b()
    except KeyError:
        v = -1
    return v

if __name__ == "__main__":
    print(c())
    print("HI")
