import random
import graphicsEngine

class rat:
    def __init__(self, name, weight, body_length, body_diameter, tail_length, temperament, thirst, hunger,
                 x_pos, y_pos, tile_value):
        self.tile_value = tile_value
        self.name = name
        self.physical_traits = {"Weight" : weight, "Body Length" : body_length,
                                "Body Diameter" : body_diameter, "Tail Length" : tail_length}
        # weight, grams, average is ~20g
        # length, mm, average is 65-95mm
        # diameter mm, average is 30-50mm
        # tail mm, average is 60-105mm
        self.temperament = temperament # cautious, calm, aggressive
        self.thirst = thirst # scale of 0-100, 100 being very thirsty
        self.hunger = hunger # scale of 0-100, 100 being very hungry
        self.position = {"X" : x_pos, "Y" : y_pos}
        self.goal = {"Current Goal" : ""}
        self.view_range = 2
        self.in_sight = []

    def run_behaviour(self, active_rats, g_engine):

        self.thirst += 1
        self.hunger += 1

        self.determine_needs(active_rats, g_engine)

        rand_move = random.randint(0, 100)

        self.move(-1,0,active_rats,g_engine)

        '''
        if rand_move < 25:
            self.move(0,1, active_rats, g_engine)
        elif rand_move > 25 and rand_move < 50:
            self.move(1,0, active_rats, g_engine)
        elif rand_move > 50 and rand_move < 75:
            self.move(0,-1, active_rats, g_engine)
        else:
            self.move(-1,0, active_rats, g_engine)
        '''

    def determine_needs(self, active_rats, g_engine):
        # Get whats in vision.

        del self.in_sight[:]

        for idx in range((0-self.view_range),(self.view_range+1)):
            try:

                temp1 = (idx + self.position["Y"])
                temp2 = (self.position["X"] - self.view_range)
                temp3 = (self.position["X"] + self.view_range + 1)

                if (temp1 < 0) or (temp2 < 0) or (temp3 < 0):
                    raise IndexError
                else:
                    self.in_sight.append(g_engine.map[idx + self.position["Y"]][(self.position["X"] - self.view_range):(self.position["X"] + self.view_range + 1)])
            except IndexError:
                self.in_sight.append("X")

        self.in_sight = list(reversed(self.in_sight))

    def eat(self, food):
        self.hunger = self.hunger - food.hunger_value

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
            if (self.position["Y"] == rat.position["Y"]) and (self.position["X"] == rat.position["X"]) and (self.name != rat.name):
                self.position["Y"] = previous_position[0]
                self.position["X"] = previous_position[1]