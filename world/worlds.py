import numpy as np

from bodies.body import Body, InfMassBody
from bodies.convex_polygon import ConvexPolygon
from bodies.shapes import Circle
from world.world import World
from bodies.spring import Spring


def single_mass_test():
    return World(bodies=[Body(position=np.array([30., 10.]),
                              velocity=np.array([-0.1, 0.]),
                              mass=1,
                              friction_coeff=1,
                              restitution_coeff=0.9,
                              shape=Circle(1)),
                         ], gravity=None)


def inf_mass_test():
    return World(bodies=[Body(position=np.array([30., 10.]),
                              velocity=np.array([-0.1, 0.]),
                              mass=1,
                              friction_coeff=1,
                              restitution_coeff=0.9,
                              shape=Circle(1)),
                         InfMassBody(position=np.array([20., 10.]),
                                     friction_coeff=1,
                                     restitution_coeff=0.9,
                                     shape=Circle(1))
                         ], gravity=None)


def simple_two_mass_test():
    return World(bodies=[Body(position=np.array([30., 10.]),
                              velocity=np.array([-0.1, 0.]),
                              mass=1,
                              friction_coeff=1,
                              restitution_coeff=0.9,
                              shape=Circle(1)),
                         Body(position=np.array([0., 10.]),
                              velocity=np.array([0.1, 0.]),
                              mass=2,
                              friction_coeff=1,
                              restitution_coeff=0.9,
                              shape=Circle(1)),
                         ], gravity=None)


def two_mass_test():
    return World(bodies=[Body(position=np.array([30., 10.]),
                              velocity=np.array([-0.1, 0.]),
                              mass=1,
                              friction_coeff=1,
                              restitution_coeff=0.9,
                              shape=Circle(1)),
                         Body(position=np.array([0., 10.5]),
                              velocity=np.array([0.2, 0.]),
                              mass=2,
                              friction_coeff=1,
                              restitution_coeff=0.9,
                              shape=Circle(1)),
                         ], gravity=None)


def spring_test():
    body1 = Body(position=np.array([30., 10.]),
                 velocity=np.array([0., 0.]),
                 mass=1,
                 friction_coeff=1,
                 restitution_coeff=0.9,
                 shape=Circle(1))
    body2 = InfMassBody(position=np.array([25., 10.]),
                        friction_coeff=1,
                        restitution_coeff=0.9,
                        shape=Circle(1))
    spring = Spring(body1,
                    body2,
                    k=1,
                    stationery_length=10)
    return World(bodies=[spring, body1, body2], gravity=None)


def advanced_spring_test():
    body1 = Body(position=np.array([10., 30.]),
                 velocity=np.array([0.4, 0.5]),
                 mass=1,
                 friction_coeff=1,
                 restitution_coeff=0.9,
                 shape=Circle(1))
    body2 = Body(position=np.array([10., 20.]),
                 velocity=np.array([0.4, -0.5]),
                 mass=1,
                 friction_coeff=1,
                 restitution_coeff=0.9,
                 shape=Circle(1))
    spring = Spring(body1,
                    body2,
                    k=0.5,
                    stationery_length=10)
    return World(bodies=[spring, body1, body2], gravity=None)


def swing_spring_test():
    body1 = Body(position=np.array([30., 10.]),
                 velocity=np.array([0., 0.5]),
                 mass=1,
                 friction_coeff=1,
                 restitution_coeff=0.9,
                 shape=Circle(1))
    body2 = InfMassBody(position=np.array([25., 10.]),
                        friction_coeff=1,
                        restitution_coeff=0.9,
                        shape=Circle(1))
    spring = Spring(body1,
                    body2,
                    k=1,
                    stationery_length=5)
    return World(bodies=[spring, body1, body2], gravity=None)


