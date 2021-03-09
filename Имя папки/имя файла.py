# class Dot:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __eq__(self, other):
#         return self.x == other.x and self.y == other.y
#
#     def __repr__(self):
#         return f"({self.x}, {self.y})"


class Board:
    letters = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J")
    # ships_rules = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]  # в эту переменную поместим «правила» по кораблям
    field_size = len(letters)

    def __init__(self, hid=False):
        self.size = Board.field_size
        self.hid = hid
        self.cells = [[None] * 10 for i in range(10)]
        # self.count = 0
        # self.busy = []
        # self.ships = []

    def show_field(self, show_ships=None):
        res = ""
        res += '    '
        for i in range(10):
            res += chr(ord('A') + i) + " "
        res += "\n"
        for i in range(10):
            res += f"{i + 1} ".format(i)
            for j in range(10):
                if self.cells[i][j]:
                    cell = (self.cells[i][j].view(i, j, show_ships))
            #     else:
            #         cell = "•" if (i, j) in self.shot else "_"
            #     res += "𝖨{}".format(cell)
            res += "\n"
        return res
        # =================================================
        # res = ""
        # res += ' '
        # for i in range(1):
        #     res += "  " + "  ".join((map(str, range(1, 11))))
        #
        # for j in range(1):
        #     for i in range(10):
        #         print(self.letters[i])
        #     if self.cells[i][j]:
        #         cell = (self.cells[i][j].view(i, j, show_ships))
        #     # else:
        #     #     cell = "•" if (i, j) in self.shot else " _ "
        #     # res += "𝖨{}".format(cell)
        # # res += "𝖨\n"
        # return res


s = Board()
print(s.show_field())

# class Ship:
#     def __init__(self, size, x, y, rotation):
#         self.size = size
#         self.hp = size
#         self.x = x
#         self.y = y
#         self.rotation = rotation
#         self.set_rotation(rotation)
#
#     def set_position(self, x, y, r):
#         self.x = x
#         self.y = y
#         self.set_rotation(r)
#
#     def set_rotation(self, r):
#         self.rotation = r
#
#         if self.rotation == 0:
#             self.width = self.size
#             self.height = 1
#         elif self.rotation == 1:
#             self.width = 1
#             self.height = self.size
#         elif self.rotation == 2:
#             self.y = self.y - self.size + 1
#             self.width = self.size
#             self.height = 1
#         elif self.rotation == 3:
#             self.x = self.x - self.size + 1
#             self.width = 1
#             self.height = self.size

