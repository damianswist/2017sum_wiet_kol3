#dawidPyth

import unittest

from Plane import Plane

class SimulationTest(unittest.TestCase):
    def test_whether_turbulations_were_added_successfully(self):
        plane = Plane()
        start_orientation = plane.current_orientation
        plane.add_turbulations(10)
        self.assertEqual(plane.current_orientation, start_orientation + 10)

    def test_wheter_correction_works(self):
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