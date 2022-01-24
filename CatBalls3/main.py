import pygame as pg
from window import Window
from scenes.main_menu import MainMenu
from scenes.game import Game
from scenes.records import Records
from scenes.loss import Loss
from scenes.settings import Settings


def main():
    pg.init()

    size = (600, 750)
    title = 'CatsBalls'
    icon = pg.image.load('images/icon.png')

    window = Window(size, title, icon)

    window.append_scene(MainMenu, 'main_menu')
    window.append_scene(Game, 'game')
    window.append_scene(Records, 'records')
    window.append_scene(Loss, 'loss')
    window.append_scene(Settings, 'settings')

    window.set_scene('main_menu')
    window.loop(60)


if __name__ == '__main__':
    main()
