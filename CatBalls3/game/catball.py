import pygame as pg


class CatBall(pg.sprite.Sprite):
    W = 60
    H = 60
    R = 30

    def __init__(self, window, x, y, image, speed, *groups):
        super().__init__(*groups)
        self.window = window
        self.x = x
        self.y = y
        self.speed_x = speed
        self.speed_y = speed
        self.image = image
        self.rect = image.get_rect(center=(x, y))
        self.fall = False
        self.shift = False
        self.speed = 1
        self.prev_y = y

    def update(self, cat_balls):
        if self.shift:
            self.move_y(self.get_el_speed_y())
            if self.y - self.prev_y >= self.H:
                self.prev_y = self.y
                self.shift = False

        elif self.fall:
            self.move_y(self.get_el_speed_y())
            if self.y - self.R >= self.window.size[1]:
                del cat_balls[cat_balls.index(self)]
                self.fall = False

    def draw(self):
        self.window.surface.blit(self.image, self.rect)

    def get_el_speed_x(self):
        return self.speed_x * self.window.elapsed

    def get_el_speed_y(self):
        return self.speed_y * self.window.elapsed

    def move_x(self, offset):
        self.x += offset
        self.rect = self.image.get_rect(center=(self.x, self.y))

    def move_y(self, offset):
        self.y += offset
        self.rect = self.image.get_rect(center=(self.x, self.y))
