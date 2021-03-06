class food:
    def __init__(self, tile_value, food_name, food_type, fullness_value, hydration_value, freshness, x_pos, y_pos):
        self.tile_value = tile_value
        self.food_name = food_name
        self.food_type = food_type
        self.fullness_value = fullness_value
        self.hydration_value = hydration_value
        self.freshness = freshness
        self.cannot_rot = ['Water']

        self.position = {"X" : x_pos, "Y" : y_pos}

    def run_tick(self, active_objects):

        if self.food_name not in self.cannot_rot:
            self.rot(active_objects)

    def rot(self, active_objects):
        self.freshness -= 1

        if self.freshness <= 0:
            active_objects.remove(self)