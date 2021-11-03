import random
import arcade

SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_BALL = 0.2
SPRITE_SCALING_KNIFE = 0.2
BALL_COUNT = 12
KNIFE_COUNT = 15

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

sound_one = arcade.load_sound("sound_one.wav")
sound_two = arcade.load_sound("sound_two.wav")

class Knife(arcade.Sprite):
    def __init__(self, filename, sprite_scaling):

        super().__init__(filename, sprite_scaling)


    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.left < 0:
            self.change_x *= -1

        if self.right > SCREEN_WIDTH:
            self.change_x *= -1

        if self.bottom < 0:
            self.change_y *= -1

        if self.top > SCREEN_HEIGHT:
            self.change_y *= -1

class Ball(arcade.Sprite):
    def reset_pos(self):
        self.center_y = random.randrange(SCREEN_HEIGHT + 10,
                                        SCREEN_HEIGHT + 80)
        self.center_x = random.randrange(SCREEN_WIDTH)

    def update(self):
        self.center_y -= 1
        if self.top < 0:
            self.reset_pos()

class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "lab 8")

        self.player_list = None
        self.ball_list = None
        self.knife_list = None
        self.player_sprite = None
        self.score = 0
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.GRAY)

    def setup(self):
        self.player_list = arcade.SpriteList()
        self.ball_list = arcade.SpriteList()
        self.knife_list = arcade.SpriteList()
        self.score = 0
        self.player_sprite = arcade.Sprite("character.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 100
        self.player_sprite.center_y = 100
        self.player_list.append(self.player_sprite)

        for i in range(BALL_COUNT):
            ball = Ball("baseballe02.png", SPRITE_SCALING_BALL)
            ball.center_x = random.randrange(SCREEN_WIDTH)
            ball.center_y = random.randrange(SCREEN_HEIGHT)
            self.ball_list.append(ball)

        for i in range(KNIFE_COUNT):
            knife = Knife("bloody-knife-png-23.png", SPRITE_SCALING_KNIFE)
            knife.center_x = SCREEN_WIDTH / 2
            knife.center_y = i * 50
            knife.change_x = 2

            self.knife_list.append(knife)

    def on_draw(self):
        arcade.start_render()
        self.ball_list.draw()
        self.player_list.draw()
        self.knife_list.draw()

        output = f"score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.BLACK, 20)

    def on_mouse_motion(self, x, y, dx, dy):
        self.player_sprite.center_x = x
        self.player_sprite.center_y = y


    def update(self, delta_time):
        self.ball_list.update()
        balls_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.ball_list)

        for ball in balls_hit_list:
            ball.reset_pos()
            self.score += 1
            arcade.play_sound(sound_one)
        self.knife_list.update()
        knife_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.knife_list)

        for knife in knife_hit_list:
            self.score -= 1
            knife.remove_from_sprite_lists()
            arcade.play_sound(sound_two)

def main():
    window = MyGame()
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()