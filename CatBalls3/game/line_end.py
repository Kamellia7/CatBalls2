import pygame as pg


class LineEnd:
    def __init__(self, window, start_point, end_point, colour, thickness):
        self.window = window
        self.start_point = start_point
        self.end_point = end_point
        self.colour = colour
        self.thickness = thickness

    def draw(self):
        pg.draw.line(self.window.surface, self.colour, self.start_point, self.end_point, self.thickness)
