class Game:
    def __init__(self, player, computer):
        self.player = player
        self.computer = computer

    def start(self):
        # начинаем игру, чередуем ходы игрока и компьютера,
        # пока один из героев не умрет. Выводим информацию о каждом ходе
        # (кто атаковал и сколько здоровья осталось у противника)
        # и объявляем победителя.
        print('Игра "Битва героев"')
        while self.player.is_alive() and self.computer.is_alive():
            print(f'Ходит {self.player.name}')
            self.player.attack(self.computer)
            print(f'Здоровье {self.computer.name}: {self.computer.health}')
            if not self.computer.is_alive():
                print(f'Победил {self.player.name}')
                break
            print(f'Ходит {self.computer.name}')
            self.computer.attack(self.player)
            print(f'Здоровье {self.player.name}: {self.player.health}')
            if not self.player.is_alive():
                print(f'Победил {self.computer.name}')
                break

