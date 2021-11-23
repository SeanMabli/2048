import numpy as np
import pygame

Display = pygame.display.set_mode([201, 201])

Board = np.zeros((4, 4), dtype=int)
PreviousBoard = np.zeros((4, 4), dtype=int)

def NewRandom(Num):
  global Board
  for _ in range(Num):
    if 0 in Board:
      Random = np.random.randint(0, 4, 2)
      while Board[Random[0], Random[1]] != 0:
        Random = np.random.randint(0, 4, 2)
      Board[Random[0], Random[1]] = np.random.choice([2, 4], p=[0.9, 0.1])

NewRandom(2)

pygame.init()
pygame.display.set_caption('2048')

done = False

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

while not np.array_equal(PreviousBoard, Board):
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      PreviousBoard = Board

    # Display
    Display.fill(BLACK)

    for i in range(3):
      pygame.draw.line(Display, WHITE, (i * 50 + 50, 0), (i * 50 + 50, 201))
      pygame.draw.line(Display, WHITE, (0, i * 50 + 50), (201, i * 50 + 50))

    for i in range(4):
      for j in range(4):
        if Board[j, i] != 0:
          Display.blit(pygame.font.SysFont("Raleway", 24).render(str(Board[j, i]), 1, WHITE), (i * 50 + (4 - len(str(Board[j, i]))) * 5 + 6, j * 50 + 20))
    
    # User Input
    if event.type == pygame.KEYDOWN:
      if (event.key == pygame.K_UP):
        PreviousBoard = Board.copy()
        for _ in range(3):
          for i in reversed(range(3)):
            for j in range(4):
              if Board[i, j] == Board[i + 1, j]:
                Board[i, j] *= 2
                Board[i + 1, j] = 0
              if Board[i, j] == 0:
                Board[i, j] = Board[i + 1, j]
                Board[i + 1, j] = 0
        NewRandom(1)

      if (event.key == pygame.K_RIGHT):
        PreviousBoard = Board.copy()
        for _ in range(3):
          for i in range(4):
            for j in range(1, 4):
              if Board[i, j] == Board[i, j - 1]:
                Board[i, j] *= 2
                Board[i, j - 1] = 0
              if Board[i, j] == 0:
                Board[i, j] = Board[i, j - 1]
                Board[i, j - 1] = 0
        NewRandom(1)

      if (event.key == pygame.K_DOWN):
        PreviousBoard = Board.copy()
        for _ in range(3):
          for i in range(1, 4):
            for j in range(4):
              if Board[i, j] == Board[i - 1, j]:
                Board[i, j] *= 2
                Board[i - 1, j] = 0
              if Board[i, j] == 0:
                Board[i, j] = Board[i - 1, j]
                Board[i - 1, j] = 0
        NewRandom(1)

      if (event.key == pygame.K_LEFT):
        PreviousBoard = Board.copy()
        for _ in range(3):
          for i in range(4):
            for j in reversed(range(3)):
              if Board[i, j] == Board[i, j + 1]:
                Board[i, j] *= 2
                Board[i, j + 1] = 0
              if Board[i, j] == 0:
                Board[i, j] = Board[i, j + 1]
                Board[i, j + 1] = 0
        NewRandom(1)

    pygame.display.flip()

pygame.quit()