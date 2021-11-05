import arcade
import random
import os

SPRITE_SCALING = 0.5
SPRITE_SCALING_GEM = 0.15
SPRITE_SCALING_BARRIER = 0.09

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Lab 9"

NUMBER_OF_GEMS = 20
MOVEMENT_SPEED = 3


class MyGame(arcade.Window):
    def __init__(self, width, height, title):

        super().__init__(width, height, title)

        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        self.all_sprites_list = None
        self.gem_list = None
        self.score = 0
        self.player_sprite = None
        self.barrier_list = None
        self.physics_engine = None

    def setup(self):

        self.all_sprites_list = arcade.SpriteList()
        self.barrier_list = arcade.SpriteList()
        self.gem_list = arcade.SpriteList()

        self.player_sprite = arcade.Sprite("among_us_character_png-.png", SPRITE_SCALING)
        self.player_sprite.center_x = 60
        self.player_sprite.center_y = 74

        for y in range(60, 700, 135):
            for x in range(100, 800, 225):
                barrier = arcade.Sprite("barrier.png", SPRITE_SCALING_BARRIER)
                barrier.center_x = x
                barrier.center_y = y
                self.barrier_list.append(barrier)

        barrier = arcade.Sprite("barrier.png", SPRITE_SCALING_BARRIER)
        barrier.center_x = 340
        barrier.center_y = 195
        self.barrier_list.append(barrier)

        barrier = arcade.Sprite("barrier.png", SPRITE_SCALING_BARRIER)
        barrier.center_x = 380
        barrier.center_y = 195
        self.barrier_list.append(barrier)

        barrier = arcade.Sprite("barrier.png", SPRITE_SCALING_BARRIER)
        barrier.center_x = 420
        barrier.center_y = 195
        self.barrier_list.append(barrier)

        barrier = arcade.Sprite("barrier.png", SPRITE_SCALING_BARRIER)
        barrier.center_x = 300
        barrier.center_y = 195
        self.barrier_list.append(barrier)

        barrier = arcade.Sprite("barrier.png", SPRITE_SCALING_BARRIER)
        barrier.center_x = 460
        barrier.center_y = 195
        self.barrier_list.append(barrier)

        barrier = arcade.Sprite("barrier.png", SPRITE_SCALING_BARRIER)
        barrier.center_x = 340
        barrier.center_y = 465
        self.barrier_list.append(barrier)

        barrier = arcade.Sprite("barrier.png", SPRITE_SCALING_BARRIER)
        barrier.center_x = 380
        barrier.center_y = 465
        self.barrier_list.append(barrier)

        barrier = arcade.Sprite("barrier.png", SPRITE_SCALING_BARRIER)
        barrier.center_x = 420
        barrier.center_y = 465
        self.barrier_list.append(barrier)

        barrier = arcade.Sprite("barrier.png", SPRITE_SCALING_BARRIER)
        barrier.center_x = 300
        barrier.center_y = 465
        self.barrier_list.append(barrier)

        barrier = arcade.Sprite("barrier.png", SPRITE_SCALING_BARRIER)
        barrier.center_x = 460
        barrier.center_y = 465
        self.barrier_list.append(barrier)

        barrier = arcade.Sprite("barrier.png", SPRITE_SCALING_BARRIER)
        barrier.center_x = 500
        barrier.center_y = 195
        self.barrier_list.append(barrier)

        barrier = arcade.Sprite("barrier.png", SPRITE_SCALING_BARRIER)
        barrier.center_x = 778
        barrier.center_y = 120
        self.barrier_list.append(barrier)

        barrier = arcade.Sprite("barrier.png", SPRITE_SCALING_BARRIER)
        barrier.center_x = 778
        barrier.center_y = 535
        self.barrier_list.append(barrier)

        barrier = arcade.Sprite("barrier.png", SPRITE_SCALING_BARRIER)
        barrier.center_x = 778
        barrier.center_y = 395
        self.barrier_list.append(barrier)

        barrier = arcade.Sprite("barrier.png", SPRITE_SCALING_BARRIER)
        barrier.center_x = 778
        barrier.center_y = 265
        self.barrier_list.append(barrier)


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
        self.player_sprite.draw()

        output = f"score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.BLACK, 24)

    def on_key_press(self, key, modifiers):

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


def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
