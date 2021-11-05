"""
No coins on the walls

Simple program to show basic sprite usage. Specifically, create coin sprites that
aren't on top of any walls, and don't have coins on top of each other.

Artwork from https://kenney.nl

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.sprite_no_coins_on_walls
"""
import arcade
import random
import os

SPRITE_SCALING = 0.5
SPRITE_SCALING_GEM = 0.2

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Sprite No Coins on Walls Example"

NUMBER_OF_GEMS = 50

MOVEMENT_SPEED = 5


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height, title):
        """
        Initializer
        """
        super().__init__(width, height, title)

        # Set the working directory (where we expect to find files) to the same
        # directory this .py file is in. You can leave this out of your own
        # code, but it is needed to easily run the examples using "python -m"
        # as mentioned at the top of this program.
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        # Sprite lists
        self.all_sprites_list = None
        self.gem_list = None

        # Set up the player
        self.player_sprite = None
        self.barrier_list = None
        self.physics_engine = None

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.all_sprites_list = arcade.SpriteList()
        self.barrier_list = arcade.SpriteList()
        self.gem_list = arcade.SpriteList()

        # Set up the player
        self.player_sprite = arcade.Sprite("pac man.png",
                                           SPRITE_SCALING)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 64

        # -- Set up the walls
        # Create a series of horizontal walls
        for y in range(0, 800, 200):
            for x in range(100, 700, 64):
                barrier = arcade.Sprite("barrier-pattern.png", SPRITE_SCALING)
                barrier.center_x = x
                barrier.center_y = y
                self.barrier_list.append(barrier)

        # -- Randomly place coins where there are no walls
        # Create the coins
        for i in range(NUMBER_OF_GEMS):

            # Create the coin instance
            # Coin image from kenney.nl
            gem = arcade.Sprite("gem.png", SPRITE_SCALING_GEM)

            # --- IMPORTANT PART ---

            # Boolean variable if we successfully placed the coin
            gem_placed_successfully = False

            # Keep trying until success
            while not gem_placed_successfully:
                # Position the coin
                gem.center_x = random.randrange(SCREEN_WIDTH)
                gem.center_y = random.randrange(SCREEN_HEIGHT)

                # See if the coin is hitting a wall
                barrier_hit_list = arcade.check_for_collision_with_list(gem, self.barrier_list)

                # See if the coin is hitting another coin
                gem_hit_list = arcade.check_for_collision_with_list(gem, self.gem_list)

                if len(barrier_hit_list) == 0 and len(gem_hit_list) == 0:
                    # It is!
                    gem_placed_successfully = True

            # Add the coin to the lists
            self.gem_list.append(gem)

            # --- END OF IMPORTANT PART ---

        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.barrier_list)

        # Set the background color
        arcade.set_background_color(arcade.color.AMAZON)

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        arcade.start_render()

        # Draw all the sprites.
        self.barrier_list.draw()
        self.gem_list.draw()
        self.player_sprite.draw()

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.UP:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0

    def on_update(self, delta_time):
        """ Movement and game logic """

        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        self.physics_engine.update()


def main():
    """ Main function """
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()