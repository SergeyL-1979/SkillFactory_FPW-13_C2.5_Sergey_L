class Board:
    
    def __init__(self, hid=False, size=10):
        self.size = size
        self.hid = hid
        self.cells = [["O"] * size for i in range(size)]
        self.shot = set()
        # self.count = 0
        # self.busy = []
        # self.ships = []

    def show_field(self):
        res = ""
        res += '    '
        for i in range(10):
            res += chr(ord('A') + i) + " "+" "
        res += "\n"
        for i in range(10):
            res += f" {i} ".format(i)
            for j in range(10):
                if self.cells[i][j]:
                    cell = (self.cells[i][j])
                else:
                    cell = " • " if (i, j) in self.shot else "_"
                res += " {} ".format(cell)
            res += "  \n"
        return res
	
s = Board()
print(s.show_field())
