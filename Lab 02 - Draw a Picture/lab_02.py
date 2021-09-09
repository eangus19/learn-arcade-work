"""
This is lab two
"""
# import the "arcade" library
import arcade

# Open up a window
arcade.open_window(600,600, "Lab two drawing")

# Set the background color
arcade.set_background_color(arcade.csscolor.LIGHT_BLUE)

# Get ready to draw
arcade.start_render()

# Drawing grass
arcade.draw_lrtb_rectangle_filled(0, 599, 300, 0, arcade.csscolor.GREEN)

# Drawing house
arcade.draw_rectangle_filled(150, 320, 200, 150, arcade.csscolor.GREY )

arcade.draw_arc_filled(150, 390, 200, 100, arcade.csscolor.DARK_GREY, 0,180)

arcade.draw_rectangle_filled(150, 275, 40, 60, arcade.csscolor.BLACK)

arcade.draw_rectangle_filled(200, 345, 30, 40, arcade.csscolor.WHITE)

arcade.draw_rectangle_filled(200, 345, 20, 30, arcade.csscolor.BLACK)

arcade.draw_rectangle_filled(100, 345, 30, 40, arcade.csscolor.WHITE)

arcade.draw_rectangle_filled(100, 345, 20, 30, arcade.csscolor.BLACK)

# Draw Trees
arcade.draw_rectangle_filled(450, 200, 20, 60, arcade.csscolor.BROWN)

arcade.draw_circle_filled(450, 240, 30, arcade.csscolor.LIGHT_GREEN)

arcade.draw_rectangle_filled(300, 250, 20, 60, arcade.csscolor.BROWN)

arcade.draw_circle_filled(300, 290, 30, arcade.csscolor.LIGHT_GREEN)

arcade.draw_rectangle_filled(520, 250, 20, 60, arcade.csscolor.BROWN)

arcade.draw_ellipse_filled(520, 300, 60, 80, arcade.csscolor.DARK_GREEN)

arcade.draw_rectangle_filled(375, 280, 20, 60, arcade.csscolor.BROWN)

arcade.draw_arc_filled(375, 310, 60, 100, arcade.csscolor.DARK_GREEN, 0, 180)

# Draw Sun
arcade.draw_circle_filled(480, 530, 60, arcade.color.YELLOW)

arcade.draw_line(480, 530, 580, 530, arcade.csscolor.YELLOW, 4)
arcade.draw_line(480, 530, 380, 530, arcade.csscolor.YELLOW, 4)
arcade.draw_line(480, 530, 480, 430, arcade.csscolor.YELLOW, 4)
arcade.draw_line(480, 530, 480, 630, arcade.csscolor.YELLOW, 4)

arcade.draw_line(480, 530, 530, 600, arcade.color.YELLOW, 4)
arcade.draw_line(480, 530, 530, 450, arcade.color.YELLOW, 4)
arcade.draw_line(480, 530, 430, 600, arcade.color.YELLOW, 4)
arcade.draw_line(480, 530, 430, 450, arcade.color.YELLOW, 4)

# Draw Text
arcade.draw_text("Have a great day! :)",
                 50, 150,
                 arcade.color.BLACK, 24)

# Finish drawing
arcade.finish_render()

# Keep the window up until someone closes it.
arcade.run()
