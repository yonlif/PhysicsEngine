import numpy as np

from bodies.body import Body, InfMassBody
from bodies.shapes import Circle
from world import World
from bodies.spring import Spring


def inf_mass_test():
    return World(bodies=[Body(position=np.array([30., 10.]),
                              velocity=np.array([-1., 0.]),
                              mass=1,
                              friction_coeff=1,
                              restitution_coeff=0.9,
                              shape=Circle(1)),
                         InfMassBody(position=np.array([20., 10.]),
                                     friction_coeff=1,
                                     restitution_coeff=0.9,
                                     shape=Circle(1))
                         ])


def two_mass_test():
    return World(bodies=[Body(position=np.array([30., 10.]),
                              velocity=np.array([-1., 0.]),
                              mass=1,
                              friction_coeff=1,
                              restitution_coeff=0.9,
                              shape=Circle(1)),
                         Body(position=np.array([0., 10.5]),
                              velocity=np.array([2., 0.]),
                              mass=2,
                              friction_coeff=1,
                              restitution_coeff=0.9,
                              shape=Circle(1)),
                         ])


def single_mass_test():
    return World(bodies=[Body(position=np.array([30., 10.]),
                              velocity=np.array([-1., 0.]),
                              mass=1,
                              friction_coeff=1,
                              restitution_coeff=0.9,
                              shape=Circle(1)),
                         ])


def spring_test():
    spring = Spring(body1=Body(position=np.array([30., 10.]),
                               velocity=np.array([0., 0.]),
                               mass=1,
                               friction_coeff=1,
                               restitution_coeff=0.9,
                               shape=Circle(1)),
                    body2=InfMassBody(position=np.array([25., 10.]),
                                      friction_coeff=1,
                                      restitution_coeff=0.9,
                                      shape=Circle(1)),
                    k=1,
                    stationery_length=10)
    return World(bodies=[spring])


def advanced_spring_test():
    spring = Spring(body1=Body(position=np.array([10., 30.]),
                               velocity=np.array([2., 5.]),
                               mass=1,
                               friction_coeff=1,
                               restitution_coeff=0.9,
                               shape=Circle(1)),
                    body2=Body(position=np.array([10., 20.]),
                               velocity=np.array([2., -5.]),
                               mass=1,
                               friction_coeff=1,
                               restitution_coeff=0.9,
                               shape=Circle(1)),
                    k=1,
                    stationery_length=10)
    return World(bodies=[spring])


def swing_spring_test():
    spring = Spring(body1=Body(position=np.array([30., 10.]),
                               velocity=np.array([0., 5.]),
                               mass=1,
                               friction_coeff=1,
                               restitution_coeff=0.9,
                               shape=Circle(1)),
                    body2=InfMassBody(position=np.array([25., 10.]),
                                      friction_coeff=1,
                                      restitution_coeff=0.9,
                                      shape=Circle(1)),
                    k=1,
                    stationery_length=5)
    return World(bodies=[spring])
