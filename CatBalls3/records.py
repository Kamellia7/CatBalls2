from pygame_widgets.textbox import TextBox
from pygame_widgets.button import Button
from .scene import Scene
from colours import *


class Records(Scene):
    def __init__(self, window):
        super().__init__(window)
        self.set_background('images/bg-records.png')
        self.records = open('records').readlines()
        self.widgets['record_table'] = self.create_record_table()
        self.widgets['button_back'] = self.create_button_back()
        self.elapsed = 0

    def show(self):
        super().show()
        self.records = open('records').readlines()

    def create_record_table(self):
        table_text_boxes = []
        table_width = 350
        table_height = 550
        table_x = (self.window.size[0] - table_width) // 2
        table_y = (self.window.size[1] - table_height) // 2
        text_box_width = 300
        text_box_height = 40
        text_box_x = table_x + (table_width - text_box_width) // 2
        padding = 30
        text_box_y = [y for y in range(table_y + int(padding * 1.5), table_height - padding, text_box_height + padding)]
        n_text_boxes = len(text_box_y)
        text_box_font_colours = COLOUR_SEQUENCE * 3
        text_box_border_colour = text_box_font_colours
        text_box_colour = (0,) * 3
        font_size = 30
        border_thickness = 5

        for i in range(n_text_boxes):
            text_box = TextBox(self.window.surface, text_box_x, text_box_y[i], text_box_width, text_box_height,
                               fontSize=font_size, colour=text_box_colour, borderColour=text_box_border_colour[i],
                               textColour=text_box_font_colours[i], borderThickness=border_thickness)
            text_box.setText(
                f'{i + 1}: {self.records[i - 1].rstrip()}' if self.records[i - 1].strip() != '' else f'{i + 1} PASS')
            text_box.disable()
            table_text_boxes.append(text_box)

        return table_text_boxes

    def create_button_back(self):
        width = 200
        height = 60
        x = (self.window.size[0] - width) // 2
        y = 600
        colour = (38,) * 3
        font_colour = BLUE
        border_colour = BLACK
        hover_colour = WHITE
        hover_border_colour = BLUE
        border_thickness = 5
        font_size = 40
        text = 'Back'

        return Button(self.window.surface, x, y, width, height, colour=colour, textColour=font_colour,
                      borderColour=border_colour, borderThickness=border_thickness, text=text, fontSize=font_size,
                      hoverBorderColour=hover_border_colour, hoverColour=hover_colour,
                      onClick=lambda: self.window.set_scene('main_menu'))

    def advance_one_step(self):
        self.draw_background()
        self.elapsed += self.window.elapsed

        if self.elapsed >= 500:
            button = self.widgets['button_back']
            change_button_text_colour(button, next_colour(button.textColour))
            change_button_hover_border_colour(button, next_colour(button.hoverBorderColour))
            self.elapsed = 0
