import arcade
import random
import os

SPRITE_SCALING = 0.2
SPRITE_SCALING_COIN = 0.01
SPRITE_SCALING_BARRIER = 0.11
SPRITE_SCALING_WALL = 0.21
SPRITE_SCALING_GEM = 0.1

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Final Lab"

NUMBER_OF_COIN = 20
MOVEMENT_SPEED = 4
NUMBER_OF_GEM = 15

print("Get ready to play Coin Collector!")

sound_one = arcade.load_sound("arcade_resources_sounds_coin4.wav")
sound_two = arcade.load_sound("sound_two.wav")


class MyGame(arcade.Window):
    def __init__(self, width, height, title):

        super().__init__(width, height, title)

        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        self.all_sprites_list = None
        self.coin_list = None
        self.wall_list = None
        self.gem_list = None
        self.score = 0
        self.player_sprite = None
        self.barrier_list = None
        self.physics_engine = None

    def setup(self):

        self.all_sprites_list = arcade.SpriteList()
        self.barrier_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.gem_list = arcade.SpriteList()

        self.player_sprite = arcade.Sprite("paceman4.png", SPRITE_SCALING)
        self.player_sprite.center_x = 60
        self.player_sprite.center_y = 74

        barrier = arcade.Sprite("barrier.png", SPRITE_SCALING_BARRIER)
        barrier.center_x = 300
        barrier.center_y = 195
        self.barrier_list.append(barrier)
        coordinate_list = [[340, 195], [380, 195], [420, 195], [460, 195], [500, 195], [540, 195],
                           [580, 195]]
        for coordinate in coordinate_list:
            barrier = arcade.Sprite("barrier.png", SPRITE_SCALING_BARRIER)
            barrier.center_x = coordinate[0]
            barrier.center_y = coordinate[1]
            self.barrier_list.append(barrier)

        barrier = arcade.Sprite("barrier.png", SPRITE_SCALING_BARRIER)
        barrier.center_x = 300
        barrier.center_y = 465
        self.barrier_list.append(barrier)
        coordinate_list = [[340, 465], [380, 465], [420, 465], [460, 465], [500, 465], [540, 465],
                           [580, 465]]
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
        barrier.center_x = 260
        barrier.center_y = 345
        self.barrier_list.append(barrier)
        coordinate_list = [[220, 345], [180, 345], [140, 345]]
        for coordinate in coordinate_list:
            barrier = arcade.Sprite("barrier.png", SPRITE_SCALING_BARRIER)
            barrier.center_x = coordinate[0]
            barrier.center_y = coordinate[1]
            self.barrier_list.append(barrier)

        wall = arcade.Sprite("wall.png", SPRITE_SCALING_WALL)
        wall.center_x = -1
        wall.center_y = 25
        self.barrier_list.append(wall)
        coordinate_list = [[-1, 75], [-1, 125], [-1, 175], [-1, 225], [-1, 275], [-1, 325],
                           [-1, 375], [-1, 425], [-1, 475], [-1, 525], [-1, 575]]
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
                           [520, 600], [585, 600], [650, 600], [715, 600], [770, 600]]
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
        wall.center_x = 65
        wall.center_y = 20
        self.barrier_list.append(wall)
        coordinate_list = [[130, 20], [195, 20], [260, 20], [325, 20], [390, 20], [455, 20],
                           [520, 20], [585, 20], [650, 20], [715, 20], [770, 20]]
        for coordinate in coordinate_list:
            wall = arcade.Sprite("wall.png", SPRITE_SCALING_WALL)
            wall.center_x = coordinate[0]
            wall.center_y = coordinate[1]
            self.barrier_list.append(wall)

        for i in range(NUMBER_OF_GEM):

            gem = arcade.Sprite("fruit.png", SPRITE_SCALING_GEM)

            gem_placed_successfully = False

            while not gem_placed_successfully:

                gem.center_x = random.randrange(SCREEN_WIDTH)
                gem.center_y = random.randrange(SCREEN_HEIGHT)

                barrier_hit_list = arcade.check_for_collision_with_list(gem, self.barrier_list)

                gem_hit_list = arcade.check_for_collision_with_list(gem, self.coin_list)

                if len(barrier_hit_list) == 0 and len(gem_hit_list) == 0:

                    gem_placed_successfully = True

            self.coin_list.append(gem)
            arcade.play_sound(sound_one)

        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.barrier_list)

        for i in range(NUMBER_OF_COIN):

            coin = arcade.Sprite("coin.png", SPRITE_SCALING_COIN)

            coin_placed_successfully = False

            while not coin_placed_successfully:

                coin.center_x = random.randrange(SCREEN_WIDTH)
                coin.center_y = random.randrange(SCREEN_HEIGHT)

                barrier_hit_list = arcade.check_for_collision_with_list(coin, self.barrier_list)

                coin_hit_list = arcade.check_for_collision_with_list(coin, self.coin_list)

                if len(barrier_hit_list) == 0 and len(coin_hit_list) == 0:
                    coin_placed_successfully = True

            self.coin_list.append(coin)
            arcade.play_sound(sound_one)

        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        arcade.start_render()
        self.barrier_list.draw()
        self.coin_list.draw()
        self.wall_list.draw()
        self.gem_list.draw()
        self.player_sprite.draw()

        output = f"score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.BLACK, 24)

        if self.score >= 35:
            arcade.draw_text("Game Over", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, arcade.color.WHITE, 80,
                             anchor_x="center")

    def on_key_press(self, key, modifiers):
        if self.score < 35:

            if key == arcade.key.UP:
                self.player_sprite.change_y = MOVEMENT_SPEED
            elif key == arcade.key.DOWN:
                self.player_sprite.change_y = -MOVEMENT_SPEED
            elif key == arcade.key.LEFT:
                self.player_sprite.change_x = -MOVEMENT_SPEED
            elif key == arcade.key.RIGHT:
                self.player_sprite.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):

        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0

    def on_update(self, delta_time):
        self.physics_engine.update()
        if self.score < 35:
            self.coin_list.update()
            coin_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.coin_list)
            for coin in coin_hit_list:
                self.score += 1
                arcade.play_sound(sound_one)
                coin.remove_from_sprite_lists()


def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()