import time


class TrafficLight:
    def __init__(self, first_light, second_light, third_light):
        self._first_light = first_light
        self._second_light = second_light
        self._third_light = third_light

    def light(self):
        print({self._first_light})
        time.sleep(7.0)
        print({self._second_light})
        time.sleep(2.0)
        print({self._third_light})
        time.sleep(5.0)


light = TrafficLight('Red', 'Yellow', 'Green')
light.light()


