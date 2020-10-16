"""
This file is based on the tutorial:
https://gamedevelopment.tutsplus.com/tutorials/how-to-create-a-custom-2d-physics-engine-the-basics-and-impulse-resolution--gamedev-6331
"""
import numpy as np

from bodies.body import Body
from bodies.convex_polygon import ConvexPolygon
from bodies.collisions.manifold import Manifold
from bodies.shapes import Circle
from utils import lies_between, point_to_vector_distance, normalize, project_vector, normal_vector


def collision_detector(a: Body, b: Body) -> Manifold:
    a_shape = a.shape
    b_shape = b.shape
    if type(a.shape) == Circle and type(b.shape) == Circle:
        r = a_shape.radius + b_shape.radius
        hit_vector_norm = np.linalg.norm(a.position - b.position)
        if hit_vector_norm == 0:
            # Circles are overlapping - IDK what to do lol, just return random but consistent value
            return Manifold(a, b, np.array([1., 0.]), a.position)
        elif r >= hit_vector_norm:
            normalized_hit_vector = (a.position - b.position) / hit_vector_norm
            hit_position = b.position + normalized_hit_vector * (b_shape.radius + (r - hit_vector_norm) / 2)
            return Manifold(a, b, normalized_hit_vector, hit_position)
    elif type(a.shape) == ConvexPolygon and type(b.shape) == ConvexPolygon:
        print("Does not support ConvexPolygon and ConvexPolygon collision yet")
        # Using advanced SAT to determain which points are inside other polygons
        if len(b.shape.vertices) < len(a.shape.vertices):
            a, b = b, a
        a_vertices = a.shape.vertices_transform_to_world(a.position, a.rotation)
        b_vertices = b.shape.vertices_transform_to_world(b.position, b.rotation)
        # TODO: Well you know - the rest
    elif type(a.shape) == ConvexPolygon or type(b.shape) == ConvexPolygon:
        if type(a.shape) == ConvexPolygon:
            polygon = a
            circle = b
        else:
            polygon = b
            circle = a
        vertices = polygon.shape.vertices_transform_to_world(polygon.position, polygon.rotation)
        number_of_v = len(vertices)
        # Check collision using Voronoi Regions
        feature_is_edge = False
        collision_index = -1
        min_distance = np.inf
        # Find the closest feature
        for index, v in enumerate(vertices):
            distance_to_v = np.linalg.norm(v - circle.position)
            if distance_to_v < min_distance:
                min_distance = distance_to_v
                feature_is_edge = False
                collision_index = index
            next_v = vertices[(index + 1) % number_of_v]
            if lies_between(circle.position, v, next_v):
                distance_to_edge = point_to_vector_distance(circle.position, v, next_v)
                if distance_to_edge < min_distance:
                    min_distance = distance_to_edge
                    feature_is_edge = True
                    collision_index = index
        # Is colliding?
        if min_distance > circle.shape.radius:
            return None
        # Find hit location and normal
        if feature_is_edge:
            next_v = vertices[(collision_index + 1) % number_of_v]
            hit_position = project_vector(next_v - vertices[collision_index],
                                          circle.position -
                                          vertices[collision_index]) + vertices[collision_index]
            return Manifold(circle, polygon,
                            normal_vector(vertices[collision_index] - next_v), hit_position)
        else:
            return Manifold(circle, polygon,
                            normalize(circle.position - vertices[collision_index]), vertices[collision_index])
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

    m.a.angular_velocity += np.cross(m.collision_point - m.a.position, impulse) / m.a.shape.inertia_m * m.a.mass_inv
    m.b.angular_velocity -= np.cross(m.collision_point - m.b.position, impulse) / m.b.shape.inertia_m * m.b.mass_inv
