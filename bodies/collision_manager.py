"""
This file is based on the tutorial:
https://gamedevelopment.tutsplus.com/tutorials/how-to-create-a-custom-2d-physics-engine-the-basics-and-impulse-resolution--gamedev-6331
"""
import numpy as np
import logging

from bodies.body import Body
from bodies.shapes import Circle, ConvexPolygon
from utils import normalize


def collision_detector(a: Body, b: Body) -> bool:
    a_shape = a.shape
    b_shape = b.shape
    if type(a.shape) == Circle and type(b.shape) == Circle:
        r = a_shape.radius + b_shape.radius
        return r >= np.linalg.norm(a.position - b.position)
    elif type(a.shape) == ConvexPolygon or type(b.shape) == ConvexPolygon:
        raise NotImplementedError("Does not support ConvexPolygon collision yet")


def collision_resolver(a: Body, b: Body):
    """
    Resolving the collision between two bodies by changing their velocity.
    Note - This is actually working well with the fact that infinite mass is represented as 0 mass
    TODO (Yonatan): Make it work for ConvexPolygons
    """
    logging.info(f"Resolving collision between {b} and {b}")
    relative_velocity = a.velocity - b.velocity
    # The normal of the collision between two circles is always the vector between their centers
    normal_vector = normalize(a.position - b.position)
    # Calculating the velocity that needs to affect the ball
    vel_along_normal = np.dot(relative_velocity, normal_vector)

    # If in the next frame they are already separating - do not act
    if vel_along_normal >= 0:
        logging.info(f"Collision between {b} and {b} did not need to be resolved")
        return None

    # The restitution coefficient is always the min
    e = min(a.restitution_coeff, b.restitution_coeff)

    # Idk some physics or something
    j = -(1 + e) * vel_along_normal
    j /= a.mass_inv + b.mass_inv

    impulse = j * normal_vector
    mass_sum = a.mass + b.mass
    ratio = a.mass / mass_sum
    a.velocity += ratio * impulse
    ratio = b.mass / mass_sum
    b.velocity -= ratio * impulse
