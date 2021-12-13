import arcade
import random
import os


# constants

SPRITE_SCALING = 0.2
SPRITE_SCALING_COIN = 0.01
SPRITE_SCALING_BARRIER = 0.11
SPRITE_SCALING_WALL = 0.21
SPRITE_SCALING_GEM = 0.05
SPRITE_SCALING_KNIFE = 0.2

VIEWPOINT_MARGIN = 200

CAMERA_SPEED = 0.1

DEFAULT_SCREEN_WIDTH = 1050
DEFAULT_SCREEN_HEIGHT = 800
SCREEN_TITLE = "Final Lab"

NUMBER_OF_COIN = 30
MOVEMENT_SPEED = 4
NUMBER_OF_GEM = 20
KNIFE_COUNT = 15

print("Welcome to Coin Collector!Collect the gems and coins to win the game. Avoid the knifes!")

# sounds

sound_one = arcade.load_sound("arcade_resources_sounds_coin4.wav")
sound_two = arcade.load_sound("sound_two.wav")
sound_three = arcade.load_sound("The-Northern-Path.mp3")

arcade.play_sound(sound_three)

class MyGame(arcade.Window):
    # This class represents the main window of the game
    def __init__(self, width, height, title):

        super().__init__(width, height, title)

        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        # Sprite Lists
        self.all_sprites_list = None
        self.coin_list = None
        self.wall_list = None
        self.gem_list = None
        self.score = 0
        self.player_sprite = None
        self.barrier_list = None
        self.knife_list = None
        self.physics_engine = None

        # Makes the screen scroll
        self.camera_sprites = arcade.Camera(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT)
        self.camera_gui = arcade.Camera(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT)

    def setup(self):

    # Sprite lists
        self.all_sprites_list = arcade.SpriteList()
        self.barrier_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.gem_list = arcade.SpriteList()
        self.knife_list = arcade.SpriteList()

    # Creating Player
        self.player_sprite = arcade.Sprite("paceman4.png", SPRITE_SCALING)
        self.player_sprite.center_x = 60
        self.player_sprite.center_y = 74

    # Create barrier and placement of barriers
        barrier = arcade.Sprite("barrier.png", SPRITE_SCALING_BARRIER)
        barrier.center_x = 300
        barrier.center_y = 100
        self.barrier_list.append(barrier)
        coordinate_list = [[340, 100], [380, 100], [420, 100], [460, 100], [500, 100], [540, 100],
                           [580, 100]]
        for coordinate in coordinate_list:
            barrier = arcade.Sprite("barrier.png", SPRITE_SCALING_BARRIER)
            barrier.center_x = coordinate[0]
            barrier.center_y = coordinate[1]
            self.barrier_list.append(barrier)

        barrier = arcade.Sprite("barrier.png", SPRITE_SCALING_BARRIER)
        barrier.center_x = 300
        barrier.center_y = 465
        self.barrier_list.append(barrier)
        coordinate_list = [[340, 465], [380, 465], [420, 465], [460, 465], [460, 340], [460, 300],
                           [460, 260]]
        for coordinate in coordinate_list:
            barrier = arcade.Sprite("barrier.png", SPRITE_SCALING_BARRIER)
            barrier.center_x = coordinate[0]
            barrier.center_y = coordinate[1]
            self.barrier_list.append(barrier)

        barrier = arcade.Sprite("barrier.png", SPRITE_SCALING_BARRIER)
        barrier.center_x = 300
        barrier.center_y = 425
        self.barrier_list.append(barrier)
        coordinate_list = [[300, 385], [300, 345]]
        for coordinate in coordinate_list:
            barrier = arcade.Sprite("barrier.png", SPRITE_SCALING_BARRIER)
            barrier.center_x = coordinate[0]
            barrier.center_y = coordinate[1]
            self.barrier_list.append(barrier)

        barrier = arcade.Sprite("barrier.png", SPRITE_SCALING_BARRIER)
        barrier.center_x = 210
        barrier.center_y = 250
        self.barrier_list.append(barrier)
        coordinate_list = [[160, 250], [112, 250], [60, 250]]
        for coordinate in coordinate_list:
            barrier = arcade.Sprite("barrier.png", SPRITE_SCALING_BARRIER)
            barrier.center_x = coordinate[0]
            barrier.center_y = coordinate[1]
            self.barrier_list.append(barrier)

    # Create walls and placement of walls
        wall = arcade.Sprite("wall.png", SPRITE_SCALING_WALL)
        wall.center_x = -100
        wall.center_y = 25
        self.barrier_list.append(wall)
        coordinate_list = [[-100, 75], [-100, 125], [-100, 175], [-100, 225], [-100, 275], [-100, 325],
                           [-100, 375], [-100, 425], [-100, 475], [-100, 525], [-100, 575], [-100, 625],
                           [-100, 675], [-100, 725], [-100, 775], [-100, 825], [-50, 825], [0, 825],
                           [50, 825], [100, 825], [150, 825], [200, 825], [250, 825], [300, 825], [350, 825],
                           [400, 825], [450, 825], [500, 825], [550, 825], [600, 825], [650, 825],
                           [650, 875], [650, 925], [650, 975], [700, 975], [750, 975], [800, 975],
                           [850, 975], [900, 975], [950, 975]]
        for coordinate in coordinate_list:
            wall = arcade.Sprite("wall.png", SPRITE_SCALING_WALL)
            wall.center_x = coordinate[0]
            wall.center_y = coordinate[1]
            self.barrier_list.append(wall)

        wall = arcade.Sprite("wall.png", SPRITE_SCALING_WALL)
        wall.center_x = 65
        wall.center_y = 600
        self.barrier_list.append(wall)
        coordinate_list = [[130, 600], [195, 600], [260, 600], [325, 600], [390, 600], [455, 600],
                           [520, 600], [585, 600], [650, 600]]
        for coordinate in coordinate_list:
            wall = arcade.Sprite("wall.png", SPRITE_SCALING_WALL)
            wall.center_x = coordinate[0]
            wall.center_y = coordinate[1]
            self.barrier_list.append(wall)

        wall = arcade.Sprite("wall.png", SPRITE_SCALING_WALL)
        wall.center_x = 801
        wall.center_y = 600
        self.barrier_list.append(wall)
        coordinate_list = [[801, 25], [801, 75], [801, 125], [801, 175], [801, 225], [801, 275], [801, 325],
                           [801, 375], [801, 425], [801, 475], [801, 525], [801, 575], [801, 625],
                           [801, 675], [801, 725], [801, 775], [801, 825]]
        for coordinate in coordinate_list:
            wall = arcade.Sprite("wall.png", SPRITE_SCALING_WALL)
            wall.center_x = coordinate[0]
            wall.center_y = coordinate[1]
            self.barrier_list.append(wall)

        wall = arcade.Sprite("wall.png", SPRITE_SCALING_WALL)
        wall.center_x = -30
        wall.center_y = 1
        self.barrier_list.append(wall)
        coordinate_list = [[40, 1], [110, 1], [155, 1], [200, 1], [245, 1], [290, 1], [335, 1],
                           [380, 1], [425, 1], [470, 1], [515, 1], [560, 1], [605, 1], [650, 1],
                           [695, 1], [740, 1], [800, 1], [850, 1], [900, 1], [950, 1], [1000, 1],
                           [1050, 1], [1100, 1], [1150, 1]]
        for coordinate in coordinate_list:
            wall = arcade.Sprite("wall.png", SPRITE_SCALING_WALL)
            wall.center_x = coordinate[0]
            wall.center_y = coordinate[1]
            self.barrier_list.append(wall)

        barrier = arcade.Sprite("barrier.png", SPRITE_SCALING_BARRIER)
        barrier.center_x = 1170
        barrier.center_y = 40
        self.barrier_list.append(barrier)
        coordinate_list = [[1170, 100], [1170, 160], [1170, 220], [1170, 280], [1170, 340], [1170, 400],
                           [1170, 460], [1170, 520], [1170, 580], [1170, 640], [1170, 700],
                           [1170, 760], [1170, 820], [1170, 880], [1170, 940], [1170, 990],
                           [1120, 990], [1070, 990], [1015, 990]]
        for coordinate in coordinate_list:
            barrier = arcade.Sprite("barrier.png", SPRITE_SCALING_BARRIER)
            barrier.center_x = coordinate[0]
            barrier.center_y = coordinate[1]
            self.barrier_list.append(barrier)

        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.barrier_list)

        # Creating Gem
        for i in range(NUMBER_OF_GEM):

            gem = arcade.Sprite("purepng.com-dragon-fruitfruitsdragon-fruitpitayapitahaya-981524762841msxvf.png", SPRITE_SCALING_GEM)

            gem_placed_successfully = False

            while not gem_placed_successfully:

                gem.center_x = random.randrange(DEFAULT_SCREEN_WIDTH)
                gem.center_y = random.randrange(DEFAULT_SCREEN_HEIGHT)

                barrier_hit_list = arcade.check_for_collision_with_list(gem, self.barrier_list)

                gem_hit_list = arcade.check_for_collision_with_list(gem, self.coin_list)

                if len(barrier_hit_list) == 0 and len(gem_hit_list) == 0:

                    gem_placed_successfully = True

            self.coin_list.append(gem)
            arcade.play_sound(sound_one)

        # Creating Coin
        for i in range(NUMBER_OF_COIN):

            coin = arcade.Sprite("coin.png", SPRITE_SCALING_COIN)

            coin_placed_successfully = False

            while not coin_placed_successfully:

                coin.center_x = random.randrange(DEFAULT_SCREEN_WIDTH)
                coin.center_y = random.randrange(DEFAULT_SCREEN_HEIGHT)

                barrier_hit_list = arcade.check_for_collision_with_list(coin, self.barrier_list)

                coin_hit_list = arcade.check_for_collision_with_list(coin, self.coin_list)

                if len(barrier_hit_list) == 0 and len(coin_hit_list) == 0:
                    coin_placed_successfully = True

            self.coin_list.append(coin)
            arcade.play_sound(sound_one)

        # Creating Knife(need to avoid)
        for i in range(KNIFE_COUNT):

            knife = arcade.Sprite("bloody-knife-png-23.png", SPRITE_SCALING_KNIFE)

            knife_placed_successfully = False

            while not knife_placed_successfully:

                knife.center_x = random.randrange(DEFAULT_SCREEN_WIDTH)
                knife.center_y = random.randrange(DEFAULT_SCREEN_HEIGHT)

                barrier_hit_list = arcade.check_for_collision_with_list(knife, self.barrier_list)

                knife_hit_list = arcade.check_for_collision_with_list(knife, self.coin_list)

                if len(barrier_hit_list) == 0 and len(knife_hit_list) == 0:
                    knife_placed_successfully = True

            self.knife_list.append(knife)
            arcade.play_sound(sound_two)


        # Background setting
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        arcade.start_render()

        # draw the sprites
        self.camera_sprites.use()
        self.barrier_list.draw()
        self.coin_list.draw()
        self.wall_list.draw()
        self.gem_list.draw()
        self.knife_list.draw()
        self.player_sprite.draw()
        self.camera_gui.use()

        # Score
        output = f"score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.LIGHT_BLUE, 24)

        # Game Over
        if self.score >= 50:
            arcade.draw_text("Game Over", DEFAULT_SCREEN_WIDTH / 2, DEFAULT_SCREEN_HEIGHT / 2, arcade.color.WHITE, 80,
                             anchor_x="center")

    # Called whenever a key is pressed
    def on_key_press(self, key, modifiers):
        if self.score < 50:

            if key == arcade.key.UP:
                self.player_sprite.change_y = MOVEMENT_SPEED
            elif key == arcade.key.DOWN:
                self.player_sprite.change_y = -MOVEMENT_SPEED
            elif key == arcade.key.LEFT:
                self.player_sprite.change_x = -MOVEMENT_SPEED
            elif key == arcade.key.RIGHT:
                self.player_sprite.change_x = MOVEMENT_SPEED

    # Called whenever the user releases a key
    def on_key_release(self, key, modifiers):

        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0

    # Movement and logic of the game
    def on_update(self, delta_time):
        self.physics_engine.update()
        if self.score < 50:
            self.coin_list.update()
            coin_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.coin_list)
            for coin in coin_hit_list:
                self.score += 1
                arcade.play_sound(sound_one)
                coin.remove_from_sprite_lists()

        self.scroll_to_player()

    def scroll_to_player(self):
        position = self.player_sprite.center_x - self.width / 2, \
                   self.player_sprite.center_y - self.height / 2
        self.camera_sprites.move_to(position, CAMERA_SPEED)

    def on_resize(self, width, height):
        self.camera_sprites.resize(int(width), int(height))
        self.camera_gui.resize(int(width), int(height))



def main():
    # Main method
    window = MyGame(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()