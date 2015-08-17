#!/usr/bin/python
#Python version is 2.7.6
#Author: Martin Schmidt aka qw2100m
#READ THE README
#Oh and all the '- 19.25' throughout this code are so that coords of an img are the ones of the center of that img instead of it's top left corner.

import sys
import math
import random
import pygame
from pygame.locals import *

pygame.init()
RESOLUTION = (640, 480)
screen = pygame.display.set_mode(RESOLUTION)
pygame.display.set_caption("PySail")


class Boat():
    
    def __init__(self, start_angle, start_x, start_y):
        #Images of the HB16 under all the possible angles for the game.
        self.HB16_0   = pygame.image.load("Art/HB16_0.png")
        self.HB16_5   = pygame.image.load("Art/HB16_5.png")
        self.HB16_10  = pygame.image.load("Art/HB16_10.png")
        self.HB16_15  = pygame.image.load("Art/HB16_15.png")
        self.HB16_20  = pygame.image.load("Art/HB16_20.png")
        self.HB16_25  = pygame.image.load("Art/HB16_25.png")
        self.HB16_30  = pygame.image.load("Art/HB16_30.png")
        self.HB16_35  = pygame.image.load("Art/HB16_35.png")
        self.HB16_40  = pygame.image.load("Art/HB16_40.png")
        self.HB16_45  = pygame.image.load("Art/HB16_45.png")
        self.HB16_50  = pygame.image.load("Art/HB16_50.png")
        self.HB16_55  = pygame.image.load("Art/HB16_55.png")
        self.HB16_60  = pygame.image.load("Art/HB16_60.png")
        self.HB16_65  = pygame.image.load("Art/HB16_65.png")
        self.HB16_70  = pygame.image.load("Art/HB16_70.png")
        self.HB16_75  = pygame.image.load("Art/HB16_75.png")
        self.HB16_80  = pygame.image.load("Art/HB16_80.png")
        self.HB16_85  = pygame.image.load("Art/HB16_85.png")
        self.HB16_90  = pygame.image.load("Art/HB16_90.png")
        self.HB16_95  = pygame.image.load("Art/HB16_95.png")
        self.HB16_100 = pygame.image.load("Art/HB16_100.png")
        self.HB16_105 = pygame.image.load("Art/HB16_105.png")
        self.HB16_110 = pygame.image.load("Art/HB16_110.png")
        self.HB16_115 = pygame.image.load("Art/HB16_115.png")
        self.HB16_120 = pygame.image.load("Art/HB16_120.png")
        self.HB16_125 = pygame.image.load("Art/HB16_125.png")
        self.HB16_130 = pygame.image.load("Art/HB16_130.png")
        self.HB16_135 = pygame.image.load("Art/HB16_135.png")
        self.HB16_140 = pygame.image.load("Art/HB16_140.png")
        self.HB16_145 = pygame.image.load("Art/HB16_145.png")
        self.HB16_150 = pygame.image.load("Art/HB16_150.png")
        self.HB16_155 = pygame.image.load("Art/HB16_155.png")
        self.HB16_160 = pygame.image.load("Art/HB16_160.png")
        self.HB16_165 = pygame.image.load("Art/HB16_165.png")
        self.HB16_170 = pygame.image.load("Art/HB16_170.png")
        self.HB16_175 = pygame.image.load("Art/HB16_175.png")
        self.HB16_180 = pygame.image.load("Art/HB16_180.png")
        self.HB16_185 = pygame.image.load("Art/HB16_185.png")
        self.HB16_190 = pygame.image.load("Art/HB16_190.png")
        self.HB16_195 = pygame.image.load("Art/HB16_195.png")
        self.HB16_200 = pygame.image.load("Art/HB16_200.png")
        self.HB16_205 = pygame.image.load("Art/HB16_205.png")
        self.HB16_210 = pygame.image.load("Art/HB16_210.png")
        self.HB16_215 = pygame.image.load("Art/HB16_215.png")
        self.HB16_220 = pygame.image.load("Art/HB16_220.png")
        self.HB16_225 = pygame.image.load("Art/HB16_225.png")
        self.HB16_230 = pygame.image.load("Art/HB16_230.png")
        self.HB16_235 = pygame.image.load("Art/HB16_235.png")
        self.HB16_240 = pygame.image.load("Art/HB16_240.png")
        self.HB16_245 = pygame.image.load("Art/HB16_245.png")
        self.HB16_250 = pygame.image.load("Art/HB16_250.png")
        self.HB16_255 = pygame.image.load("Art/HB16_255.png")
        self.HB16_260 = pygame.image.load("Art/HB16_260.png")
        self.HB16_265 = pygame.image.load("Art/HB16_265.png")
        self.HB16_270 = pygame.image.load("Art/HB16_270.png")
        self.HB16_275 = pygame.image.load("Art/HB16_275.png")
        self.HB16_280 = pygame.image.load("Art/HB16_280.png")
        self.HB16_285 = pygame.image.load("Art/HB16_285.png")
        self.HB16_290 = pygame.image.load("Art/HB16_290.png")
        self.HB16_295 = pygame.image.load("Art/HB16_295.png")
        self.HB16_300 = pygame.image.load("Art/HB16_300.png")
        self.HB16_305 = pygame.image.load("Art/HB16_305.png")
        self.HB16_310 = pygame.image.load("Art/HB16_310.png")
        self.HB16_315 = pygame.image.load("Art/HB16_315.png")
        self.HB16_320 = pygame.image.load("Art/HB16_320.png")
        self.HB16_325 = pygame.image.load("Art/HB16_325.png")
        self.HB16_330 = pygame.image.load("Art/HB16_330.png")
        self.HB16_335 = pygame.image.load("Art/HB16_335.png")
        self.HB16_340 = pygame.image.load("Art/HB16_340.png")
        self.HB16_345 = pygame.image.load("Art/HB16_345.png")
        self.HB16_350 = pygame.image.load("Art/HB16_350.png")
        self.HB16_355 = pygame.image.load("Art/HB16_355.png")
        self.SEA      = pygame.image.load("Art/sea.png") #Image of the sea for the background
        
        #Few colors, thaught I would put them here in case
        #                        R  G  B
        self.RED             = (255, 0, 0)
        self.GREEN           = (0, 255, 0)
        self.BLUE            = (0, 0, 255)
        self.PURPLE          = (128, 0, 128)
        self.LIGHT_BLUE      = (0, 128, 255)
        self.GREY            = (128, 128, 128)        
        
        self.angle = start_angle  #Starting angle of the boat
        self.pos_x = start_x - 19.25 #Starting x coords of the center of the boat
        self.pos_y = start_y - 19.25 #Starting y coords of the center of the boat
        self.direction = [0, -1]
        self.speed = 1
        

    def turn_left(self):
        self.angle += 5
        self.angle %= 360
        
    def turn_right(self):
        self.angle -= 5 
        self.angle %= 360   
        
    def forward(self):
        self.direction[0] = math.sin(-math.radians(self.angle))
        self.direction[1] = -math.cos(math.radians(self.angle))

        self.pos_x += self.direction[0]*self.speed
        self.pos_y += self.direction[1]*self.speed
        
    
    



    def draw_boat(self):
        """Just returns the surface of the boat_img angled the right way."""
        if self.angle == 0:
            return self.HB16_0
        elif self.angle == 5:
            return self.HB16_5
        elif self.angle == 10:
            return self.HB16_10
        elif self.angle == 15:
            return self.HB16_15
        elif self.angle == 20:
            return self.HB16_20
        elif self.angle == 25:
            return self.HB16_25
        elif self.angle == 30:
            return self.HB16_30
        elif self.angle == 35:
            return self.HB16_35
        elif self.angle == 40:
            return self.HB16_40
        elif self.angle == 45:
            return self.HB16_45
        elif self.angle == 50:
            return self.HB16_50
        elif self.angle == 55:
            return self.HB16_55
        elif self.angle == 60:
            return self.HB16_60
        elif self.angle == 65:
            return self.HB16_65
        elif self.angle == 70:
            return self.HB16_70
        elif self.angle == 75:
            return self.HB16_75
        elif self.angle == 80:
            return self.HB16_80
        elif self.angle == 85:
            return self.HB16_85
        elif self.angle == 90:
            return self.HB16_90
        elif self.angle == 95:
            return self.HB16_95
        elif self.angle == 100:
            return self.HB16_100
        elif self.angle == 105:
            return self.HB16_105
        elif self.angle == 110:
            return self.HB16_110
        elif self.angle == 115:
            return self.HB16_115
        elif self.angle == 120:
            return self.HB16_120
        elif self.angle == 125:
            return self.HB16_125
        elif self.angle == 130:
            return self.HB16_130
        elif self.angle == 135:
            return self.HB16_135
        elif self.angle == 140:
            return self.HB16_140
        elif self.angle == 145:
            return self.HB16_145
        elif self.angle == 150:
            return self.HB16_150
        elif self.angle == 155:
            return self.HB16_155
        elif self.angle == 160:
            return self.HB16_160
        elif self.angle == 165:
            return self.HB16_165
        elif self.angle == 170:
            return self.HB16_170
        elif self.angle == 175:
            return self.HB16_175
        elif self.angle == 180:
            return self.HB16_180
        elif self.angle == 185:
            return self.HB16_185
        elif self.angle == 190:
            return self.HB16_190
        elif self.angle == 195:
            return self.HB16_195
        elif self.angle == 200:
            return self.HB16_200
        elif self.angle == 205:
            return self.HB16_205
        elif self.angle == 210:
            return self.HB16_210
        elif self.angle == 215:
            return self.HB16_215
        elif self.angle == 220:
            return self.HB16_220
        elif self.angle == 225:
            return self.HB16_225
        elif self.angle == 230:
            return self.HB16_230
        elif self.angle == 235:
            return self.HB16_235
        elif self.angle == 240:
            return self.HB16_240
        elif self.angle == 245:
            return self.HB16_245
        elif self.angle == 250:
            return self.HB16_250
        elif self.angle == 255:
            return self.HB16_255
        elif self.angle == 260:
            return self.HB16_260
        elif self.angle == 265:
            return self.HB16_265
        elif self.angle == 270:
            return self.HB16_270
        elif self.angle == 275:
            return self.HB16_275
        elif self.angle == 280:
            return self.HB16_280
        elif self.angle == 285:
            return self.HB16_285
        elif self.angle == 290:
            return self.HB16_290
        elif self.angle == 295:
            return self.HB16_295
        elif self.angle == 300:
            return self.HB16_300
        elif self.angle == 305:
            return self.HB16_305
        elif self.angle == 310:
            return self.HB16_310
        elif self.angle == 315:
            return self.HB16_315
        elif self.angle == 320:
            return self.HB16_320
        elif self.angle == 325:
            return self.HB16_325
        elif self.angle == 330:
            return self.HB16_330
        elif self.angle == 335:
            return self.HB16_335
        elif self.angle == 340:
            return self.HB16_340
        elif self.angle == 345:
            return self.HB16_345
        elif self.angle == 350:
            return self.HB16_350
        elif self.angle == 355:
            return self.HB16_355
        
        
        
class Main():
    def __init__(self):
        self.FPS = 30
        self.fps_clock = pygame.time.Clock()
        boat = Boat(0, 320, 240)
        
    def Run(self):
        boat = Boat(0,320, 240)
        while True:
            screen.blit(boat.SEA, (0, 0))  #Blits the background
            screen.blit(pygame.transform.scale(boat.draw_boat(), (40, 40)), (boat.pos_x, boat.pos_y))  #The transform.scale is there because otherwise the boat would be way too big, a ~1/4 of the screen.
            boat.forward()  #Always make the boat go forward, it's a sailboat, it ain't gonna stop.
            for event in pygame.event.get():
                if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()          
                if event.type == KEYDOWN:
                    if event.key == K_LEFT:
                        boat.turn_left()
                    if event.key == K_RIGHT:
                        boat.turn_right()
                        
            pygame.display.update()
            self.fps_clock.tick(self.FPS)
            
Game = Main()
Game.Run()
                        
