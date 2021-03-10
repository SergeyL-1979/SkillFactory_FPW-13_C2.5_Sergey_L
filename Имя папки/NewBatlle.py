class Dot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f"({self.x}, {self.y})"


class BoardException(Exception):
    pass


class BoardOutException(BoardException):
    def __str__(self):
        return "Вы пытаетесь выстрелить за доску!"


class BoardUsedException(BoardException):
    def __str__(self):
        return "Вы уже стреляли в эту клетку"


class BoardWrongShipException(BoardException):
    pass


class Ship:
    def __init__(self, bow, l, rotation):
        self.bow = bow
        self.l = l
        self.rotation = rotation

    @property
    def dots(self):
        ship_dots = []
        for i in range(self.l):
            cur_x = self.bow.x
            cur_y = self.bow.y

            if self.rotation == 0:
                cur_x += i

            elif self.rotation == 1:
                cur_y += i

            ship_dots.append(Dot(cur_x, cur_y))

        return ship_dots

    def shooten(self, shot):
        return shot in self.dots


class Board:
    def __init__(self, hid=False, size=10):
        self.shot = None
        self.size = size
        self.hid = hid
        self.count = 0
        self.cells = [["O"] * size for i in range(size)]
        # self.shot = set()
        self.busy = []
        self.ships = []

    def show_field(self):
        res = ""
        res += '    '
        for i in range(10):
            res += chr(ord('A') + i) + " " + " "
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

            if self.hid:
                res = res.replace("■", "O")

        return res

    def add_ship(self, ship):

        for d in ship.dots:
            if self.out(d) or d in self.busy:
                raise BoardWrongShipException()
        for d in ship.dots:
            self.cells[d.x][d.y] = "■"
            self.busy.append(d)

        self.ships.append(ship)
        self.contour(ship)

    def contour(self, ship, verb=False):
        near = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1), (0, 0), (0, 1),
            (1, -1), (1, 0), (1, 1)
        ]
        for d in ship.dots:
            for dx, dy in near:
                cur = Dot(d.x + dx, d.y + dy)
                if not (self.out(cur)) and cur not in self.busy:
                    if verb:
                        self.size[cur.x][cur.y] = "."
                    self.busy.append(cur)

    def out(self, d):
        return not ((0 <= d.x < self.size) and (0 <= d.y < self.size))


s = Board()
b = Ship(Dot(1, 1), 4, 0)
c = Ship(Dot(5, 5), 3, 1)
s.add_ship(b)
s.add_ship(c)
print(s.show_field())
