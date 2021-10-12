import arcade

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.ASH_GREY)

    def on_draw(self):
        arcade.start_render()

def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT,
                       "Drawing Example")
    arcade.run()


main()