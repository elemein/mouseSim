class food:
    def __init__(self, food_name, food_type, hunger_value, freshness):
        self.food_name = food_name
        self.food_type = food_type
        self.hunger_value = hunger_value
        self.freshness = freshness

    def rot(self):
        self.freshness -= 1