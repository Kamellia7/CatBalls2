import pygame as pg
import pygame_widgets as pw
from pygame_widgets.button import Button
from .scene import Scene
from .game import Game
from .records import Records
from collections import namedtuple
from colours import *


class MainMenu(Scene):
    def __init__(self, window):
        super().__init__(window)
        self.set_background('images/bg-main-menu.jpg')

        buttons = self.create_buttons()
        self.widgets['central_buttons'] = buttons
        self.elapsed = 0

    def advance_one_step(self):
        self.draw_background()
        self.elapsed += self.window.elapsed

        if self.elapsed >= 500:
            buttons = self.widgets['central_buttons']

            change_button_text_colour(buttons.start, next_colour(buttons.start.textColour))
            change_button_text_colour(buttons.settings, next_colour(buttons.settings.textColour))
            change_button_text_colour(buttons.records, next_colour(buttons.records.textColour))

            change_button_hover_border_colour(buttons.start, next_colour(buttons.start.hoverBorderColour))
            change_button_hover_border_colour(buttons.settings, next_colour(buttons.settings.hoverBorderColour))
            change_button_hover_border_colour(buttons.records, next_colour(buttons.records.hoverBorderColour))

            self.elapsed = 0

    def create_buttons(self):
        size = (200, 80)
        window_size = self.window.size

        x = (window_size[0] - size[0]) // 2
        k = window_size[1] // 10
        y = (2 * k, 4 * k, 6 * k)

        font_size = 40
        texts = ('start', 'settings', 'records')
        colours = (BLUE, VIOLET, RED)

        Buttons = namedtuple("Buttons", texts)
        buttons = (
            Button(self.window.surface, x, y[i], *size,
                   colour=(0,) * 3,
                   text=texts[i].capitalize(),
                   fontSize=font_size,
                   borderThickness=10,
                   hoverBorderColour=colours[i],
                   hoverColour=WHITE,
                   textColour=colours[i]) for i in range(3))

        buttons = Buttons(*buttons)

        buttons.start.onClick = lambda: self.window.set_scene('game')
        buttons.settings.onClick = lambda: self.window.set_scene('settings')
        buttons.records.onClick = lambda: self.window.set_scene('records')

        return buttons
