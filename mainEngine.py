import mouseObjects
import environmentObjects
import graphicsEngine
import time

'''
ToDo: 
    - Make it so the mice can search for and consume water.

'''

Mimo = mouseObjects.rat("Mimo", 15, 60, 35, 100, "cautious", 0, 0, 3, 6, "M")
Edgar = mouseObjects.rat("Edgar", 20, 80, 40, 80, "calm", 0, 0, 6, 3, "E")
Davis = mouseObjects.rat("Davis", 25, 90, 45, 60, "aggressive", 0, 0, 2, 1, "D")

active_mice = [Mimo, Edgar, Davis]

seed1 = environmentObjects.food("S", "Sunflower Seed 1", "Seed", 5, 0, 10, 12, 5)
water1 = environmentObjects.food("W", "Water Hole 1", "Water", 0, 10, 100, 7, 3)

active_objects = [seed1, water1]

g_engine = graphicsEngine.g_engine()

def main():

    g_engine.g_engine_draw_objects(active_mice, active_objects)

    while True:
        for rat in active_mice:
            rat.run_behaviour(active_mice, g_engine)

        for object in active_objects:
            object.run_tick(active_objects)

        g_engine.g_engine_update(active_mice, active_objects)
        time.sleep(1)

if __name__ == "__main__":
    main()