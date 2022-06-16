#!/usr/bin/env python3
# Created By: Alex De Meo
# Date: 03/25/2022
# Description: This is my CPT game for the edgebadge


import constants
import time
import random
import stage
import ugame


def splash_scene():
    # this function is the main game scene

    # set a var to hold the soumd
    coin_sound = open("coin.wav", "rb")

    # accesses audio library
    sound = ugame.audio

    # Stops sound from playing
    sound.stop()

    # Ensures unmuted
    sound.mute(False)

    # Plays the coin sound at the beginning of the splash screen
    sound.play(coin_sound)

    # accesses the image bank and setting it to a variable st index 0
    image_bank_mt_background = stage.Bank.from_bmp16("mt_game_studio.bmp")

    # creates the 10 by 8 image grid, sets it to background
    background = stage.Grid(
        image_bank_mt_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y
    )

    # creates the 10 by 8 image grid, sets it to background
    # this allows us to knit together an image
    background = stage.Grid(
        image_bank_mt_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y
    )

    # used this program to split the image into tile:

    #   https://ezgif.com/sprite-cutter/ezgif-5-818cdbcc3f66.png

    background.tile(2, 2, 0)  # blank white
    background.tile(3, 2, 1)
    background.tile(4, 2, 2)
    background.tile(5, 2, 3)
    background.tile(6, 2, 4)
    background.tile(7, 2, 0)  # blank white

    background.tile(2, 3, 0)  # blank white
    background.tile(3, 3, 5)
    background.tile(4, 3, 6)
    background.tile(5, 3, 7)
    background.tile(6, 3, 8)
    background.tile(7, 3, 0)  # blank white

    background.tile(2, 4, 0)  # blank white
    background.tile(3, 4, 9)
    background.tile(4, 4, 10)
    background.tile(5, 4, 11)
    background.tile(6, 4, 12)
    background.tile(7, 4, 0)  # blank white

    background.tile(2, 5, 0)  # blank white
    background.tile(3, 5, 0)
    background.tile(4, 5, 13)
    background.tile(5, 5, 14)
    background.tile(6, 5, 0)
    background.tile(7, 5, 0)  # blank white

    # 60 means 60 hertz which will update it 60 times per second
    game = stage.Stage(ugame.display, constants.FPS)

    # accesses the first layer(background) and makes the list of images for the background
    game.layers = [background]

    # takes layers and shows them on the screen
    game.render_block()

    # this is the game loop so it is supposed to loop forever
    while True:
        # wait for two seconds
        time.sleep(2.0)

        # goes to the menu
        menu_scene()


