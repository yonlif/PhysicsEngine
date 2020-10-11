from typing import List

from bodies.body import Body
from bodies.collision_manager import collision_detector, collision_resolver


class World:
    def __init__(self, bodies: List[Body]):
        self.bodies = bodies

    def update(self, timestamp=0.1):
        for body in self.bodies:
            body.update(timestamp)
        for i, a in enumerate(self.bodies[:-1]):
            for j, b in enumerate(self.bodies[i + 1:]):
                if collision_detector(a, b):
                    collision_resolver(a, b)
