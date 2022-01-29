import pygame as pg
from collections.abc import Iterable


class Scene:
    def __init__(self, window):
        self.window = window
        self.widgets = {}
        self.background = None

    def set_background(self, image_path):
        self.background = pg.image.load(image_path)
        self.background = pg.transform.scale(self.background, self.window.size).convert_alpha()

    def draw_background(self):
        self.window.surface.blit(self.background, (0, 0))

    def hide_widgets(self, key):
        widgets = self.widgets[key]
        if isinstance(widgets, Iterable):
            for widget in widgets:
                widget.hide()
        else:
            widgets.hide()

    def hide_all_widgets(self):
        for key in self.widgets:
            self.hide_widgets(key)

    def show_widgets(self, key):
        widgets = self.widgets[key]
        if isinstance(widgets, Iterable):
            for widget in widgets:
                widget.show()
        else:
            widgets.show()

    def show_all_widgets(self):
        for key in self.widgets:
            self.show_widgets(key)

    def hide(self):
        self.hide_all_widgets()

    def show(self):
        self.show_all_widgets()

    def advance_one_step(self):
        pass
