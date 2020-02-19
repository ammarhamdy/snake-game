surface_size = (510, 510)
tile_size = 10
tile_region = tile_size * 2.5
stroke_width = 5

# play_size.
play_size = (
    stroke_width,  # top
    surface_size[0] - stroke_width,  # right
    surface_size[1] - stroke_width,  # bottom
    stroke_width  # left
)


def update_play_size(index):
    global play_size
    play_size = (stroke_width * (index + 2),
                 surface_size[0] - stroke_width * (index + 2),
                 surface_size[1] - stroke_width * (index + 2),
                 stroke_width * (index + 2))


# borders.
max_num_border = 20
borders_position = [(stroke_width * (i + 1), stroke_width * (i + 1),
                     surface_size[0] - stroke_width * 2 * (i + 1),
                     surface_size[1] - stroke_width * 2 * (i + 1))
                    for i in range(max_num_border)]

## speed.
speed_factor = 3
monster_speed_factor = 2
food_speed_factor = 1
