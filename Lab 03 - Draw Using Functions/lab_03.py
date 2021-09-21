"""
This is lab three
"""
# import the "arcade" library
import arcade

def draw_grass():
    """ Draw the grass """
    arcade.draw_lrtb_rectangle_filled(0, 599, 300, 0, arcade.csscolor.GREEN)

def draw_house(x, y):
    """ Draw a house """
    arcade.draw_rectangle_filled(x + 15, y + 3, 190, 137, arcade.csscolor.GREY)
    arcade.draw_arc_filled(x + 15, y + 65, 200, 170, arcade.csscolor.DARK_GREY, 0, 180)
    arcade.draw_rectangle_filled(x + 15, y - 35, 40, 60, arcade.csscolor.BLACK)
    arcade.draw_rectangle_filled(x + 70, y + 28, 30, 40, arcade.csscolor.WHITE)
    arcade.draw_rectangle_filled(x + 70, y + 28, 20, 30, arcade.csscolor.BLACK)
    arcade.draw_rectangle_filled(x - 40, y + 28, 30, 40, arcade.csscolor.WHITE)
    arcade.draw_rectangle_filled(x - 40, y + 28, 20, 30, arcade.csscolor.BLACK)

def draw_sun(x, y):
    """ Draw a sun """

    # Draw sun
    arcade.draw_circle_filled(x, 30 + y, 60, arcade.color.YELLOW)

    # Draw lines for sun
    arcade.draw_line(480, 530, 580, 530, arcade.csscolor.YELLOW, 4)
    arcade.draw_line(480, 530, 380, 530, arcade.csscolor.YELLOW, 4)
    arcade.draw_line(480, 530, 480, 430, arcade.csscolor.YELLOW, 4)
    arcade.draw_line(480, 530, 480, 630, arcade.csscolor.YELLOW, 4)
    arcade.draw_line(480, 530, 530, 600, arcade.color.YELLOW, 4)
    arcade.draw_line(480, 530, 530, 450, arcade.color.YELLOW, 4)
    arcade.draw_line(480, 530, 430, 600, arcade.color.YELLOW, 4)
    arcade.draw_line(480, 530, 430, 450, arcade.color.YELLOW, 4)

def draw_trees(x, y):
    """ Draw trees """
    arcade.draw_rectangle_filled(x + 2, y + 10, 30, 60, arcade.csscolor.BROWN)
    arcade.draw_circle_filled(430, 255, 35, arcade.csscolor.DARK_SEA_GREEN)
    arcade.draw_rectangle_filled(300, 250, 20, 60, arcade.csscolor.BROWN)
    arcade.draw_circle_filled(300, 290, 30, arcade.csscolor.LIGHT_GREEN)
    arcade.draw_rectangle_filled(520, 250, 20, 60, arcade.csscolor.BROWN)
    arcade.draw_ellipse_filled(520, 300, 60, 80, arcade.csscolor.DARK_GREEN)
    arcade.draw_rectangle_filled(375, 280, 20, 60, arcade.csscolor.BROWN)
    arcade.draw_arc_filled(375, 310, 60, 100, arcade.csscolor.DARK_GREEN, 0, 180)

def on_draw(delta_time):
    """ Draw everything """
    arcade.start_render()

    draw_grass()
    draw_house(150, 320)
    draw_sun(480, 500)
    draw_sun(95, 505)
    draw_trees(430, 200)

def main():
    arcade.open_window(600, 600, "Lab three drawing")
    arcade.set_background_color(arcade.csscolor.LIGHT_BLUE)
    arcade.start_render()

    # Call on_draw every 60th of a second.
    arcade.schedule(on_draw, 1/60)
    arcade.run()

# Call the main function to get the program started.
main()