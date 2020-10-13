import random
import graphicsEngine

class rat:
    def __init__(self, name, weight, body_length, body_width, body_height, tail_length, temperament, thirst, hunger,
                 x_pos, y_pos, tile_value):
        self.tile_value = tile_value
        self.name = name
        self.weight = weight # grams, average is ~20g
        self.body_length = body_length # mm, average is 65-95mm
        self.body_width = body_width # mm, average is 30-50mm
        self.body_height = body_height # mm, average is 30-50mm
        self.tail_length = tail_length # mm, average is 60-105mm
        self.temperament = temperament # cautious, calm, aggressive
        self.thirst = thirst # scale of 0-100, 100 being very thirsty
        self.hunger = hunger # scale of 0-100, 100 being very hungry
        self.x_pos = x_pos
        self.y_pos = y_pos

    def run_behaviour(self, active_rats):

        rand_move = random.randint(0, 100)

        if rand_move < 25:
            self.move(0,1, active_rats)
        elif rand_move > 25 and rand_move < 50:
            self.move(1,0, active_rats)
        elif rand_move > 50 and rand_move < 75:
            self.move(0,-1, active_rats)
        else:
            self.move(-1,0, active_rats)

    def eat(self, food):
        self.hunger = self.hunger - food.hunger_value

    def move(self, x_move, y_move, active_rats):

        previous_position = [self.y_pos, self.x_pos]

        # Try to update the x position so long as its in the map.
        try:
            if (self.x_pos + x_move) >= 0:
                self.x_pos += x_move
        except IndexError:
            pass

        # Try to update the y position so long as its in the map.
        try:
            if (self.y_pos + y_move) >= 0:
                self.y_pos += y_move
        except IndexError:
            pass

        # Check for collisions. If true, revert to old position. This in a way enforces a turn order.
        for rat in active_rats:
            if (self.y_pos == rat.y_pos) and (self.x_pos == rat.x_pos) and (self.name != rat.name):
                self.y_pos = previous_position[0]
                self.x_pos = previous_position[1]