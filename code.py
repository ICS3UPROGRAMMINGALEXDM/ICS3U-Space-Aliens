#!/usr/bin/env python3
# Created By: Alex De Meo
# Date: 03/25/2022
# Description: This is my CPT game for the edgebadge

import ugame
import stage


def game_scene():
    # his function is the main game scene

    # accesses the image bank and setting it to a variable st index 0
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")\
    # sets up a new image bank, this one for the sprites
    image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")
    # creates the 10 by 8 image grid, sets it to background
    background = stage.Grid(image_bank_background, 10, 8)
    # creates the ship sprite and sets it to the 5th index of the sprite list
    # puts it to 75,66 on the screen
    ship = stage.Sprite(image_bank_sprites, 5, 75, 66)

    # 60 means 60 hertz which will update it 60 times per second
    game = stage.Stage(ugame.display, 60)
    # accesses the first layer(background) and makes the list of images for the background
    game.layers = [ship] + [background]
    # takes layers and shows them on the screen
    game.render_block()
    # this is the game loop so it is supposed to loop forever
    while True:
        # Get user input

        # update game logic

        # redraw sprites 
        # refreshes the ship sprite
        game.render_sprites([ship])
        # wait until the specified 60th of a second is reached
        game.tick()


if __name__ == "__main__":
    game_scene()
