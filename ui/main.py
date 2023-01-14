# -*- encoding: utf-8 -*-
'''
@File    :   main.py
@Time    :   2022/12/26 14:09:19
@Author  :   Muyao ZHONG 
@Version :   1.0
@Contact :   zmy125616515@hotmail.com
@License :   (C)Copyright 2019-2020
@Title   :   
'''
import sys
import os
sys.path.append(os.path.abspath('./'))


import pygame,sys 
from option.settings import * 
from tools.debug import debug 
from ui.level import Level 

class Game:
    def __init__(self):
        # general setup
        
        pygame.init()
        self.screen=pygame.display.set_mode((WIDTH,HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.level = Level()
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()
              
            self.screen.fill("black")
            self.level.run()
            # debug('hello')      
            pygame.display.update()
            self.clock.tick(FPS)

if __name__ == '__main__':
    game=Game()
    game.run()