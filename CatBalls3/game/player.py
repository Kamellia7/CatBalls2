import pygame as pg
from .catball import CatBall
from .line_shoot import LineShoot
from colours import *
import math


def is_collided(cb1, cb2, offset=10):
    return (cb1.R + offset + cb2.R) ** 2 >= (cb1.x - cb2.x) ** 2 + (cb1.y - cb2.y) ** 2


class Player(CatBall):
    def __init__(self, window, x, y, image, speed, *groups, cat_balls, game, ):
        super().__init__(window, x, y, image, speed, *groups)
        self.line_shoot = LineShoot(window, (x, y), (x, y), WHITE, 3)
        self.run = False
        self.cat_balls = cat_balls
        self.game = game
        self.angle = 0
        self.start = False
        self.count = 0
        self.mouse_down = False

    def input_process(self):
        if not self.run:
            for event in self.window.events:
                if event.type == pg.MOUSEBUTTONDOWN:
                    self.mouse_down = True
                elif event.type == pg.MOUSEBUTTONUP and self.mouse_down:
                    ex, ey = pg.mouse.get_pos()
                    dx = ex - self.x
                    dy = ey - self.y
                    self.angle = math.atan2(dx, dy)
                    self.run = True
                    self.line_shoot.end_point = self.line_shoot.start_point
                    self.mouse_down = False
                if self.mouse_down:
                    self.line_shoot.end_point = pg.mouse.get_pos()

    def handle_border_collision(self):
        ww, wh = self.window.size

        if self.x - self.R <= 0 or self.x + self.R >= ww:
            self.speed_x = -self.speed_x
        if self.y - self.R <= 0:
            self.run = False
        if self.y + self.R >= wh:
            self.back_to_start_state()
            self.run = False

    def get_chain(self, node, chain):
        for cb in self.cat_balls:
            if is_collided(node, cb, 40) and node.image == cb.image and cb not in chain:
                chain.append(cb)
                chain = self.get_chain(cb, chain)
        return chain

    def handle_cat_balls_collision(self, new_image):
        for cb in self.cat_balls:
            if is_collided(self, cb):
                self.game.check_over()
                chain = self.get_chain(self, [self])
                self.handle_chain(chain, new_image)
                self.run = False
                break

    def handle_chain(self, chain, new_image):
        cat_ball = self.copy_cat_ball()
        if len(chain) >= 3:
            self.count -= 1
            self.game.score += len(chain)
            self.game.widgets['text_score'].setText(f'Score: {self.game.score}')

            cat_ball.fall = True
            for cb in chain:
                cb.fall = True

        self.cat_balls.append(cat_ball)
        self.back_to_start_state()
        self.image = new_image

    def move(self):
        speed_x = self.get_el_speed_x()
        speed_y = self.get_el_speed_y()
        self.move_x(speed_x * math.sin(self.angle))
        self.move_y(speed_y * math.cos(self.angle))

    def copy_cat_ball(self):
        return CatBall(self.window, self.x, self.y, self.image, 1)

    def back_to_start_state(self):
        self.count += 1
        self.speed_x = abs(self.speed_x)
        self.speed_y = abs(self.speed_y)
        self.x, self.y = self.line_shoot.start_point
        self.rect = self.image.get_rect(center=self.line_shoot.start_point)

    def shift_cat_balls_down(self):
        for cb in self.cat_balls:
            cb.shift = True

    def update(self, new_image, cat_balls=None):
        if self.run:
            self.move()
            self.handle_border_collision()
            self.handle_cat_balls_collision(new_image)
            if self.count % 6 == 0 and self.count:
                self.shift_cat_balls_down()
                self.count += 1

    def draw(self):
        super().draw()
        self.line_shoot.draw()
