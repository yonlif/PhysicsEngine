import numpy as np
from typing import List

from bodies.shapes import Shape


class Body:
    def __init__(self,
                 position: np.array,
                 velocity: np.array,
                 mass: float,
                 shape: Shape,
                 restitution_coeff: float,
                 friction_coeff: float):
        self.position = position
        self.velocity = velocity
        self.mass = mass
        self.mass_inv = 1.0 / mass
        self.shape = shape
        self.restitution_coeff = restitution_coeff
        self.friction_coeff = friction_coeff

    def update(self, timestamp: float):
        self.position = self.position + self.velocity * timestamp

    def draw(self) -> List:
        x, y = self.position[0], self.position[1]
        return self.shape.draw((x, y))


class InfMassBody(Body):
    def __init__(self, position: np.array, restitution_coeff, shape, friction_coeff):
        super().__init__(position,
                         np.zeros(shape=position.shape),
                         mass=1,
                         shape=shape,
                         restitution_coeff=restitution_coeff,
                         friction_coeff=friction_coeff)
        self.mass = 0
        self.mass_inv = 0

    def update(self, timestamp):
        pass


class EmptyBody(Body):
    def __init__(self):
        super().__init__(None,
                         None,
                         mass=1,
                         shape=Shape(),
                         restitution_coeff=0,
                         friction_coeff=0)
        self.mass = 0
        self.mass_inv = 0

    def update(self, timestamp):
        pass

    def draw(self) -> List:
        return []
