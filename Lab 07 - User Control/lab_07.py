""" Lab 7 """

import arcade

# --- Constants ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
MOVEMENT_SPEED = 3

class Snowball:
    def __init__(self, position_x, position_y, change_x, change_y, radius, color):

        # Take the parameters of the init function above,
        # and create instance variables out of them.
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.radius = radius
        self.color = color
        self.laser_sound = arcade.load_sound(":resources:sounds/explosion2.wav")

    def draw(self):
        """ Draw the balls with the instance variables we have. """
        arcade.draw_circle_filled(self.position_x + 140,
                                  self.position_y + 140,
                                  self.radius,
                                  self.color)

        arcade.draw_circle_filled(self.position_x + 70,
                                  self.position_y + 70,
                                  self.radius,
                                  self.color)

        arcade.draw_circle_filled(self.position_x,
                                  self.position_y,
                                  self.radius,
                                  self.color)

    def update(self):
        # Move the ball
        self.position_y += self.change_y
        self.position_x += self.change_x

        if self.position_x < self.radius:
            self.position_x = self.radius

        if self.position_x > SCREEN_WIDTH - self.radius:
            self.position_x = SCREEN_WIDTH - self.radius

        if self.position_y < self.radius:
            self.position_y = self.radius

        if self.position_y > SCREEN_HEIGHT - self.radius:
            self.position_y = SCREEN_HEIGHT - self.radius
            arcade.play_sound(self.laser_sound)

class Snowball_black:
    def __init__(self, position_x, position_y, change_x, change_y, radius, color):

        # Take the parameters of the init function above,
        # and create instance variables out of them.
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.radius = radius
        self.color = color
        self.laser_sound = arcade.load_sound(":resources:sounds/explosion2.wav")

    def draw(self):
        """ Draw the balls with the instance variables we have. """
        arcade.draw_circle_filled(self.position_x,
                                  self.position_y,
                                  self.radius,
                                  self.color)

        arcade.draw_circle_filled(self.position_x - 140,
                                  self.position_y - 140,
                                  self.radius,
                                  self.color)

        arcade.draw_circle_filled(self.position_x - 70,
                                  self.position_y - 70,
                                  self.radius,
                                  self.color)

    def update(self):
        # Move the ball
        self.position_y += self.change_y
        self.position_x += self.change_x

        if self.position_x < self.radius:
            self.position_x = self.radius

        if self.position_x > SCREEN_WIDTH - self.radius:
            self.position_x = SCREEN_WIDTH - self.radius

        if self.position_y < self.radius:
            self.position_y = self.radius

        if self.position_y > SCREEN_HEIGHT - self.radius:
            self.position_y = SCREEN_HEIGHT - self.radius
            arcade.play_sound(self.laser_sound)

class MyGame(arcade.Window):
    """ Our Custom Window Class"""

    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        """ Initializer """

        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 7")

        self.set_mouse_visible(False)

        # Create ball
        self.snowball = Snowball(150, 100, 0, 0, 50, arcade.color.WHITE)
        self.snowball_black = Snowball_black(150, 100, 0, 0, 50, arcade.color.BLACK)

        self.laser_sound = arcade.load_sound(":resources:sounds/explosion2.wav")

        arcade.set_background_color(arcade.color.SKY_BLUE)
    def on_draw(self):
        arcade.start_render()
        # Drawing house
        arcade.draw_rectangle_filled(150, 320, 200, 150, arcade.csscolor.GREY)
        arcade.draw_arc_filled(150, 390, 200, 100, arcade.csscolor.DARK_GREY, 0, 180)
        arcade.draw_rectangle_filled(150, 275, 40, 60, arcade.csscolor.BLACK)
        arcade.draw_rectangle_filled(200, 345, 30, 40, arcade.csscolor.WHITE)
        arcade.draw_rectangle_filled(200, 345, 20, 30, arcade.csscolor.BLACK)
        arcade.draw_rectangle_filled(100, 345, 30, 40, arcade.csscolor.WHITE)
        arcade.draw_rectangle_filled(100, 345, 20, 30, arcade.csscolor.BLACK)
        # Drawing grass
        arcade.draw_lrtb_rectangle_filled(0, 799, 250, 0, arcade.csscolor.GREEN)
        self.snowball.draw()
        self.snowball_black.draw()

    def update(self, delta_time):
        self.snowball.update()
        self.snowball_black.update()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.snowball.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.snowball.change_x = MOVEMENT_SPEED
        elif key == arcade.key.UP:
            self.snowball.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.snowball.change_y = -MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.snowball.change_x = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.snowball.change_y = 0

    def on_mouse_motion(self, x, y, dx, dy):
        self.snowball_black.position_x = x
        self.snowball_black.position_y = y

    def on_mouse_press(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            arcade.play_sound(self.laser_sound)
        elif button == arcade.MOUSE_BUTTON_RIGHT:
            arcade.play_sound(self.laser_sound)

def main():
    window = MyGame(800, 600)
    arcade.run()


main()