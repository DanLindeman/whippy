from math import pi, sqrt, atan2
import random
import pygame
import PyParticles

(width, height) = (400, 400)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Springs')

universe = PyParticles.Environment(width, height)
universe.colour = (255, 255, 255)
universe.addFunctions(['move', 'bounce', 'collide', 'drag', 'accelerate'])
#universe.acceleration = (pi, 0.01)
#universe.acceleration = (-1, 1)
#universe.mass_of_air = 0.02

center = (width/2, height/2)

universe.addParticles(mass=10000, size=10, speed=1, elasticity=0, colour=(0, 0, 0))
base = universe.particles[0]
for p in range(3):
    universe.addParticles(mass=100, size=6, speed=1, elasticity=0, colour=(20, 40, 200))
#for p in range(2):
    #universe.addParticles(mass=50, size=6, speed=1, elasticity=0, colour=(20, 40, 200))
#universe.addParticles(mass=10, size=6, speed=1, elasticity=0, colour=(255, 0, 0))

universe.addSpring(0, 1, length=1, strength=10)
universe.addSpring(1, 2, length=1, strength=10)
universe.addSpring(2, 3, length=1, strength=10)
#universe.addSpring(3, 4, length=1, strength=10)
#universe.addSpring(4, 5, length=1, strength=10)
#universe.addSpring(5, 6, length=1, strength=10)

"""
TODO:
Only draw whip within a center circle.
"""

"""
TODO:
While moving, make iteractions whip-like,
when not moving, make them very strong?
"""

selected_particle = universe.particles[0]
paused = False
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                paused = (True, False)[paused]
    x, y = pygame.mouse.get_pos()
    rel = pygame.mouse.get_rel()
    selected_particle.mouseMove(x, y, rate=1)
    #if rel != (0, 0):
        #print("Moving!")
    if not paused:
        universe.update()
    screen.fill(universe.colour)
    delx = center[0] - base.x
    dely = center[1] - base.y
    dist = sqrt(delx**2 + dely**2)
    angle = atan2(dely, delx)*180/pi
    if dist < 50:
        pygame.draw.circle(screen, base.colour, (int(base.x), int(base.y)), base.size, 0)
    for p in universe.particles[1:]:
        pygame.draw.circle(screen, p.colour, (int(p.x), int(p.y)), p.size, 0)
    for s in universe.springs:
        #pygame.draw.aaline(screen, (0, 0, 0), (int(s.p1.x), int(s.p1.y)), (int(s.p2.x), int(s.p2.y)))
        pygame.draw.line(screen, (0, 0, 0), (int(s.p1.x), int(s.p1.y)), (int(s.p2.x), int(s.p2.y)), 5)

    pygame.display.flip()
