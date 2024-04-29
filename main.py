import hero
import game

player = hero.Hero('Игрок')
computer = hero.Hero('Компьютер')

game = game.Game(player, computer)
game.start()
