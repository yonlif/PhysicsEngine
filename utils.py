from typing import List

import numpy as np


def normalize(v: np.array) -> np.array:
    norm = np.linalg.norm(v)
    if norm == 0:
        return v
    return v / norm


def xy_to_text(xy) -> str:
    return f"({xy[0]:.2f}, {xy[1]:.2f})"


def rotate_point(base_point: np.array, point_to_rotate: np.array, rotation: float) -> np.array:
    """
    2D rotation clockwise
    :param base_point: The point over we will rotate
    :param point_to_rotate: The point to rotate
    :param rotation: Angle in radians
    :return: The new point after rotation
    """
    c, s = np.cos(rotation), np.sin(rotation)
    r_matrix = np.array(((c, -s), (s, c)))
    return np.dot(r_matrix, (point_to_rotate - base_point)) + base_point


def project_vector(base_vector: np.array, vector_to_project: np.array) -> np.array:
    return normalize(base_vector) * np.dot(base_vector, vector_to_project) / np.linalg.norm(base_vector)


def project_multiple_vectors(base_vector: np.array, vectors_to_project: List[np.array]) -> List[np.array]:
    projection_vector = normalize(base_vector)
    projection_matrix = projection_vector.reshape(-1, 1)
    res = np.dot(np.array(vectors_to_project), projection_matrix)
    return [vec * projection_vector for vec in res]


def normal_vector(vector: np.array, left_hand=True) -> np.array:
    """
    Creating the normal vector for 2D vectors - the vector perpendicular to the given one.
    DO NOT CONFUSE WITH NORMALIZE!
    :param vector: Given 2D vector for which we will find the normal
    :param left_hand: If True the function will return the left hand normal - if False - the right hand
    """
    tmp = -1 if left_hand else 1
    return normalize(np.array([-tmp * vector[1], tmp * vector[0]]))


def lies_between(point_to_check: np.array, v_1: np.array, v_2: np.array) -> bool:
    """
    https://stackoverflow.com/questions/33155240/how-to-check-if-a-point-is-between-two-other-points-but-not-limited-to-be-align?rq=1
    TODO: This can obviously be optimized
    """
    a = np.linalg.norm(v_1 - v_2)
    b = np.linalg.norm(v_2 - point_to_check)
    c = np.linalg.norm(point_to_check - v_1)
    return a**2 + b**2 >= c**2 and a**2 + c**2 >= b**2


def point_to_vector_distance(point, v_1, v_2):
    return np.abs(np.cross(v_2 - v_1, v_1 - point)) / np.linalg.norm(v_2 - v_1)