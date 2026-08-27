from particle import Particle


def collide(particle1: Particle, particle2: Particle, dt) -> bool:
    # distance now, and distance after dt if nothing collides in between
    delta_before = particle1.get_x() - particle2.get_x()
    delta_after = (particle1.get_x() + particle1.get_vx() * dt) - (
        particle2.get_x() + particle2.get_vx() * dt
    )
    if delta_before == 0 or delta_after == 0:
        return True
    # sign flip between before/after means the particles crossed paths
    return delta_after / delta_before < 0


def get_collision_time(particle1: Particle, particle2: Particle):
    # x1 + v1*dt == x2 + v2*dt  =>  dt = (x2 - x1) / (v1 - v2)
    return (particle2.get_x() - particle1.get_x()) / (
        particle1.get_vx() - particle2.get_vx()
    )


def move_to_collision_point(particle1: Particle, particle2: Particle) -> float:
    dt_collision = get_collision_time(particle1, particle2)
    particle1.move(dt_collision)
    particle2.move(dt_collision)
    return dt_collision


def elastic_collision(particle1: Particle, particle2: Particle, dt) -> bool:
    if not collide(particle1, particle2, dt):
        return False

    dt_collision = move_to_collision_point(particle1, particle2)

    u1, m1 = particle1.get_vx(), particle1.get_mass()
    u2, m2 = particle2.get_vx(), particle2.get_mass()

    v1 = (u1 * (m1 - m2) + 2 * m2 * u2) / (m1 + m2)
    v2 = (u2 * (m2 - m1) + 2 * m1 * u1) / (m2 + m1)

    particle1.set_vx(v1)
    particle2.set_vx(v2)

    dt_rest = dt - dt_collision
    particle1.move(dt_rest)
    particle2.move(dt_rest)

    return True
