import matplotlib.pyplot as plt
import numpy as np
from typing import List, Tuple

from bodies.shapes import Shape, Circle
from utils import rotate_point, normal_vector


class ConvexPolygon(Shape):
    """
    Conventions:
    1. Vertices are ordered clockwise
    2. The normal at index i corresponds to the edge between vertex i and (i + 1) % len(vertices)
    """

    def __init__(self, vertices: List[np.array]):
        self.vertices = vertices
        self.normals = []
        self.calculate_normals()

        self.circles = [Circle(0.5) for _ in vertices]
        self.lines = None

        self.polygon_area = 0
        self.inertia_m = 0
        self.center = np.zeros(2)
        self.calculate_center()

        self.calculate_inertia_m()

    def calculate_inertia_m(self):
        inertia = 0
        for v1, v2 in zip(self.vertices, self.vertices[1:] + [self.vertices[0]]):
            relative_tri = 0.5 * abs(np.cross(v1, v2)) / self.polygon_area
            inertia_tri = relative_tri * (np.linalg.norm(v1) + np.linalg.norm(v2) + np.dot(v1, v2)) / 6
            inertia += inertia_tri
        self.inertia_m = inertia

    def calculate_normals(self):
        for v_a, v_b in zip(self.vertices, self.vertices[1:] + [self.vertices[0]]):
            self.normals.append(normal_vector(v_a - v_b))

    def calculate_center(self):
        # https://stackoverflow.com/a/19750258/7501501

        for v_a, v_b in zip(self.vertices, self.vertices[1:] + [self.vertices[0]]):
            face_area = 0.5 * abs(np.cross(v_a, v_b))
            self.polygon_area += face_area
            self.center += (v_a + v_b) * face_area
        if self.polygon_area == 0:
            raise ValueError("Invalid polygon - polygon area is 0")
        self.center = self.center / (3.0 * self.polygon_area)

    def vertices_transform_to_world(self, location: np.array, rotation: float) -> List[np.array]:
        return [rotate_point(location + self.center, location + v, rotation) for v in self.vertices]

    def draw(self, location: Tuple[float, float], rotation: float):
        vertices = self.vertices_transform_to_world(location, rotation)
        drawing = []

        if not self.lines:
            self.lines = []
            for (x1, y1), (x2, y2) in zip(vertices, vertices[1:] + [vertices[0]]):
                line, = plt.plot([x1, x2], [y1, y2])
                self.lines.append(line)
        else:
            for i, ((x1, y1), (x2, y2)) in enumerate(zip(vertices, vertices[1:] + [vertices[0]])):
                self.lines[i].set_data([x1, x2], [y1, y2])
            drawing += self.lines

        for c, loc in zip(self.circles, vertices):
            drawing += c.draw(loc, rotation)
        return drawing

    def __repr__(self):
        return "ConvexPolygon"
