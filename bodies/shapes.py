from typing import List, Tuple
import numpy as np
import matplotlib.pyplot as plt

from utils import xy_to_text


class Shape:
    def draw(self, location: Tuple[float, float]) -> List:
        raise NotImplementedError(f"The object {type(self)} did not implement the draw function")


class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius
        self.circle = None
        self.text = None

    def draw(self, location: Tuple[float, float]) -> List:
        if not self.circle:
            self.text = plt.text(*location, xy_to_text(location))
            self.circle = plt.Circle(location, self.radius)
            return [self.circle]
        self.circle.center = location
        self.text.set_position(location)
        self.text.set_text(xy_to_text(location))
        return [self.circle, self.text]

    def __repr__(self):
        return "Circle"


class Line(Shape):
    def __init__(self, body1, body2):
        self.body1 = body1
        self.body2 = body2
        self.line = None
        self.text = None

    def draw(self, location: Tuple[float, float]) -> List:
        if not self.line:
            self.line, = plt.plot([self.body1.position[0], self.body2.position[0]],
                                   [self.body1.position[1], self.body2.position[1]])
            return []
        self.line.set_data([self.body1.position[0], self.body2.position[0]],
                           [self.body1.position[1], self.body2.position[1]])
        return [self.line]

    def __repr__(self):
        return "Line"
