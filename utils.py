import numpy as np


def normalize(v: np.array) -> np.array:
    norm = np.linalg.norm(v)
    if norm == 0:
        return v
    return v / norm


def xy_to_text(xy) -> str:
    return f"({xy[0]:.2f}, {xy[1]:.2f})"
