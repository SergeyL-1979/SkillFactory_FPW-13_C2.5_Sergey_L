class Game(object):
    letters = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J")
    ships_rules = [1, 1, 1, 1, 2, 2, 2, 3, 3, 4]
    field_size = len(letters)

    def __init__(self):

        self.players = []
        self.current_player = None
        self.next_player = None

        self.status = 'prepare'

    # при старте игры назначаем текущего и следующего игрока
    def start_game(self):

        self.current_player = self.players[0]
        self.next_player = self.players[1]

    # функция переключения статусов
    def status_check(self):
        # переключаем с prepare на in game если в игру добавлено два игрока.
        # далее стартуем игру
        if self.status == 'prepare' and len(self.players) >= 2:
            self.status = 'in game'
            self.start_game()
            return True
        # переключаем в статус game over если у следующего игрока осталось 0 кораблей.
        if self.status == 'in game' and len(self.next_player.ships) == 0:
            self.status = 'game over'
            return True

    def add_player(self, player):
        # при добавлении игрока создаем для него поле
        player.field = Field(Game.field_size)
        player.enemy_ships = list(Game.ships_rules)
        # расставляем корабли
        self.ships_setup(player)
        # высчитываем вес для клеток поля (это нужно только для ИИ, но в целом при расширении возможностей
        # игры можно будет например на основе этого давать подсказки игроку).
        player.field.recalculate_weight_map(player.enemy_ships)
        self.players.append(player)

    def ships_setup(self, player):
        # делаем расстановку кораблей по правилам заданным в классе Game
        for ship_size in Game.ships_rules:
            # задаем количество попыток при выставлении кораблей случайным образом
            # нужно для того чтобы не попасть в бесконечный цикл когда для последнего корабля остаётся очень мало места
            retry_count = 30

            # создаем предварительно корабль-балванку просто нужного размера
            # дальше будет видно что мы присваиваем ему координаты которые ввел пользователь
            ship = Ship(ship_size, 0, 0, 0)

            while True:

                Game.clear_screen()
                if player.auto_ship_setup is not True:
                    player.field.draw_field(FieldPart.main)
                    player.message.append('Куда поставить {} корабль: '.format(ship_size))
                    for _ in player.message:
                        print(_)
                else:
                    print('{}. Расставляем корабли...'.format(player.name))

                player.message.clear()

                x, y, r = player.get_input('ship_setup')
                # если пользователь ввёл какую-то ерунду функция возвратит нули, значит без вопросов делаем continue
                # фактически просто просим еще раз ввести координаты
                if x + y + r == 0:
                    continue

                ship.set_position(x, y, r)

                # если корабль помещается на заданной позиции - отлично. добавляем игроку на поле корабль
                # также добавляем корабль в список кораблей игрока. и переходим к следующему кораблю для расстановки
                if player.field.check_ship_fits(ship, FieldPart.main):
                    player.field.add_ship_to_field(ship, FieldPart.main)
                    player.ships.append(ship)
                    break

                # сюда мы добираемся только если корабль не поместился. пишем юзеру что позиция неправильная
                # и отнимаем попытку на расстановку
                player.message.append('Неправильная позиция!')
                retry_count -= 1
                if retry_count < 0:
                    # после заданного количества неудачных попыток - обнуляем карту игрока
                    # убираем у него все корабли и начинаем расстановку по новой
                    player.field.map = [[Cell.empty_cell for _ in range(Game.field_size)] for _ in
                                        range(Game.field_size)]
                    player.ships = []
                    self.ships_setup(player)
                    return True

    def draw(self):
        if not self.current_player.is_ai:
            self.current_player.field.draw_field(FieldPart.main)
            self.current_player.field.draw_field(FieldPart.radar)
            # если интересно узнать вес клеток можно расскомментировать эту строку:
            # self.current_player.field.draw_field(FieldPart.weight)
        for line in self.current_player.message:
            print(line)

    # игроки меняются вот так вот просто.
    def switch_players(self):
        self.current_player, self.next_player = self.next_player, self.current_player

    @staticmethod
    def clear_screen():
        os.system('cls' if os.name == 'nt' else 'clear')