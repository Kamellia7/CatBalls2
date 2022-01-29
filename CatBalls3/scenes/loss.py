from pygame_widgets.textbox import TextBox
from .scene import Scene
from .game import Game
from colours import *
from .records import Records


class Loss(Scene):
    def __init__(self, window):
        super().__init__(window)
        self.set_background('images/bg-records.png')
        records = Records(window)

        self.widgets = records.widgets
        self.advance_one_step = records.advance_one_step

        self.widgets['text_score'] = self.create_text_score()
        self.widgets['input_name'] = self.create_input_name()
        self.widgets['input_n_slot'] = self.create_input_n_slot()
        self.widgets['button_back'] = self.create_save_button()
        self.elapsed = 0

    def create_save_button(self):
        button = self.widgets['button_back']
        button.string = 'next'
        button.text = button.font.render(button.string, True, button.textColour)

        def f():
            nonlocal self
            self.save()
            self.window.set_scene('main_menu')

        button.onClick = f
        return button

    def save(self):
        in_name = self.widgets['input_name']
        in_n_slot = self.widgets['input_n_slot']
        text_in_name = in_name.getText()[6:]
        text_in_n_slot = in_n_slot.getText()[7:]

        if '' == text_in_name.strip() or '' == text_in_n_slot.strip():
            return

        n = int(text_in_n_slot)
        value = f'{text_in_name}: {Game.score}\n'
        with open('records', 'r+') as f:
            text_records = f.readlines()
            print(text_records)
            text_records[n - 1] = value
            f.seek(0)
            f.writelines(text_records)
            print(text_records)

    def create_input_name(self):
        text_box_width = 250
        text_box_height = 40
        text_box_x = 50
        text_box_y = 70
        text_box_font_colour = BLACK
        text_box_border_colour = text_box_font_colour
        text_box_colour = WHITE
        font_size = 30
        border_thickness = 5

        text_box = TextBox(self.window.surface, text_box_x, text_box_y, text_box_width, text_box_height,
                           fontSize=font_size, colour=text_box_colour, borderColour=text_box_border_colour,
                           textColour=text_box_font_colour, borderThickness=border_thickness)

        return text_box

    def show(self):
        super().show()
        self.widgets['input_name'].setText('Name: ')
        self.widgets['input_n_slot'].setText("N slot: ")
        self.widgets['text_score'].setText(f'Score: {Game.score}')

    def create_input_n_slot(self):
        text_box_width = 250
        text_box_height = 40
        text_box_x = 305
        text_box_y = 70
        text_box_font_colour = BLACK
        text_box_border_colour = text_box_font_colour
        text_box_colour = WHITE
        font_size = 30
        border_thickness = 5

        text_box = TextBox(self.window.surface, text_box_x, text_box_y, text_box_width, text_box_height,
                           fontSize=font_size, colour=text_box_colour, borderColour=text_box_border_colour,
                           textColour=text_box_font_colour, borderThickness=border_thickness)

        return text_box

    def create_text_score(self):
        text_box_width = 250
        text_box_height = 40
        text_box_x = 180
        text_box_y = 550
        text_box_font_colour = BLACK
        text_box_border_colour = text_box_font_colour
        text_box_colour = WHITE
        font_size = 30
        border_thickness = 5

        text_box = TextBox(self.window.surface, text_box_x, text_box_y, text_box_width, text_box_height,
                           fontSize=font_size, colour=text_box_colour, borderColour=text_box_border_colour,
                           textColour=text_box_font_colour, borderThickness=border_thickness)

        text_box.disable()
        text_box.setText('Score: ' + str(Game.score))
        return text_box
