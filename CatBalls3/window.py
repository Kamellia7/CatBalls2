import pygame as pg
import pygame_widgets as pw


class Window:
    def __init__(self, size, title, icon):
        self.surface = pg.display.set_mode(size)
        pg.display.set_caption(title)
        pg.display.set_icon(icon)

        self.size = size
        self.scenes = {}
        self.scene = None
        self.events = None
        self.elapsed = 0

    def loop(self, frame_rate=0):
        clock = pg.time.Clock()
        pg.mixer.music.load('cat_virtuoso.mp3')
        pg.mixer.music.set_volume(0.4)
        pg.mixer.music.play(loops=-1)

        while True:
            self.elapsed = clock.tick(frame_rate)
            self.events = pg.event.get()

            for event in self.events:
                if event.type == pg.QUIT:
                    exit(0)

            self.surface.fill((255,) * 3)
            self.scene.advance_one_step()
            pw.update(self.events)
            pg.display.update()


    def append_scene(self, scene_class, name):
        self.scenes[name] = scene_class

    def set_scene(self, name_scene_class):
        if self.scene is not None:
            self.scene.hide()
        self.scene = self.scenes[name_scene_class]
        if isinstance(self.scene, type):
            self.scene = self.scenes[name_scene_class](self)
            self.scenes[name_scene_class] = self.scene

        self.scene.show()
