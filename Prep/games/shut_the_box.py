class Box():
    def __init__(self, name):
        self.name = name

    def status(self):
        return [1,2,3]

def play():
    box = Box('box')
    box2 = Box('Carl')
    print box.status()
    print "Welcome to Shut The Box"

if __name__ == '__main__':
    play()
