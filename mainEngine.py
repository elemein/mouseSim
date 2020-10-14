import mouseObjects
import environmentObjects
import graphicsEngine
import time

'''
ToDo:

    - Figure out how to make the mouse vision work. 

'''


seed1 = environmentObjects.food("S","Sunflower Seed 1","Seed",5, 10, 12, 5)

Mimo = mouseObjects.rat("Mimo", 15, 60, 35, 100, "cautious", 0, 0, 3, 6, "M")
Edgar = mouseObjects.rat("Edgar", 20, 80, 40, 80, "calm", 0, 0, 6, 3, "E")
Davis = mouseObjects.rat("Davis", 25, 90, 45, 60, "aggressive", 0, 0, 2, 1, "D")

active_mice = [Mimo, Edgar, Davis]
active_objects = [seed1]

g_engine = graphicsEngine.g_engine()

def main():

    while True:
        for rat in active_mice:
            rat.run_behaviour(active_mice, g_engine)

        for object in active_objects:
            object.run_tick(active_objects)

        g_engine.g_engine_update(active_mice, active_objects)
        time.sleep(1)

if __name__ == "__main__":
    main()