def spring_and_collision_test():
    body1 = Body(position=np.array([25., 5.]),
                 velocity=np.array([0.3, 0.]),
                 mass=2,
                 friction_coeff=1,
                 restitution_coeff=0.7,
                 shape=Circle(1))
    body2 = InfMassBody(position=np.array([25., 10.]),
                        friction_coeff=1,
                        restitution_coeff=0.9,
                        shape=Circle(1))
    spring = Spring(body1=body1,
                    body2=body2,
                    k=1,
                    stationery_length=5)
    return World(bodies=[spring,
                         body1,
                         body2,
                         Body(position=np.array([10., 15.]),
                              velocity=np.array([0.3, 0.]),
                              mass=1,
                              friction_coeff=1,
                              restitution_coeff=0.7,
                              shape=Circle(1)),
                         ], gravity=None)


def bounce_house_test():
    edge1 = InfMassBody(position=np.array([0., 10.]),
                        friction_coeff=1,
                        restitution_coeff=0.9,
                        shape=Circle(1))
    edge2 = InfMassBody(position=np.array([50., 10.]),
                        friction_coeff=1,
                        restitution_coeff=0.9,
                        shape=Circle(1))
    middle = Body(position=np.array([25., 9.]),
                  velocity=np.array([0., 0.]),
                  mass=2,
                  friction_coeff=1,
                  restitution_coeff=1,
                  shape=Circle(1))
    spring1 = Spring(body1=edge1,
                     body2=middle,
                     k=1,
                     stationery_length=25)
    spring2 = Spring(body1=middle,
                     body2=edge2,
                     k=1,
                     stationery_length=25)
    body = Body(position=np.array([25., 30.]),
                velocity=np.array([0., 0.]),
                mass=1,
                friction_coeff=1,
                restitution_coeff=1,
                shape=Circle(5))
    return World(bodies=[edge1, edge2, middle, body, spring1, spring2], gravity=np.array([0., -0.01]))


def advanced_bounce_house_test():
    edge1 = InfMassBody(position=np.array([0., 10.]),
                        friction_coeff=1,
                        restitution_coeff=0.9,
                        shape=Circle(1))
    edge2 = InfMassBody(position=np.array([50., 10.]),
                        friction_coeff=1,
                        restitution_coeff=0.9,
                        shape=Circle(1))
    bodies = [edge1]
    first = edge1
    length_between = 5
    for i in range(length_between, 50, length_between):
        second = Body(position=np.array([float(i), 10.]),
                      velocity=np.array([0., 0.]),
                      mass=2,
                      friction_coeff=1,
                      restitution_coeff=0.7,
                      shape=Circle(1))
        spring = Spring(body1=first,
                        body2=second,
                        k=0.1,
                        stationery_length=length_between)
        first = second
        bodies.append(second)
        bodies.append(spring)
    bodies.append(
        Spring(body1=first,
               body2=edge2,
               k=0.15,
               stationery_length=length_between)
    )
    bodies.append(edge2)
    body = Body(position=np.array([25., 30.]),
                velocity=np.array([0., 0.]),
                mass=1,
                friction_coeff=1,
                restitution_coeff=1,
                shape=Circle(5))
    bodies.append(body)
    return World(bodies=bodies, gravity=np.array([0., -0.01]))


def throwing_in_angle_test():
    body1 = Body(position=np.array([5., 5.]),
                 velocity=np.array([2., 5.]),
                 mass=1,
                 friction_coeff=1,
                 restitution_coeff=0.7,
                 shape=Circle(1))
    return World(bodies=[body1], gravity=np.array([0., -0.5]))


def convex_polygon_test():
    body1 = Body(position=np.array([5., 5.]),
                 velocity=np.array([0., 0.]),
                 mass=1,
                 friction_coeff=1,
                 restitution_coeff=0.7,
                 shape=ConvexPolygon(vertices=[np.array([-1., -1.]),
                                               np.array([1., -1.]),
                                               np.array([0., 1.])]))
    return World(bodies=[body1], gravity=None)


def rotated_convex_polygon_test():
    body1 = Body(position=np.array([5., 5.]),
                 rotation=np.pi,
                 velocity=np.array([0., 0.]),
                 mass=1,
                 friction_coeff=1,
                 restitution_coeff=0.7,
                 shape=ConvexPolygon(vertices=[np.array([-1., -1.]),
                                               np.array([1., -1.]),
                                               np.array([0., 1.])]))
    return World(bodies=[body1], gravity=None)


