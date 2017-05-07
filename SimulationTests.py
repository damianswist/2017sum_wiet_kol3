#dawidPyth

import unittest

from Plane import Plane
from Simulation import Simulation


class SimulationTest(unittest.TestCase):
    def test_whether_default_deviation_is_set_properly(self):
        simulation = Simulation()
        default_deviation = 10
        self.assertEqual(simulation.deviation, default_deviation)

    def test_whether_default_mean_orientation_is_set_properly(self):
        simulation = Simulation()
        default_mean_orientation = 0
        self.assertEqual(simulation.mean_orientation, default_mean_orientation)

    def test_whether_default_max_level_deviation_is_set_properly(self):
        simulation = Simulation()
        default_max_level_deviation = 10
        self.assertEqual(simulation.max_level_deviation, default_max_level_deviation)

    def test_whether_setting_deviation_works(self):
        simulation = Simulation(deviation=50)
        self.assertEqual(simulation.deviation, 50)

    def test_whether_setting_mean_orientation_works(self):
        simulation = Simulation(mean_orientation=50)
        self.assertEqual(simulation.mean_orientation, 50)

    def test_whether_setting_max_level_deviation_works(self):
        simulation = Simulation(max_level_deviation=50)
        self.assertEqual(simulation.max_level_deviation, 50)

    def test_whether_turbulations_are_generated(self):
        simulation = Simulation()
        number = simulation.generate_turbulations()
        self.assertIsNotNone(number)

    def test_whether_deviation_is_always_lower_than_max_deviation_level(self):
        simulation = Simulation(deviation=100, max_level_deviation=50)
        self.assertGreater(simulation.max_level_deviation, simulation.deviation)

    def test_whether_turbulations_were_added_successfully(self):
        plane = Plane()
        start_orientation = plane.current_orientation
        plane.add_turbulations(10)
        self.assertEqual(plane.current_orientation, start_orientation + 10)

    def test_whether_correction_works(self):
        plane = Plane()
        start_orientation = plane.current_orientation
        plane.add_turbulations(10)
        plane.correct_tilt()
        self.assertEqual(plane.current_orientation, start_orientation)

    def test_whether_orientation_can_be_higher_then_360(self):
        plane = Plane()
        plane.add_turbulations(100000)
        orientation = plane.current_orientation
        self.assertLess(orientation, 360)



if __name__ == '__main__':
    unittest.main()