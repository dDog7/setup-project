import pygame
import data.scripts.engine as engine
import data.scripts.settings as settings

pygame.init()
display = pygame.display.set_mode((1920, 1080), pygame.OPENGL|pygame.FULLSCREEN|pygame.HWACCEL|pygame.DOUBLEBUF)
screen = pygame.Surface((1920, 1080))
engine.screen = screen
clock = pygame.time.Clock()
engine.clock = clock
shader = engine.Shader((1920, 1080), (1920, 1080), (0, 0), 'data/shaders/vertex.glsl', 'data/shaders/fragment.glsl', display)

fpsCap = 60

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((255, 0, 255))
    engine.clear((255, 0, 255))
    
    engine.update()
    pygame.display.flip()
    shader.render(screen)
    engine.dt = clock.tick(fpsCap) / 1000
pygame.quit()
