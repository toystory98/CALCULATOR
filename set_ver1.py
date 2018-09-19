import pygame, sys
from pygame.locals import * 

#set color
white = (255,255,255)
red = (166,0,12)
red_dark = (125,2,11)
black = (0,0,0)
black_med = (17,17,19)
black_light = (58,58,58)
yellow_light = (255,218,108)


pygame.init()   #initialize all imported pygame modules
pygame.display.set_caption('CALCULATOR') # set window caption
screen = pygame.display.set_mode((350,500)) # set window size
screen.fill(white) # set window background color
font = pygame.font.SysFont('Arial', 60) # set normal font
font_med = pygame.font.SysFont('Arial', 40) # set medium font that smaller than normal font
