# myke - test pygame 2021-08-03 1.0

import pygame
from pygame.locals import *

# ti = pygame.init()
# print(ti)
# f = pygame.font.init()
# print(f)

pygame.init()
display_width = 800
display_height = 600
game_display = pygame.display.set_mode((display_width, display_height))

pygame.display.update()

#while True:
  #for event in pygame.event.get():
    #print(event)

while True:
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
quit()
