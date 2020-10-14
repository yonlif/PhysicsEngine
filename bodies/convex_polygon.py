import numpy as np
from typing import List, Tuple

from bodies.shapes import Shape, Circle


class ConvexPolygon(Shape):
    """
    Conventions:
    1. Vertices are ordered counter-clockwise
    2. The normal at index i corresponds to the edge between vertex i and (i + 1) % len(vertices)
    """

    def __init__(self, vertices: List[np.array]):
        self.vertices = vertices
        self.normals = []
        self.circles = [Circle(0.5) for _ in vertices]

    def draw(self, location: Tuple[float, float]):
        return sum([c.draw(location + loc) for c, loc in zip(self.circles, self.vertices)], [])
