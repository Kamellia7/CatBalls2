from .scene import Scene
import pygame as pg
from pygame_widgets.button import Button
from pygame_widgets.textbox import TextBox

from colours import *
import random

from game.catball import CatBall
from game.line_end import LineEnd
from game.player import Player


class Game(Scene):
    score = 0
    n_cat_images = 5
    n_rows = 4

    def __init__(self, window):
        super().__init__(window)
        self.set_background('images/bg-game.png')
        self.cat_images = self.load_cat_images()
        self.cat_balls = self.create_cat_balls()
        self.height_line_end = 557
        self.line_end = self.create_line_end()
        self.player = self.create_player()
        self.widgets['button_exit'] = self.create_button_exit()
        self.score = 0

        self.widgets['text_score'] = self.create_text_score()
        self.elapsed = 0

    def create_button_exit(self):
        size = (200, 60)
        x = 30
        y = self.line_end.start_point[1] + CatBall.H * 2
        colour = WHITE
        font_colour = BLUE
        border_colour = BLUE
        hover_colour = WHITE
        hover_border_colour = BLUE
        border_thickness = 5
        font_size = 40
        text = 'Exit'
        score = 0

        return Button(self.window.surface, x, y, *size, colour=colour, textColour=font_colour,
                      borderColour=border_colour, borderThickness=border_thickness, text=text, fontSize=font_size,
                      hoverBorderColour=hover_border_colour, hoverColour=hover_colour,
                      onClick=lambda: self.window.set_scene('main_menu'))

    def create_text_score(self):
        text_box_width = 200
        text_box_height = 60
        text_box_x = 30
        text_box_y = self.line_end.start_point[1] + CatBall.H * 0.5
        text_box_font_colours = COLOUR_SEQUENCE
        text_box_border_colour = text_box_font_colours
        text_box_colour = WHITE
        font_size = 40
        border_thickness = 5

        text_box = TextBox(self.window.surface, text_box_x, text_box_y, text_box_width, text_box_height,
                           fontSize=font_size, colour=text_box_colour, borderColour=text_box_border_colour[0],
                           textColour=text_box_font_colours[0], borderThickness=border_thickness)

        text_box.setText(f'Score: {self.score}')
        text_box.disable()

        return text_box

    @staticmethod
    def load_cat_images():
        return [
            pg.transform.scale(
                pg.image.load(f'images/c{i}.png'),
                (CatBall.W, CatBall.H)).convert_alpha()
            for i in range(1, Game.n_cat_images + 1)]

    def create_line_end(self):
        return LineEnd(self.window, (0, self.height_line_end), (self.window.size[0], self.height_line_end),
                       colour=WHITE,
                       thickness=5)

    def create_cat_balls(self):
        ww = self.window.size[0]
        cw, ch = CatBall.W, CatBall.H
        offset_between = 10
        t = ww // cw
        offset_x = cw // 2 + ((t * cw) - (t * offset_between)) % cw
        n_column = ((t * cw) - (t * offset_between)) // cw
        n_rows = Game.n_rows
        cat_balls = []
        y = ch // 2 + offset_between
        for i in range(n_rows):
            x = offset_x
            for j in range(n_column):
                cat_balls.append(CatBall(self.window, x, y, random.choice(self.cat_images), 1))
                x += cw + offset_between
            y += ch + offset_between
        return cat_balls

    def add_cat_balls_line(self):
        ww = self.window.size[0]
        cw, ch = CatBall.W, CatBall.H
        offset_between = 10
        t = ww // cw
        n_column = ((t * cw) - (t * offset_between)) // cw
        y = ch // 2 + offset_between
        x = cw // 2 + ((t * cw) - (t * offset_between)) % cw
        for j in range(n_column):
            self.cat_balls.append(CatBall(self.window, x, y, random.choice(self.cat_images), 1))
            x += cw + offset_between

    def draw_cat_balls(self):
        for cat_ball in self.cat_balls:
            cat_ball.draw()

    def update_cat_balls(self):
        shift = self.cat_balls[0].shift

        for cat_ball in self.cat_balls:
            cat_ball.update(self.cat_balls)

        if shift != self.cat_balls[0].shift:
            self.check_over()
            self.add_cat_balls_line()

    def create_player(self):
        ww, wh = self.window.size
        mid_x = ww // 2
        y = self.line_end.start_point[1] + CatBall.H * 1.5
        return Player(self.window, mid_x, y, random.choice(self.cat_images), 0.5, cat_balls=self.cat_balls, game=self)

    def over(self):
        Game.score = self.score
        self.window.set_scene('loss')

    def new(self):
        self.cat_balls = self.create_cat_balls()
        self.player = self.create_player()
        self.score = 0
        self.widgets['text_score'].setText(f'Score: {self.score}')

    def show(self):
        super().show()
        self.new()

    def check_over(self):
        for cb in self.cat_balls:
            if cb.y + cb.H >= self.height_line_end:
                self.over()

    def advance_one_step(self):
        self.draw_background()
        self.line_end.draw()
        self.update_cat_balls()
        self.draw_cat_balls()
        self.player.input_process()
        self.player.update(random.choice(self.cat_images))
        self.player.draw()

        self.elapsed += self.window.elapsed

        if self.elapsed >= 1000:
            button = self.widgets['button_exit']
            change_button_text_colour(button, next_colour(button.textColour))
            change_button_hover_border_colour(button, next_colour(button.hoverBorderColour))
            self.elapsed = 0
