"""
This file is based on the tutorial:
https://gamedevelopment.tutsplus.com/tutorials/how-to-create-a-custom-2d-physics-engine-the-basics-and-impulse-resolution--gamedev-6331
"""
import numpy as np

from bodies.body import Body
from bodies.convex_polygon import ConvexPolygon
from bodies.collisions.manifold import Manifold
from bodies.shapes import Circle
from utils import normalize


def collision_detector(a: Body, b: Body) -> Manifold:
    a_shape = a.shape
    b_shape = b.shape
    if type(a.shape) == Circle and type(b.shape) == Circle:
        r = a_shape.radius + b_shape.radius
        if r >= np.linalg.norm(a.position - b.position):
            return Manifold(a, b, normalize(a.position - b.position))
    elif type(a.shape) == ConvexPolygon or type(b.shape) == ConvexPolygon:
        print("Does not support ConvexPolygon collision yet")
    return None


def collision_resolver(m: Manifold):
    """
    Resolving the collision between two bodies by changing their velocity.
    Note - This is actually working well with the fact that infinite mass is represented as 0 mass
    """
    print(f"Resolving collision between {m.a} and {m.b}")
    relative_velocity = m.a.velocity - m.b.velocity
    # The normal of the collision between two circles is always the vector between their centers
    # Calculating the velocity that needs to affect the ball
    vel_along_normal = np.dot(relative_velocity, m.normal_vector)

    # If in the next frame they are already separating - do not act
    if vel_along_normal >= 0:
        print(f"Collision between {m.a} and {m.b} did not need to be resolved")
        return None

    # The restitution coefficient is always the min
    e = min(m.a.restitution_coeff, m.b.restitution_coeff)

    # Idk some physics or something
    j = -(1 + e) * vel_along_normal
    j /= m.a.mass_inv + m.b.mass_inv

    impulse = j * m.normal_vector
    m.a.velocity += m.a.mass_inv * impulse
    m.b.velocity -= m.b.mass_inv * impulse
