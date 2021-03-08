# skillfactory_fpw13_C2.5_Sergey_L

https://dtf.ru/flood/187827-python-napishem-morskoy-boy-s-dostoynym-sopernikom-ii

    class Board:
        def __init__(self):
            self.fields = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

        def update(self, n, seed):
            self.fields[(n / 3)][n % 3] = seed

        def printBoard(self):
            print
            for l in self.fields:
                for e in l:
                    print e,
                print

    b = Board()

    b.printBoard()

    b.update(1, 'X')
    b.printBoard()

    0 0 0
    0 0 0
    0 0 0

    0 X 0
    0 0 0
    0 0 0
