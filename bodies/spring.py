import numpy as np
from typing import List

from bodies.body import Body, EmptyBody
from utils import normalize


class Spring(EmptyBody):
    def __init__(self, body1: Body, body2: Body, k: float, stationery_length: float):
        """
        The spring must be attached to two bodies.
        k is the rate, spring constant or force constant of the spring,
        a constant that depends on the spring's material and construction.
        stationery_length is the length at which the spring is at stationery state.
        """
        super().__init__()
        self.body1 = body1
        self.body2 = body2
        self.k = k
        self.stationery_length = stationery_length

    def update(self, timestamp):
        """
        Hooke's law states that `F = k * x`
        Than `k * x = m * a`
        So `a = k / m * x`
        Where `x` is the distance between the bodies minus the stationery length
        """
        x_magnitude = np.linalg.norm(self.body1.position - self.body2.position) - self.stationery_length
        x_vector = normalize(self.body1.position - self.body2.position) * x_magnitude
        # Check mass for infinite mass
        if self.body1.mass > 0:
            self.body1.velocity -= x_vector * self.k / self.body1.mass
        if self.body2.mass > 0:
            self.body2.velocity += x_vector * self.k / self.body2.mass
        self.body1.update(timestamp)
        self.body2.update(timestamp)

    def draw(self) -> List:
        return self.body1.draw() + self.body2.draw()