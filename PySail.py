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
        
        self.angle = start_angle  #Starting angle of the boat
        self.pos_x = start_x - 19.25 #Starting x coords of the center of the boat
        self.pos_y = start_y - 19.25 #Starting y coords of the center of the boat
        self.direction = [0, -1]
        self.speed = -0.01
        self.sail_trim = 5 #1 is in, 5 is out

    def turn_left(self, degrees):
        self.angle += degrees
        self.angle %= 360
        
    def turn_right(self, degrees):
        self.angle -= degrees 
        self.angle %= 360   
        
    def forward(self):
        self.direction[0] = math.sin(-math.radians(self.angle))
        self.direction[1] = -math.cos(math.radians(self.angle))

        self.pos_x += self.direction[0]*self.speed
        self.pos_y += self.direction[1]*self.speed
    
    def turn_180(self):
        """This is only used when the player reaches the limit of the window."""
        if self.angle < 180:
            self.angle += 180
        else:
            self.angle -= 180
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
    def sail_in(self):
        if self.sail_trim > 1:
            self.sail_trim -= 1
    
    def sail_out(self):
        if self.sail_trim < 5:
            self.sail_trim += 1
        
class Wind():        
    def __init__(self, wind_power):
        self.wind_power = wind_power  #Multiples of 2 only !
    def get_allures(self, boat_angle, sail_trim):
        self.boat_angle = boat_angle
        self.sail_trim = sail_trim #I just put this here for convenience instead of having to get it in the get_speed method.
        if self.boat_angle > 355 or self.boat_angle < 5:
            self.allure = "vent de face"
        elif self.boat_angle > 5 and self.boat_angle < 45 or self.boat_angle > 315 and self.boat_angle < 355:
            self.allure = "pres"
        elif self.boat_angle > 45 and self.boat_angle < 80 or self.boat_angle > 280 and self.boat_angle < 315:
            self.allure = "bon plein"
        elif self.boat_angle > 80 and self.boat_angle < 100 or self.boat_angle > 260 and self.boat_angle < 280:
            self.allure = "travers"
        elif self.boat_angle > 100 and self.boat_angle < 140 or self.boat_angle > 220 and self.boat_angle < 260:
            self.allure = "largue"
        elif self.boat_angle > 140 and self.boat_angle < 170 or self.boat_angle > 190 and self.boat_angle < 220:
            self.allure = "grand largue"
        elif self.boat_angle > 170 and self.boat_angle < 190:
            self.allure = "vent arriere"
        
    def get_speed(self):
        """Sets the speed of the boat accordingly to the wind angle and sail trim."""
        if self.allure == "vent de face":
            return -0.01
        elif self.allure == "pres":
            if self.sail_trim == 1:  #Best
                return 2.2
            elif self.sail_trim == 2:
                return 1.8
            elif self.sail_trim == 3:
                return 1
            elif self.sail_trim > 3:
                return 0.15
        elif self.allure == "bon plein":
            if self.sail_trim == 1:
                return 2.4
            elif self.sail_trim == 2:  #Best
                return 2.6
            elif self.sail_trim == 3:
                return 1.9
            elif self.sail_trim == 3:
                return 1.5
            elif self.sail_trim == 4:
                return 1
            elif self.sail_trim == 5:
                return 0.3
        elif self.allure == "travers":  #Fastest one
            if self.sail_trim == 1:
                return 2
            elif self.sail_trim == 2: 
                return 2.5
            elif self.sail_trim == 3:  #Best
                return 3.1
            elif self.sail_trim == 4:
                return 1.9
            elif self.sail_trim == 5:
                return 0.7
        elif self.allure == "largue":
            if self.sail_trim == 1:
                return 0.3
            elif self.sail_trim == 2:
                return 1
            elif self.sail_trim == 3:
                return 2.5
            elif self.sail_trim == 4:  #Best
                return 3
            elif self.sail_trim == 5:
                return 2.4
        elif self.allure == "grand largue":
            if self.sail_trim == 1:
                return 0.2
            elif self.sail_trim == 2:
                return 0.5
            elif self.sail_trim == 3:
                return 1.5
            elif self.sail_trim == 4:
                return 2.5
            elif self.sail_trim == 5:
                return 3
        elif self.allure == "vent arriere":
            if self.sail_trim == 1:
                return 0.1
            elif self.sail_trim == 2:
                return 0.5
            elif self.sail_trim == 3:
                return 1.6
            elif self.sail_trim == 4:
                return 2.5
            elif self.sail_trim == 5:
                return 2.9
                
