from unittest import TestCase

import physics
from particle import Particle


class TestPhysics(TestCase):
    def test_collide(self):
        p1 = Particle(pos_x=0, vx=2)
        p2 = Particle(pos_x=10, vx=-2)

        self.assertFalse(physics.collide(p1, p2, dt=1.0))

        self.assertTrue(physics.collide(p1, p2, dt=3))

        self.assertTrue(physics.collide(p1, p2, dt=10))

    def test_get_collision_time_symmetric(self):
        p1 = Particle(pos_x=0.0, vx=2.0)
        p2 = Particle(pos_x=10.0, vx=-2.0)

        dt = physics.get_collision_time(p1, p2)

        self.assertAlmostEqual(dt, 2.5)

    def test_get_collision_time_asymmetric(self):
        p1 = Particle(pos_x=0.0, vx=4.0)
        p2 = Particle(pos_x=10.0, vx=-1.0)
        dt = physics.get_collision_time(p1, p2)
        self.assertAlmostEqual(dt, 2.0)

    def test_elastic_collision_symmetric(self):
        p1 = Particle(pos_x=0.0, vx=2.0)
        p2 = Particle(pos_x=10.0, vx=-2.0)

        result = physics.elastic_collision(p1, p2, dt=10.0)

        self.assertTrue(result)

        self.assertAlmostEqual(p1.get_vx(), -2.0)
        self.assertAlmostEqual(p2.get_vx(), 2.0)
