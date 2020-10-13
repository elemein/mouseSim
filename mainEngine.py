import mouseObjects
import environmentObjects
import graphicsEngine
import time

sunflower_seed = environmentObjects.food("Sunflower Seed","Seed",5, 100)

Mimo = mouseObjects.rat("Mimo", 15, 60, 35, 35, 100, "cautious", 0, 0, 3, 6, "M")
Edgar = mouseObjects.rat("Edgar", 20, 80, 40, 40, 80, "calm", 0, 0, 6, 3, "E")
Davis = mouseObjects.rat("Davis", 25, 90, 45, 45, 60, "aggressive", 0, 0, 2, 1, "D")

active_rats = [Mimo, Edgar, Davis]

g_engine = graphicsEngine.g_engine()

def main():

    while True:
        for rat in active_rats:
            rat.run_behaviour(active_r)

        g_engine.g_engine_update(active_rats)
        ats
        time.sleep(1)

if __name__ == "__main__":
    main()