def menu_scene():
    # his function is the main game scene

    # accesses the image bank and setting it to a variable st index 0
    image_bank_mt_background = stage.Bank.from_bmp16("mt_game_studio.bmp")

    # new variable called text set to list
    text = []

    # variable makes a piece of text // pallette selects the color
    name_text = stage.Text(
        width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None
    )

    # moves the cursor to this location
    name_text.move(5, 10)

    # What the text is going to say
    name_text.text("DE MEO GAME STUDIOS")

    # adds it to the list
    text.append(name_text)

    # making another text object
    start_text = stage.Text(
        width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None
    )

    # moves the cursor to this location
    start_text.move(35, 110)

    # What the text will say
    start_text.text("PRESS START!")

    # adding to text list
    text.append(start_text)

    # creates the 10 by 8 image grid, sets it to background
    background = stage.Grid(
        image_bank_mt_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y
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
            print("Start")
            game_scene()

        # wait until the specified 60th of a second is reached
        game.tick()


def game_scene():
    # his function is the main game scene
    # keeps track of the score
    score = 0

    def show_alien():
        # This function takes an alien from off screen and puts it onscreen
        for alien_number in range(len(aliens)):
            # makes sure alien is off screen
            if aliens[alien_number].x < 0:
                aliens[alien_number].move(random.randint(0 + constants.SPRITE_SIZE, constants.SCREEN_X - constants.SPRITE_SIZE), constants.OFF_TOP_SCREEN)
                break

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

    boom_sound = open("boom.wav", 'rb')

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

    # This loop creates a random background with the tiles
    # first for loop goes through the x axis
    for x_location in range(constants.SCREEN_GRID_X):
        # this loop goes through the y axis
        for y_location in range(constants.SCREEN_GRID_Y):
            # picks a random tile from the background
            tile_picked = random.randint(1, 3)

            # places tile at the specified location
            background.tile(x_location, y_location, tile_picked)

    # creates the ship sprite and sets it to the index 5 of the sprite list
    # puts it to 75,66 on the screen
    ship = stage.Sprite(
        image_bank_sprites, 5, 75, constants.SCREEN_Y - (2 * constants.SPRITE_SIZE)
    )

    # creates the alien sprites and sets it to index 9 of the sprite list
    aliens = []
    for lazer_number in range(constants.TOTAL_NUMBER_OF_ALIENS):
        # creates an alien and sets it off screen
        a_single_alien = stage.Sprite(image_bank_sprites, 9, constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)

        # adds alien to aliens list
        aliens.append(a_single_alien)

    # funtion places 1 alien on the screen
    show_alien()
    
    # Creates a list for the lazers we will have on screen
    lazers = []

    # loop is to make the lazers
    for lazer_number in range(constants.TOTAL_NUMBER_OF_LAZERS):
        # Creates a lazer sprite and puts it off the screen
        a_single_lazer = stage.Sprite(image_bank_sprites, 10, constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)

        # add to the list
        lazers.append(a_single_lazer)

    # 60 means 60 hertz which will update it 60 times per second
    game = stage.Stage(ugame.display, constants.FPS)

    # accesses the first layer(background) and makes the list of images for the background
    game.layers = lazers + [ship] + aliens + [background]

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
            for lazer_number in range(len(lazers)):
                # Makes sure the lazer is stil off screen
                if lazers[lazer_number].x < 0:
                    # moves the lazer to the ship location
                    lazers[lazer_number].move(ship.x, ship.y)

                    # plays sound
                    sound.play(pew_sound)
                    break
        
        for lazer_number in range(len(lazers)):
            if lazers[lazer_number].x > 0:
                # if the lazer is on the screen, it will move the lazer up the screen
                lazers[lazer_number].move(lazers[lazer_number].x, lazers[lazer_number].y - constants.LAZER_SPEED)

                if lazers[lazer_number].y < constants.OFF_TOP_SCREEN:
                    # if lazer is now off screen, it moves it to its resting position
                    lazers[lazer_number].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)

        for alien_number in range(len(aliens)):
            if aliens[alien_number].x > 0:
                # moves the alien down the screen if it is on screen
                aliens[alien_number].move(aliens[alien_number].x, aliens[alien_number].y + constants.ALIEN_SPEED)

                if aliens[alien_number].y > constants.SCREEN_Y:
                    # when the alien goes off the screen, it moves the alien to its resting position
                    aliens[alien_number].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)

                    # displays another alien
                    show_alien()

        for lazer_number in range(len(lazers)):
            # ensures it is referencing a lazer on screen
            if lazers[lazer_number].x > 0:
                for alien_number in range(len(aliens)):
                    # ensures it is referencing an alien that is on screem
                    if aliens[alien_number].x > 0:
                        # This if statement checks to see if both the x and y axis of both the alien and lazer cross each other. If they cross its a hit, if  not continue on
                        if stage.collide(lazers[lazer_number].x + 6, lazers[lazer_number].y + 2, lazers[lazer_number].x + 11, lazers[lazer_number].y + 12, aliens[alien_number].x + 1, aliens[alien_number].y, aliens[alien_number].x + 15, aliens[alien_number].y + 15):
                            # moves the alien off screen
                            aliens[alien_number].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)

                            # moves the lazer off screen
                            lazers[lazer_number].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)

                            # stops any previous sound playing
                            sound.stop()

                            # play the sound for the explosion
                            sound.play(boom_sound)

                            # update score
                            score += 1

                            # replace destroyed alien
                            show_alien()
                            show_alien()

        # redraw sprites
        # refreshes the ship sprite
        game.render_sprites(lazers +[ship] + aliens)

        # wait until the specified 60th of a second is reached
        game.tick()


if __name__ == "__main__":
    splash_scene()
                                                     