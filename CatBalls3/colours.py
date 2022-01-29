BLACK = (0,) * 3
WHITE = (230,) * 3
BLUE = (100, 100, 255)
VIOLET = (255, 100, 255)
RED = (255, 100, 100)
COLOUR_SEQUENCE = (BLUE, VIOLET, RED)


def change_button_text_colour(button, colour):
    button.text = button.font.render(button.string, True, colour)
    button.textColour = colour


def change_button_hover_border_colour(button, colour):
    button.hoverBorderColour = colour


def next_colour(colour):
    return {
        BLUE: VIOLET,
        VIOLET: RED,
        RED: BLUE,
    }[colour]
