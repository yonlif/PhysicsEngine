from typing import List

from bodies.body import Body
from bodies.collisions.collision_manager import collision_detector, collision_resolver
from physics_constants import g_vector


class World:
    def __init__(self, bodies: List[Body], gravity=g_vector):
        self.bodies = bodies
        self.gravity = gravity

    def update(self, timedelta):
        for body in self.bodies:
            body.update(timedelta)
            if self.gravity is not None and body.velocity is not None:
                body.acceleration += self.gravity
        for i, a in enumerate(self.bodies[:-1]):
            for j, b in enumerate(self.bodies[i + 1:]):
                manifold = collision_detector(a, b)
                if manifold:
                    collision_resolver(manifold)
