import arcade
import random
import os

SPRITE_SCALING = 0.5
SPRITE_SCALING_GEM = 0.15
SPRITE_SCALING_BARRIER = 0.09
SPRITE_SCALING_WALL = 0.09

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Lab 9"

NUMBER_OF_GEMS = 20
MOVEMENT_SPEED = 4

sound_one = arcade.load_sound("arcade_resources_sounds_coin4.wav")


class MyGame(arcade.Window):
    def __init__(self, width, height, title):

        super().__init__(width, height, title)

        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        self.all_sprites_list = None
        self.gem_list = None
        self.wall_list = None
        self.score = 0
        self.player_sprite = None
        self.barrier_list = None
        self.physics_engine = None

    def setup(self):

        self.all_sprites_list = arcade.SpriteList()
        self.barrier_list = arcade.SpriteList()
        self.gem_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()

        self.player_sprite = arcade.Sprite("among_us_character_png-.png", SPRITE_SCALING)
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

        wall = arcade.Sprite("wall.png", SPRITE_SCALING_WALL)
        wall.center_x = 195
        wall.center_y = 570
        self.barrier_list.append(wall)
        wall = arcade.Sprite("wall.png", SPRITE_SCALING_WALL)
        wall.center_x = 195
        wall.center_y = 535
        self.barrier_list.append(wall)
        wall = arcade.Sprite("wall.png", SPRITE_SCALING_WALL)
        wall.center_x = 775
        wall.center_y = 400
        self.barrier_list.append(wall)
        wall = arcade.Sprite("wall.png", SPRITE_SCALING_WALL)
        wall.center_x = 730
        wall.center_y = 400
        self.barrier_list.append(wall)
        wall = arcade.Sprite("wall.png", SPRITE_SCALING_WALL)
        wall.center_x = 685
        wall.center_y = 400
        self.barrier_list.append(wall)
        barrier = arcade.Sprite("barrier.png", SPRITE_SCALING_BARRIER)
        barrier.center_x = 540
        barrier.center_y = 235
        self.barrier_list.append(barrier)
        barrier = arcade.Sprite("barrier.png", SPRITE_SCALING_BARRIER)
        barrier.center_x = 540
        barrier.center_y = 275
        self.barrier_list.append(barrier)
        barrier = arcade.Sprite("barrier.png", SPRITE_SCALING_BARRIER)
        barrier.center_x = 540
        barrier.center_y = 315
        self.barrier_list.append(barrier)
        barrier = arcade.Sprite("barrier.png", SPRITE_SCALING_BARRIER)
        barrier.center_x = 580
        barrier.center_y = 157
        self.barrier_list.append(barrier)
        wall = arcade.Sprite("wall.png", SPRITE_SCALING_WALL)
        wall.center_x = 785
        wall.center_y = 200
        self.barrier_list.append(wall)
        wall = arcade.Sprite("wall.png", SPRITE_SCALING_WALL)
        wall.center_x = 745
        wall.center_y = 200
        self.barrier_list.append(wall)
        wall = arcade.Sprite("wall.png", SPRITE_SCALING_WALL)
        wall.center_x = 705
        wall.center_y = 200
        self.barrier_list.append(wall)
        wall = arcade.Sprite("wall.png", SPRITE_SCALING_WALL)
        wall.center_x = 195
        wall.center_y = 55
        self.barrier_list.append(wall)
        wall = arcade.Sprite("wall.png", SPRITE_SCALING_WALL)
        wall.center_x = 195
        wall.center_y = 90
        self.barrier_list.append(wall)
        wall = arcade.Sprite("wall.png", SPRITE_SCALING_WALL)
        wall.center_x = 195
        wall.center_y = 125
        self.barrier_list.append(wall)
        wall = arcade.Sprite("wall.png", SPRITE_SCALING_WALL)
        wall.center_x = 40
        wall.center_y = 220
        self.barrier_list.append(wall)
        wall = arcade.Sprite("wall.png", SPRITE_SCALING_WALL)
        wall.center_x = 76
        wall.center_y = 220
        self.barrier_list.append(wall)
        wall = arcade.Sprite("wall.png", SPRITE_SCALING_WALL)
        wall.center_x = 425
        wall.center_y = 350
        self.barrier_list.append(wall)

        for i in range(NUMBER_OF_GEMS):

            gem = arcade.Sprite("gem.png", SPRITE_SCALING_GEM)

            gem_placed_successfully = False

            while not gem_placed_successfully:

                gem.center_x = random.randrange(SCREEN_WIDTH)
                gem.center_y = random.randrange(SCREEN_HEIGHT)

                barrier_hit_list = arcade.check_for_collision_with_list(gem, self.barrier_list)

                gem_hit_list = arcade.check_for_collision_with_list(gem, self.gem_list)

                if len(barrier_hit_list) == 0 and len(gem_hit_list) == 0:

                    gem_placed_successfully = True

            self.gem_list.append(gem)

        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.barrier_list)

        arcade.set_background_color(arcade.color.GRAY)

    def on_draw(self):
        arcade.start_render()
        self.barrier_list.draw()
        self.gem_list.draw()
        self.wall_list.draw()
        self.player_sprite.draw()

        output = f"score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.BLACK, 24)

        if self.score >= 20:
            arcade.draw_text("Game Over", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, arcade.color.BLACK, 80,
                             anchor_x="center")

    def on_key_press(self, key, modifiers):
        if self.score < 20:

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
        if self.score < 20:
            self.gem_list.update()
            gem_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.gem_list)
            for gem in gem_hit_list:
                self.score += 1
                arcade.play_sound(sound_one)
                gem.remove_from_sprite_lists()


def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