class inGameHUD():
    def __init__(self):
        self.PURPLE = (128, 0, 128)
        self.WHITE  = (255, 255, 255)
        self.font = pygame.font.Font("freesansbold.ttf", 16)
        self.CORNER_OF_HUD = (RESOLUTION[0] - 100, RESOLUTION[1] - 30)
        
    def draw(self, sail_trim):
        pygame.draw.rect(screen, self.PURPLE, (self.CORNER_OF_HUD[0], self.CORNER_OF_HUD[1], 100, 30))
        text_surface = self.font.render("Sail Trim:{0}/5".format(sail_trim), True, self.WHITE)
        text_rect = (self.CORNER_OF_HUD[0] + 5, self.CORNER_OF_HUD[1] + 5)  #+'s are to center the text.
        #text_rect.center = (self.CORNER_OF_HUD[0], self.CORNER_OF_HUD[1])
        screen.blit(text_surface, text_rect)
          
class Main():
    def __init__(self):
        #Few colors, thaught I would put them here in case
        #                        R  G  B
        self.RED             = (255, 0, 0)
        self.GREEN           = (0, 255, 0)
        self.BLUE            = (0, 0, 255)
        self.PURPLE          = (128, 0, 128)
        self.LIGHT_BLUE      = (0, 128, 255)
        self.GREY            = (128, 128, 128) 
        
        self.FPS = 30
        self.fps_clock = pygame.time.Clock()
        boat = Boat(0, 320, 240)
        
    def Run(self):
        HUD = inGameHUD()
        boat = Boat(0,320, 240)
        wind = Wind(0)
        while True:
            screen.blit(boat.SEA, (0, 0))  #Blits the background
            screen.blit(pygame.transform.scale(boat.draw_boat(), (30, 30)), (boat.pos_x, boat.pos_y))  #The transform.scale is there because otherwise the boat would be way too big, a ~1/4 of the screen.
            if boat.pos_x <= -30 or boat.pos_x > RESOLUTION[0] - 30 or boat.pos_y <= -30 or boat.pos_y > RESOLUTION[1]:  #If boat is getting out of the window.
                boat.turn_180()
            else:
                boat.forward()  #Always make the boat go forward, it's a sailboat, it ain't gonna stop.
            
            for event in pygame.event.get():
                if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()          
                if event.type == KEYDOWN:
                    if event.key == K_LEFT:
                        boat.turn_left(15)
                    if event.key == K_RIGHT:
                        boat.turn_right(15)
                    if event.key == K_g:
                        boat.turn_left(5)
                    if event.key == K_h:
                        boat.turn_right(5)
                    if event.key == K_f:
                        boat.turn_left(10)
                    if event.key == K_j:
                        boat.turn_right(10)
                    if event.key == K_LCTRL or event.key == K_RCTRL:
                        boat.sail_in()
                    if event.key == K_LSHIFT or event.key == K_RSHIFT:
                        boat.sail_out()
                        
            wind.get_allures(boat.angle, boat.sail_trim)
            boat.speed = wind.get_speed()
            HUD.draw(boat.sail_trim)
            pygame.display.update()
            self.fps_clock.tick(self.FPS)
            

Game = Main()
Game.Run()
                        
