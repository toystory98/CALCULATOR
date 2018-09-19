import pygame, sys   #import pygame modules
from pygame.locals import *
from button_ver2 import *
from set_ver2 import *

def is_click(self):  # mouse click function
    return pygame.mouse.get_pressed()[0] and self.collidepoint(pygame.mouse.get_pos()) 

def is_press(self): # keyboard press function
    return pygame.key.get_pressed()[self]

def main(): # main function
    start = True
    equasion = ''

    while start: # pygame main loop
        
        pygame.display.update() # update display
        
        # set button
        b_0 = button.num('0')
        b_1 = button.num('1')
        b_2 = button.num('2')
        b_3 = button.num('3')
        b_4 = button.num('4')
        b_5 = button.num('5')
        b_6 = button.num('6')
        b_7 = button.num('7')
        b_8 = button.num('8')
        b_9 = button.num('9')
        b_plus = button.num('+')
        b_minus = button.num('-')
        b_multi = button.num('*')
        b_divide = button.num('/')
        b_dot = button.num('.')
        b_cancle = button.num('C')
        b_ans = button.num('=')
        b_t1 = button.num('(')
        b_t2 = button.num(')')
        b_del = button.num('D')

        for event in pygame.event.get():  #	events from the queue
            
            if event.type == pygame.MOUSEMOTION: # set mouse
                rectpos = event.pos 
            if event.type == pygame.MOUSEBUTTONDOWN or pygame.KEYDOWN: # if use click mouse and pressed key
                if is_click(b_1.click) or is_press(pygame.K_1): #if click button on window or press key on keyboard
                    equasion = equasion + '1'   # equasion append 1
                if is_click(b_2.click) or is_press(pygame.K_2):
                    equasion = equasion + '2'
                if is_click(b_3.click) or is_press(pygame.K_3):
                    equasion = equasion + '3'
                if is_click(b_4.click) or is_press(pygame.K_4):
                    equasion = equasion + '4'
                if is_click(b_5.click) or is_press(pygame.K_5):
                    equasion = equasion + '5'
                if is_click(b_6.click) or is_press(pygame.K_6):
                    equasion = equasion + '6'
                if is_click(b_7.click) or is_press(pygame.K_7):
                    equasion = equasion + '7'
                if is_click(b_8.click) or is_press(pygame.K_8):
                    equasion = equasion + '8'
                if is_click(b_9.click) or is_press(pygame.K_9):
                    equasion = equasion + '9'
                if is_click(b_0.click) or is_press(pygame.K_0):
                    equasion = equasion + '0'
                if is_click(b_plus.click) or is_press(pygame.K_EQUALS):
                    equasion = equasion + '+'
                if is_click(b_minus.click) or is_press(pygame.K_MINUS):
                    equasion = equasion + '-'
                if is_click(b_multi.click) or is_press(pygame.K_x):
                    equasion = equasion + '*'
                if is_click(b_divide.click) or is_press(pygame.K_SLASH):
                    equasion = equasion + '/'
                if is_click(b_dot.click) or is_press(pygame.K_PERIOD):
                    equasion = equasion + '.'
                if is_click(b_t1.click) or is_press(pygame.K_LEFTBRACKET):
                    equasion = equasion + '('
                if is_click(b_t2.click) or is_press(pygame.K_RIGHTBRACKET):
                    equasion = equasion + ')'
                if is_click(b_del.click) or is_press(pygame.K_BACKSPACE):
                    equasion = equasion[:-1]   # delete last string
                if is_click(b_cancle.click) or is_press(pygame.K_c):
                    equasion = '' # reset equasion
                if is_click(b_ans.click) or is_press(pygame.K_RETURN):
                    if equasion == '' :    # if enter = while not have input
                        pass    # no effect to window
                    elif '/0' in equasion:    # if number divide by 0 
                        equasion = 'Syntax Error'    # display show Syntax Error
                    elif equasion[0] in '*/':    # if equasion start by * or /
                        equasion = 'Syntax Error'    # display show Syntax Error
                    elif equasion[-1] in '+-*/':    # if equasion end by + or - or * or /
                        equasion = 'Syntax Error'    # display show Syntax Error
                    elif '++' in equasion:     # if in equasion have + stuck together (ex.++)
                        equasion = 'Syntax Error'   # display show Syntax Error
                    elif '--' in equasion:      # if in equasion have - stuck together (ex.--)
                        equasion = 'Syntax Error'   # display show Syntax Error
                    elif '//' in equasion:      # if in equasion have / stuck together (ex.//)
                        equasion = 'Syntax Error'   # display show Syntax Error
                    else :
                        equasion = str(eval(equasion))   # summary equasion
                    
                if len(equasion)>=18:  # set lenght of equasion not over 18
                    equasion = equasion[:-1]  

        pygame.draw.rect(screen,corel, (32, 20, 293, 75))   # set rectan to show equasion         
        screen.blit(font_med.render(equasion,True,black), ((34,50)))  # set equasion font
        
        if event.type == QUIT or is_press(K_ESCAPE):  # close pygame if close window or press esc key
            start = False
        
        

main() # call main function

pygame.quit() # quit pygame
quit()


