from unittest import TestCase

from particle import Particle


class TestParticle(TestCase):
    def test_constructor(self):
        p = Particle(pos_x=0.0, vx=2.0)
        self.assertEqual(p.get_x(), 0.0)
        self.assertEqual(p.get_vx(), 2.0)

    def test_move(self):
        p = Particle(pos_x=0.0, vx=2.0)
        p.move(dt=3.0)
        self.assertEqual(p.get_x(), 6.0)
