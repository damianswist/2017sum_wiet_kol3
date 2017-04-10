from Plane import Plane
import random
from time import sleep
from select import select
import sys


class Simulation:

    def __init__(self, mean_orientation = 0, deviation = 10, max_level_deviation = 10):
        self.mean_orientation = mean_orientation
        self.deviation = deviation
        self.max_level_deviation = max_level_deviation

    def generate_turbulations(self):
        return random.gauss(self.mean_orientation, self.deviation)

    def run(self):
        init_orientation = random.uniform(-self.max_level_deviation, self.max_level_deviation)
        plane = Plane(init_orientation)
        while True:
            print "Current orientation: {:01.4f}".format(plane.current_orientation)
            plane.add_turbulations(self.generate_turbulations())
            print "Current orientation after turbulations: {:01.4f}".format(plane.current_orientation)
            correction_tilt = plane.correct_tilt()
            print "Correction: {:01.4f}".format(correction_tilt)
            print "Current orientation after correction: {:01.4f}\n".format(plane.current_orientation)
            print "\nPress ENTER to stop simulation\n"

            # while True:
            #     sleep(0.5)
            #     if sys.stdin in select([sys.stdin, ], [], [], 0)[0]:
            #         raise StopIteration()
            #     else:
            #         break

if __name__ == "__main__":

    if len(sys.argv) == 3:
        simulation = Simulation(int(float(sys.argv[1])), int(float(sys.argv[2])), int(float(sys.argv[3])))
    else:
        simulation = Simulation()

    simulation.run()
