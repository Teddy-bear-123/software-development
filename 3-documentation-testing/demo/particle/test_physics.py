from unittest import TestCase
from particle import Particle
import physics


class TestPhysics(TestCase):
    def test_collide(self):
        # 1 - build two particles going to collide
        # 2 - test physics.collide() with a dt too short (no collision)
        # 3 - test physics.collide() with a dt just OK
        # 4 - test physics.collide() with a dt larger than OK
        raise NotImplementedError("TODO: test collide()")

    def test_get_collision_time_symmetric(self):
        # 1 - build two particles in a symmetric configuration
        # 2 - check get_collision_time()
        raise NotImplementedError("TODO: test get_collision_time(), symmetric case")

    def test_get_collision_time_asymmetric(self):
        # 1 - build two particles in an asymmetric configuration
        # 2 - check get_collision_time()
        raise NotImplementedError("TODO: test get_collision_time(), asymmetric case")

    def test_elastic_collision_symmetric(self):
        # 1 - build two particles in a symmetric configuration
        # 2 - call elastic_collision() with a valid dt
        # 3 - check the return status
        # 4 - check both particles' new properties
        raise NotImplementedError("TODO: test elastic_collision()")