def rotating_convex_polygon_test():
    body1 = Body(position=np.array([5., 5.]),
                 velocity=np.array([0.1, 0.1]),
                 angular_velocity=0.1,
                 mass=1,
                 friction_coeff=1,
                 restitution_coeff=0.7,
                 shape=ConvexPolygon(vertices=[np.array([-1., -1.]),
                                               np.array([1., -1.]),
                                               np.array([0., 1.])]))
    return World(bodies=[body1], gravity=None)


def convex_polygon_vs_circle_collision_test():
    body1 = Body(position=np.array([20., 20.]),
                 velocity=np.array([0., 0.]),
                 mass=10,
                 friction_coeff=1,
                 restitution_coeff=0.7,
                 shape=ConvexPolygon(vertices=[np.array([0., 10.]),
                                               np.array([10., -10.]),
                                               np.array([-10., -10.])]))
    body2 = Body(position=np.array([45., 25.]),
                 velocity=np.array([-0.1, 0.]),
                 mass=1,
                 friction_coeff=1,
                 restitution_coeff=0.9,
                 shape=Circle(1))

    return World(bodies=[body1, body2], gravity=None)


def convex_polygon_vs_circle_corner_collision_test():
    body1 = Body(position=np.array([20., 20.]),
                 velocity=np.array([0., 0.]),
                 mass=10,
                 friction_coeff=1,
                 restitution_coeff=0.7,
                 shape=ConvexPolygon(vertices=[np.array([0., 10.]),
                                               np.array([10., -10.]),
                                               np.array([-10., -10.])]))
    body2 = Body(position=np.array([45., 10.]),
                 velocity=np.array([-0.1, 0.]),
                 mass=1,
                 friction_coeff=1,
                 restitution_coeff=0.9,
                 shape=Circle(1))

    return World(bodies=[body1, body2], gravity=None)


def trapezoid_test():
    body1 = Body(position=np.array([10., 10.]),
                 velocity=np.array([0., 0.]),
                 mass=100,
                 friction_coeff=1,
                 restitution_coeff=1,
                 shape=ConvexPolygon(vertices=[np.array([-5., -5.]),
                                               np.array([-5., 5.]),
                                               np.array([15., 5.]),
                                               np.array([5., -5.])]))
    body2 = Body(position=np.array([25., 10.]),
                 velocity=np.array([-0.1, 0.]),
                 mass=1,
                 friction_coeff=1,
                 restitution_coeff=1,
                 shape=Circle(1))
    return World(bodies=[body1, body2], gravity=None)


def two_pendulums_test():
    top = InfMassBody(position=np.array([25., 10.]),
                        friction_coeff=1,
                        restitution_coeff=0.9,
                        shape=Circle(1))
    middle = Body(position=np.array([25., 20.]),
                  velocity=np.array([0., 0.]),
                  mass=1,
                  friction_coeff=1,
                  restitution_coeff=1,
                  shape=Circle(1))
    bottom = Body(position=np.array([25., 30.]),
                  velocity=np.array([0., 0.]),
                  mass=1,
                  friction_coeff=1,
                  restitution_coeff=1,
                  shape=Circle(1))
    spring1 = Spring(body1=top,
                     body2=middle,
                     k=0.1,
                     stationery_length=10)
    spring2 = Spring(body1=middle,
                     body2=bottom,
                     k=0.1,
                     stationery_length=10)
    return World(bodies=[top, middle, bottom, spring1, spring2], gravity=np.array([0., -0.01]))


def ball_and_floor():
    ball = Body(position=np.array([2., 3.]),
                velocity=np.array([1., 4.]),
                mass=1,
                friction_coeff=0.1,
                restitution_coeff=1,
                shape=Circle(1))
    floor = InfMassBody(position=np.array([25., 0.]),
                        friction_coeff=0.1,
                        restitution_coeff=0.9,
                        shape=ConvexPolygon(vertices=[np.array([-25., -1.]),
                                                      np.array([-25., 1.]),
                                                      np.array([25., 1.]),
                                                      np.array([25., -1.])]))
    return World(bodies=[ball, floor], gravity=np.array([0., -0.9]))
