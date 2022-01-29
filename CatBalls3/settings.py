from pygame_widgets.button import Button
from pygame_widgets.textbox import TextBox
from .scene import Scene
from .game import Game
from colours import *


class Settings(Scene):
    def __init__(self, window):
        super().__init__(window)
        self.set_background('images/bg-records.png')
        self.widgets['input_n_types_balls'], self.widgets['input_n_rows'] = self.create_inputs()
        self.widgets['button_save'], self.widgets['button_back'] = self.create_buttons()

    def create_inputs(self):
        text_box_width = 400
        text_box_height = 40
        text_box_x = 100
        text_box_y = (150, 250)
        text_box_font_colour = BLACK
        text_box_border_colour = text_box_font_colour
        text_box_colour = WHITE
        font_size = 30
        border_thickness = 5

        return [TextBox(self.window.surface, text_box_x, text_box_y[i], text_box_width, text_box_height,
                        fontSize=font_size, colour=text_box_colour, borderColour=text_box_border_colour,
                        textColour=text_box_font_colour, borderThickness=border_thickness) for i in range(2)]

    def show(self):
        super().show()
        self.widgets['input_n_types_balls'].setText(f'N types balls (max N = 6): {Game.n_cat_images}')
        self.widgets['input_n_rows'].setText(f'N rows: {Game.n_rows}')

    def save(self):
        Game.n_cat_images = int(self.widgets['input_n_types_balls'].getText()[-1])
        Game.n_rows = int(self.widgets['input_n_rows'].getText()[-1])

        if not isinstance(self.window.scenes['game'], type):
            game = self.window.scenes['game']
            game.cat_images = game.load_cat_images()

    def create_buttons(self):
        width = 200
        height = 60
        x = (self.window.size[0] - width) // 2
        y = (500, 600)
        texts = ('Save', 'Back')
        on_click = (self.save, lambda: self.window.set_scene('main_menu'))
        colour = BLACK
        font_colour = BLUE
        border_colour = BLACK
        hover_colour = WHITE
        hover_border_colour = BLUE
        border_thickness = 5
        font_size = 40
        text = 'Back'

        return [Button(self.window.surface, x, y[i], width, height, colour=colour, textColour=font_colour,
                       borderColour=border_colour, borderThickness=border_thickness, text=texts[i], fontSize=font_size,
                       hoverBorderColour=hover_border_colour, hoverColour=hover_colour,
                       onClick=on_click[i]) for i in range(2)]

    def create_button_save(self):
        pass

    def advance_one_step(self):
        self.draw_background()
