#!/usr/bin/env python3
# Created By: Alex De Meo
# Date: 03/25/2022
# Description: This is my CPT game for the edgebadge


import constants
import stage
import ugame


def menu_scene():
    # his function is the main game scene

    # accesses the image bank and setting it to a variable st index 0
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")

    # new variable called text set to list
    text = []

    # variable makes a piece of text // pallette selects the color
    text1 = stage.Text(
        width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None
    )

    # moves the cursor to this location
    text1.move(2, 10)

    # What the text is going to say
    text1.text("DE MEO GAME STUDIOS")

    # adds it to the list
    text.append(text1)

    # making another text object
    text2 = stage.Text(
        width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None
    )

    # moves the cursor to this location
    text2.move(35, 110)

    # What the text will say
    text2.text("PRESS START!")

    # adding to text list
    text.append(text2)

    # creates the 10 by 8 image grid, sets it to background
    background = stage.Grid(
        image_bank_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y
    )

    # 60 means 60 hertz which will update it 60 times per second
    game = stage.Stage(ugame.display, constants.FPS)

    # accesses the first layer(background) and makes the list of images for the background
    game.layers = text + [background]

    # takes layers and shows them on the screen
    game.render_block()

    # this is the game loop so it is supposed to loop forever
    while True:
        # Get user input
        # getting the buttons that are pressed - 60 times a second
        keys = ugame.buttons.get_pressed()

        # The if statements decide what to do when a button is pressed
        if keys & ugame.K_START:
            game_scene()

        # wait until the specified 60th of a second is reached
        game.tick()


def game_scene():
    # his function is the main game scene

    # accesses the image bank and setting it to a variable st index 0
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")

    # sets up a new image bank, this one for the sprites
    image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")

    # This is for the buttons that we want information about their state
    # 'A button' sets it to the button up state
    a_button = constants.button_state["button_up"]

    # 'B button' sets is to the button up state
    b_button = constants.button_state["button_up"]

    # 'Start button' sets it to button up
    start_button = constants.button_state["button_up"]

    # 'Select button' sets is to button up
    select_button = constants.button_state["button_up"]

    # The next portion is to set up the sound
    # this sets a variable to the wav file that holds the sound
    pew_sound = open("pew.wav", "rb")

    # uses the audio library in ugame
    sound = ugame.audio

    # makes sure there is no sound in the beginning
    sound.stop()

    # makes sure that sound isn't muted
    sound.mute(False)

    # creates the 10 by 8 image grid, sets it to background
    background = stage.Grid(
        image_bank_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y
    )

    # creates the ship sprite and sets it to the index 5 of the sprite list
    # puts it to 75,66 on the screen
    ship = stage.Sprite(
        image_bank_sprites, 5, 75, constants.SCREEN_Y - (2 * constants.SPRITE_SIZE)
    )

    # creates the alien sprite and sets it to index 9 of the sprite list
    alien = stage.Sprite(
        image_bank_sprites,
        9,
        int(constants.SCREEN_X / 2 - constants.SPRITE_SIZE / 2),
        16,
    )

    # 60 means 60 hertz which will update it 60 times per second
    game = stage.Stage(ugame.display, constants.FPS)

    # accesses the first layer(background) and makes the list of images for the background
    game.layers = [ship] + [alien] + [background]

    # takes layers and shows them on the screen
    game.render_block()

    # this is the game loop so it is supposed to loop forever
    while True:
        # Get user input
        # getting the buttons that are pressed - 60 times a second
        keys = ugame.buttons.get_pressed()

        # The if statements decide what to do when a button is pressed
        if keys & ugame.K_X:
            pass
        if keys & ugame.K_O != 0:
            if a_button == constants.button_state["button_up"]:
                a_button = constants.button_state["button_just_pressed"]
            elif a_button == constants.button_state["button_just_pressed"]:
                a_button = constants.button_state["button_still_pressed"]
        else:
            if a_button == constants.button_state["button_still_pressed"]:
                a_button = constants.button_state["button_released"]
            else:
                a_button = constants.button_state["button_up"]
        if keys & ugame.K_START:
            pass
        if keys & ugame.K_SELECT:
            pass
        if keys & ugame.K_RIGHT:
            if ship.x <= constants.SCREEN_X - constants.SPRITE_SIZE:
                # Moves the ship right
                ship.move(ship.x + 1, ship.y)
            else:
                # stops the ship at the right edge of the screen
                ship.move(constants.SCREEN_X - constants.SPRITE_SIZE, ship.y)
        if keys & ugame.K_LEFT:
            # Checks to ensure the ship is still on screen
            if ship.x >= 0:
                # moves the ship left
                ship.move(ship.x - 1, ship.y)
            else:
                # Stops at the left edge of the screen
                ship.move(0, ship.y)
        if keys & ugame.K_UP:
            # moves the ship up
            pass
        if keys & ugame.K_DOWN:
            # moves the ship down
            pass

        # update game logic

        # play the pew sound if the A button was just pressed ( in the button_just_pressed state)
        if a_button == constants.button_state["button_just_pressed"]:
            sound.play(pew_sound)

        # redraw sprites
        # refreshes the ship sprite
        game.render_sprites([ship] + [alien])

        # wait until the specified 60th of a second is reached
        game.tick()


if __name__ == "__main__":
    menu_scene()
