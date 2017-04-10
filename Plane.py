class Plane:
    def __init__(self, current_orientation=0):
        self.current_orientation = current_orientation

    def add_turbulations(self, turbulations):
        self.current_orientation += turbulations

    def correct_tilt(self):
        tilt_to_correct = self.current_orientation
        self.current_orientation = 0

        if tilt_to_correct < 0:
            return -tilt_to_correct
        if tilt_to_correct > 0:
            return -tilt_to_correct

        return tilt_to_correct

