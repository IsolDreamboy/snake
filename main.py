import pygame
import random

pygame.init()
tela = pygame.display.set_mode((800, 600))
relogio= pygame.time.Clock()


snake_pos= [[100, 50], [90, 50], [80, 50]]
direcao = [10,0]
comida_pos = [random.randrange(0,600,10), random.randrange(0,400,10)]

# Loop Principal
rodando = True
while rodando:
   for event in pygame.event.get():
        if event.type == pygame.QUIT:
          rodando = False
          break
        elif event.type == pygame.KEYDOWN:
          if event.key == pygame.K_UP: direcao = [0, -10]
          if event.key == pygame.K_DOWN: direcao = [0, 10]
          if event.key == pygame.K_LEFT: direcao = [-10, 0]
          if event.key == pygame.K_RIGHT: direcao = [10, 0]
        if not rodando:
            break
        # Atualiza posição da cabeça
        nova_cabeca = [snake_pos[0][0] + direcao[0], snake_pos[0][1] + direcao[1]]
        snake_pos.insert(0, nova_cabeca)

        # Lógica de Colisão/Comida
        if snake_pos[0] == comida_pos:
            comida_pos = [random.randrange(0, 600, 10), random.randrange(0, 400, 10)]
        else:
            snake_pos.pop()

        # Desenho
        tela.fill((0, 0, 0))
        for pedaco in snake_pos:
            pygame.draw.rect(tela, (0, 255, 0), [pedaco[0], pedaco[1], 10, 10])
        pygame.draw.rect(tela, (255, 0, 0), [comida_pos[0], comida_pos[1], 10, 10])
        
        pygame.display.update()
        relogio.tick(15)

pygame.quit()