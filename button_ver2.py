import pygame, sys   #import pygame modules
from pygame.locals import * 
from set_ver2 import *

class button:   #creat button class
    
    class num:      # set number and key button that have same button size
        def __init__(self,t):  # set coordinates for each number and key about location of each button
            
            Ax = [32,106,180,254]
            Ay = [110,184,258,332,406]

            if t in '7':  
                x = 32
                y = 110
            if t == '8':  
                x = 106
                y = 110
            if t == '9':   
                x = 180
                y = 110
            if t == '+':   
                x = 254
                y = 110
            if t == '4':   
                x = 32
                y = 184
            if t == '5':   
                x = 106
                y = 184
            if t == '6':
                x = 180 
                y = 184
            if t == '-':
                x = 254 
                y = 184
            if t == '1':
                x = 32 
                y = 258
            if t == '2':
                x = 106 
                y = 258
            if t == '3':
                x = 180 
                y = 258
            if t == '*':
                x = 254 
                y = 258
            if t == '.':
                x = 32 
                y = 332
            if t == '0':
                x = 106 
                y = 332
            if t == 'D':
                x = 180 
                y = 332
            if t == '/':
                x = 254 
                y = 332
            if t == '=':
                x = 32
                y = 406
            
            if t == '(':
                x = 106
                y = 406

            if t == ')':
                x = 180
                y = 406

            if t == 'C':
                x = 254
                y = 406
                
            self.x = x   # for use button x-coordinate
            self.y = y   # for use button y-coordinate
            self.click = pygame.draw.rect(screen,black_light, (x, y, 70, 70))  # for use button coordinates
            mouse = pygame.mouse.get_pos()   # get mouse position
            if x+70 > mouse[0] > x and y+70 > mouse[1] > y:  # if mouse in button position
                pygame.draw.rect(screen,black_light, (x, y, 70, 70))  #button color is lighter
                screen.blit(font.render(t,True,white), ((x+23,y+18)))  #set text in button
            else:
                pygame.draw.rect(screen,black_med, (x, y, 70, 70))  #button color is normal
                screen.blit(font.render(t,True,white), ((x+23,y+18)))
                