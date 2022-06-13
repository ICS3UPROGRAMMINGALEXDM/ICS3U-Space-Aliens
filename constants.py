#!/usr/bin/env python3
# Created By: Alex De Meo
# Date: 03/25/2022
# Description: This is my constants file for the edge badge

# EdgeBadge screen size is 160x128 and Sprites are 16x16
SCREEN_X = 160
SCREEN_Y = 128
# Screen grid size
SCREEN_GRID_X = 10
SCREEN_GRID_Y = 8
# Size of the characters
SPRITE_SIZE = 16
TOTAL_NUMBER_OF_ALIENS = 5
# how many times the screen updates every second
FPS = 60
# How fast every sprite can move
SPRITE_MOVEMENT_SPEED = 1

# Button state is a dictionary that holds key value pairs
# first element is the key, second is the value

button_state = {
    "button_up": "up",
    "button_just_pressed": "just pressed",
    "button_still_pressed": "still pressed",
    "button_released": "released",
}
