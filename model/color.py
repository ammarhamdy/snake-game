from random import randint


white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)


palettes = (
    # w3 schools palettes.
    ((107, 91, 149), (254, 178, 54), (214, 65, 97), (255, 123, 37)),
    ((62, 68, 68),(130, 183, 75),(64, 93, 39),(193, 148, 106)),
    # ((254, 251, 216),(97, 134, 133),(54, 72, 107),(64, 64, 161)),
    ((200, 195, 204),(86, 63, 70), (140, 163, 163),(72, 79, 79)),
    ((104, 98, 86),(193, 80, 46), (88, 126, 118),(169, 110, 91)),
    # my pallet
    ((220, 20, 60),(255, 69, 0),(0, 250, 154),(255, 255, 0)),
    ((0, 255, 127),(0, 255, 0),(0, 250, 154),(0, 128, 128))
)
current_palette = palettes[randint(0, len(palettes)-1)]
color_index = -1
current = black


def update():
    global color_index
    global palette_index
    global current
    color_index = (color_index + 1) % 4
    current = current_palette[color_index]
