import pygame
import data.scripts.settings as settings
from pymunk import Vec2d

pygame.init()
display = pygame.display.set_mode((1920, 1080), pygame.OPENGL|pygame.FULLSCREEN|pygame.HWACCEL|pygame.DOUBLEBUF)
import data.scripts.engine as engine
screen = pygame.Surface((1920, 1080))
engine.screen = screen
clock = pygame.time.Clock()
engine.clock = clock
shader = engine.Shader((1920, 1080), (1920, 1080), (0, 0), 'data/shaders/vertex.glsl', 'data/shaders/fragment.glsl', display)


floor = engine.Object(engine.colorImg(engine.square, (255, 255, 255), (120, 90, 0)), Vec2d(960, 540+256), 0, Vec2d(1728, 96))
box1 = engine.PhysicsObject(engine.square, Vec2d(960-16, 64), 0, Vec2d(32, 32))
box2 = engine.PhysicsObject(engine.square, Vec2d(960+8, 16), 0, Vec2d(32, 32))
engine.debugProperties.append(None)


fpsCap = 60
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_PAUSE:
                engine.debugMenuEnabled = not engine.debugMenuEnabled
            if event.key == pygame.K_SPACE:
                box2.body.velocity = Vec2d(box2.body.velocity.x, -500)
    screen.fill((19, 19, 19))
    engine.clear((19, 19, 19))
    keys_pressed = pygame.key.get_pressed()
    mouse_pressed = pygame.mouse.get_pressed()

    floor.update()
    box1.update()
    box2.update()
    if keys_pressed[pygame.K_a]:
        box2.body.velocity = Vec2d(-200, box2.body.velocity.y)
    if keys_pressed[pygame.K_d]:
        box2.body.velocity = Vec2d(200, box2.body.velocity.y)
    
    engine.debugProperties[0] = f'1: {box1.body.angle}, 2: {box2.body.angle}'
    engine.update()
    shader.render(screen)
    pygame.display.flip()
    engine.dt = clock.tick(fpsCap) / 1000
pygame.quit()