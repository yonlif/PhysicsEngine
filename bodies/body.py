import numpy as np
from typing import List

from bodies.shapes import Shape


class Body:
    def __init__(self,
                 position: np.array,
                 velocity: np.array,
                 mass: float,
                 restitution_coeff: float,
                 friction_coeff: float,
                 shape: Shape,
                 rotation: float=0,
                 angular_velocity: float=0):
        self.position = position
        self.rotation = rotation

        self.velocity = velocity
        self.angular_velocity = angular_velocity

        self.mass = mass
        self.mass_inv = 1.0 / mass

        self.acceleration = np.zeros(2)
        self.torque = 0

        self.shape = shape
        self.restitution_coeff = restitution_coeff
        self.friction_coeff = friction_coeff

    def update(self, timedelta=1):
        self.velocity += self.acceleration * timedelta
        self.position = self.position + self.velocity * timedelta

        self.angular_velocity += self.torque / 1 * timedelta  # TODO: Add inertia
        self.rotation = self.rotation + self.angular_velocity * timedelta

        self.acceleration = np.zeros(self.position.shape)
        self.torque = 0

    def draw(self) -> List:
        x, y = self.position[0], self.position[1]
        return self.shape.draw((x, y), self.rotation)

    def __repr__(self):
        return f"<{self.shape} at {self.position}>"


class InfMassBody(Body):
    def __init__(self, position: np.array, restitution_coeff, shape, friction_coeff):
        super().__init__(position=position,
                         rotation=0,
                         velocity=np.zeros(shape=position.shape),
                         angular_velocity=0,
                         mass=1,
                         restitution_coeff=restitution_coeff,
                         friction_coeff=friction_coeff,
                         shape=shape)
        self.mass = 0
        self.mass_inv = 0

    def update(self, timedelta=1):
        pass


class EmptyBody(Body):
    def __init__(self):
        super().__init__(position=None,
                         rotation=0,
                         velocity=None,
                         angular_velocity=0,
                         mass=1,
                         restitution_coeff=0,
                         friction_coeff=0,
                         shape=Shape())
        self.mass = 0
        self.mass_inv = 0

    def update(self, timedelta=1):
        pass

    def draw(self) -> List:
        return []
