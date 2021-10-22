import arcade

arcade.open_window(600, 600, "Sound Demo")
laser_sound = arcade.load_sound()
arcade.play_sound(laser_sound)
arcade.run()