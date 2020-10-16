import random
import graphicsEngine

# Behaviours:
# Every tick, the rat will have to check its state and change its behaviour based on that.
# It will check the following:
# DONT IMPLEMENT YET - If it is in danger, if so, incur fight or flight.
# If it is thirsty, if so, find water. Water>Food (have a stat that determines when a mouse will look for it)
# If it is hungry, if so, find food.
# DONT IMPLEMENT YET - If bored, try to find a playmate to play around with. (set stat to determine how long will search for).
# DONT IMPLEMENT YET - If it is bored, play by moving around.
# DONT IMPLEMENT YET - Mate?

# In order to find, it will have to have a "set search path" function. (should have a stat that determines how long it stays on a path)
# Essentially it'll choose a direction to go, and go it until it decides on a new direction OR sees a barrier.
# If at any point it sees its goal, it should go for it.
# Once adjacent to the goal, it should consume/use it.

class rat:
    def __init__(self, name, weight, body_length, body_diameter, tail_length, temperament, hydration, hunger,
                 x_pos, y_pos, tile_value):
        self.tile_value = tile_value
        self.name = name
        self.physical_traits = {"Weight": weight, "Body Length": body_length,
                                "Body Diameter": body_diameter, "Tail Length": tail_length}
        # weight, grams, average is ~20g
        # length, mm, average is 65-95mm
        # diameter mm, average is 30-50mm
        # tail mm, average is 60-105mm
        self.temperament = temperament  # cautious, calm, aggressive
        self.hydration = hydration
        self.fullness = hunger
        self.position = {"X": x_pos, "Y": y_pos}
        self.goal = {"Goal" : ""}
        self.view_range = 2
        self.in_sight = []

        self.goal_to_plan = {"Find" : self.search, "Consume": self.consume}

    def run_behaviour(self, active_rats, g_engine):
        self.hydration -= 1
        self.fullness -= 1

        # What do I need?
        self.determine_needs(active_rats, g_engine)

        # Get whats in vision. What can I do about my needs w/ whats near?
        self.examine_surroundings(active_rats, g_engine)

        #i last was here

        self.goal_to_plan[self.goal["Goal"]["Actions"][0]](self.goal["Goal"]["Subject"][0])

        rand_move = random.randint(0, 100)

        #       Up = y(1),  |Left = x(-1)
        #       Down = y(-1)|Right = x(1)
        self.move(y_move=-1, x_move=1, active_rats=active_rats, g_engine=g_engine)

    def determine_needs(self, active_rats, g_engine):

        # Run through priority tree.
        if self.hydration < 50:
            self.goal["Goal"] = {"Actions" : ["Find","Consume"], "Subject" : ["Drink"]}
        elif self.fullness < 50:
            self.goal["Goal"] = {"Actions" : ["Find","Consume"], "Subject" : ["Food"]}

    def examine_surroundings(self, active_rats, g_engine):

        # Find how wide and tall the view range must be.
        view_range_perimeter = (self.view_range * 2) + 1
        # Find out the middle, to easily pinpoint where you'd be, as you'd be at the intersection of your view range when top-down.
        view_range_middle = self.view_range + 1

        # Create a 2d array by filling in 0's for as many elements wide and tall as the view range perimeter.
        in_sight_local = [[0 for y in range(0, view_range_perimeter)] for x in range(0, view_range_perimeter)]

        for idx_y, line in enumerate(in_sight_local):  # Per line in_sight
            for idx_x, tile in enumerate(line): # Per tile per line
                try: # As this tests individual tiles, we want any Index Errors to indicate out of bounds, hence "X"
                    adjusted_y_position = self.position["Y"]+(2 - idx_y) # We want to start 2 up
                    adjusted_x_position = self.position["X"]+(idx_x - 2) # We want to start 2 left

                    # If its going to try to access an index via a negative entry, we list it as out of bounds.
                    if adjusted_x_position < 0 or adjusted_y_position < 0:
                        raise IndexError

                    # Update the map tile to the mouse's vision.
                    in_sight_local[idx_y][idx_x] = g_engine.map[adjusted_y_position][adjusted_x_position]
                except IndexError:
                    in_sight_local[idx_y][idx_x] = "X"

    def search(self,search_for):
        print(f'Searching for {search_for}')
        pass

    def consume(self, object):
        self.fullness = self.fullness - object.hunger_value

    def move(self, x_move, y_move, active_rats, g_engine):

        previous_position = [self.position["Y"], self.position["X"]]

        # Try to update the x position so long as its in the map.
        try:
            if (self.position["X"] + x_move) >= 0 and (self.position["X"] + x_move) < (len(g_engine.map[0])):
                self.position["X"] += x_move
        except IndexError:
            pass

        # Try to update the y position so long as its in the map.
        try:
            if (self.position["Y"] + y_move) >= 0 and (self.position["Y"] + y_move) < (len(g_engine.map)):
                self.position["Y"] += y_move
        except IndexError:
            pass

        # Check for collisions. If true, revert to old position. This in a way enforces a turn order.
        for rat in active_rats:
            if (self.position["Y"] == rat.position["Y"]) and (self.position["X"] == rat.position["X"]) and (
                    self.name != rat.name):
                self.position["Y"] = previous_position[0]
                self.position["X"] = previous_position[1]
