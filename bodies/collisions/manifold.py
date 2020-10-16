import numpy as np

from bodies.body import Body


class Manifold:
    def __init__(self, a: Body, b: Body, normal_vector: np.array, collision_point: np.array):
        self.a = a
        self.b = b
        self.normal_vector = normal_vector
        self.collision_point = collision_point

    def __repr__(self):
        return f"<Manifold: Collision between {self.a} and {self.b} at position {self.collision_point}>"
