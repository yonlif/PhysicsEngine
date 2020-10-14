from typing import List

from bodies.body import Body
from bodies.collision_manager import collision_detector, collision_resolver
from physics_constants import g_vector


class World:
    def __init__(self, bodies: List[Body], gravity=g_vector):
        self.bodies = bodies
        self.gravity = gravity

    def update(self):
        for body in self.bodies:
            body.update()
            if self.gravity is not None and body.velocity is not None:
                body.velocity += self.gravity
        for i, a in enumerate(self.bodies[:-1]):
            for j, b in enumerate(self.bodies[i + 1:]):
                if collision_detector(a, b):
                    collision_resolver(a, b)
