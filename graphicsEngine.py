import os

class g_engine:

    def __init__(self):
        self.map = []

        self.setup_map()

    def setup_map(self):
        map_reader = open("map.txt","r")

        for line in map_reader.readlines():
            self.map.append(line.strip()) # .strip() is a function of strings to remove carriage-returns, e.g. "\n"

        for idx, line in enumerate(self.map):
            self.map[idx] = list(line) # Take the list of tile values and turn self.map into a 2d-array.

    def g_engine_draw_objects(self, active_rats, active_objects):

        for rat in active_rats:
            self.map[rat.position["Y"]][rat.position["X"]] = rat.tile_value

        for object in active_objects:
            self.map[object.position["Y"]][object.position["X"]] = object.tile_value

    def g_engine_update(self, active_rats, active_objects):

        self.reset_map()

        # check for animal movements
        self.g_engine_draw_objects(active_rats,active_objects)

        self.print_map()

    def reset_map(self):
        for y_pos_idx, line in enumerate(self.map):
            for x_pos_idx, tile in enumerate(line):
                self.map[y_pos_idx][x_pos_idx] = '.'

    def print_map(self):

        print('\n'*50)

        for line in reversed(self.map):
            g_tile = ""
            for tile in line:
                g_tile += tile

            print(g_tile)