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
