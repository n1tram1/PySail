#!/usr/bin/python
#Python version is 2.7.9
#Author: Martin Schmidt aka qw2100m
#READ THE README
#Oh and all the '- 19.25' throughout this code are so that coords of an img are the ones of the center of that img instead of it's top left corner.

import sys
import math
import time
import threading
import socket
import pickle
import random
import pygame
from pygame.locals import *

pygame.init()
RESOLUTION = [640, 480]
pygame.display.set_caption("PySail")
FPS = 60

def set_resolution(x_res, y_res):
    global RESOLUTION
    RESOLUTION = [x_res, y_res]
    global screen
    screen = pygame.display.set_mode(RESOLUTION)
            
class Boat():    
    def __init__(self, start_angle, start_x, start_y):
        #Images of the HB16 under all the possible angles for the game.
        #pygame.transform.scale(boat.boat_img, (30, 30))
        self.HB16_0   = pygame.transform.scale(pygame.image.load("Art/HB16_0.png"), (30, 30))
        self.HB16_5   = pygame.transform.scale(pygame.image.load("Art/HB16_5.png"), (30, 30))
        self.HB16_10  = pygame.transform.scale(pygame.image.load("Art/HB16_10.png"), (30, 30))
        self.HB16_15  = pygame.transform.scale(pygame.image.load("Art/HB16_15.png"), (30, 30))
        self.HB16_20  = pygame.transform.scale(pygame.image.load("Art/HB16_20.png"), (30, 30))
        self.HB16_25  = pygame.transform.scale(pygame.image.load("Art/HB16_25.png"), (30, 30))
        self.HB16_30  = pygame.transform.scale(pygame.image.load("Art/HB16_30.png"), (30, 30))
        self.HB16_35  = pygame.transform.scale(pygame.image.load("Art/HB16_35.png"), (30, 30))
        self.HB16_40  = pygame.transform.scale(pygame.image.load("Art/HB16_40.png"), (30, 30))
        self.HB16_45  = pygame.transform.scale(pygame.image.load("Art/HB16_45.png"), (30, 30))
        self.HB16_50  = pygame.transform.scale(pygame.image.load("Art/HB16_50.png"), (30, 30))
        self.HB16_55  = pygame.transform.scale(pygame.image.load("Art/HB16_55.png"), (30, 30))
        self.HB16_60  = pygame.transform.scale(pygame.image.load("Art/HB16_60.png"), (30, 30))
        self.HB16_65  = pygame.transform.scale(pygame.image.load("Art/HB16_65.png"), (30, 30))
        self.HB16_70  = pygame.transform.scale(pygame.image.load("Art/HB16_70.png"), (30, 30))
        self.HB16_75  = pygame.transform.scale(pygame.image.load("Art/HB16_75.png"), (30, 30))
        self.HB16_80  = pygame.transform.scale(pygame.image.load("Art/HB16_80.png"), (30, 30))
        self.HB16_85  = pygame.transform.scale(pygame.image.load("Art/HB16_85.png"), (30, 30))
        self.HB16_90  = pygame.transform.scale(pygame.image.load("Art/HB16_90.png"), (30, 30))
        self.HB16_95  = pygame.transform.scale(pygame.image.load("Art/HB16_95.png"), (30, 30))
        self.HB16_100 = pygame.transform.scale(pygame.image.load("Art/HB16_100.png"), (30, 30))
        self.HB16_105 = pygame.transform.scale(pygame.image.load("Art/HB16_105.png"), (30, 30))
        self.HB16_110 = pygame.transform.scale(pygame.image.load("Art/HB16_110.png"), (30, 30))
        self.HB16_115 = pygame.transform.scale(pygame.image.load("Art/HB16_115.png"), (30, 30))
        self.HB16_120 = pygame.transform.scale(pygame.image.load("Art/HB16_120.png"), (30, 30))
        self.HB16_125 = pygame.transform.scale(pygame.image.load("Art/HB16_125.png"), (30, 30))
        self.HB16_130 = pygame.transform.scale(pygame.image.load("Art/HB16_130.png"), (30, 30))
        self.HB16_135 = pygame.transform.scale(pygame.image.load("Art/HB16_135.png"), (30, 30))
        self.HB16_140 = pygame.transform.scale(pygame.image.load("Art/HB16_140.png"), (30, 30))
        self.HB16_145 = pygame.transform.scale(pygame.image.load("Art/HB16_145.png"), (30, 30))
        self.HB16_150 = pygame.transform.scale(pygame.image.load("Art/HB16_150.png"), (30, 30))
        self.HB16_155 = pygame.transform.scale(pygame.image.load("Art/HB16_155.png"), (30, 30))
        self.HB16_160 = pygame.transform.scale(pygame.image.load("Art/HB16_160.png"), (30, 30))
        self.HB16_165 = pygame.transform.scale(pygame.image.load("Art/HB16_165.png"), (30, 30))
        self.HB16_170 = pygame.transform.scale(pygame.image.load("Art/HB16_170.png"), (30, 30))
        self.HB16_175 = pygame.transform.scale(pygame.image.load("Art/HB16_175.png"), (30, 30))
        self.HB16_180 = pygame.transform.scale(pygame.image.load("Art/HB16_180.png"), (30, 30))
        self.HB16_185 = pygame.transform.scale(pygame.image.load("Art/HB16_185.png"), (30, 30))
        self.HB16_190 = pygame.transform.scale(pygame.image.load("Art/HB16_190.png"), (30, 30))
        self.HB16_195 = pygame.transform.scale(pygame.image.load("Art/HB16_195.png"), (30, 30))
        self.HB16_200 = pygame.transform.scale(pygame.image.load("Art/HB16_200.png"), (30, 30))
        self.HB16_205 = pygame.transform.scale(pygame.image.load("Art/HB16_205.png"), (30, 30))
        self.HB16_210 = pygame.transform.scale(pygame.image.load("Art/HB16_210.png"), (30, 30))
        self.HB16_215 = pygame.transform.scale(pygame.image.load("Art/HB16_215.png"), (30, 30))
        self.HB16_220 = pygame.transform.scale(pygame.image.load("Art/HB16_220.png"), (30, 30))
        self.HB16_225 = pygame.transform.scale(pygame.image.load("Art/HB16_225.png"), (30, 30))
        self.HB16_230 = pygame.transform.scale(pygame.image.load("Art/HB16_230.png"), (30, 30))
        self.HB16_235 = pygame.transform.scale(pygame.image.load("Art/HB16_235.png"), (30, 30))
        self.HB16_240 = pygame.transform.scale(pygame.image.load("Art/HB16_240.png"), (30, 30))
        self.HB16_245 = pygame.transform.scale(pygame.image.load("Art/HB16_245.png"), (30, 30))
        self.HB16_250 = pygame.transform.scale(pygame.image.load("Art/HB16_250.png"), (30, 30))
        self.HB16_255 = pygame.transform.scale(pygame.image.load("Art/HB16_255.png"), (30, 30))
        self.HB16_260 = pygame.transform.scale(pygame.image.load("Art/HB16_260.png"), (30, 30))
        self.HB16_265 = pygame.transform.scale(pygame.image.load("Art/HB16_265.png"), (30, 30))
        self.HB16_270 = pygame.transform.scale(pygame.image.load("Art/HB16_270.png"), (30, 30))
        self.HB16_275 = pygame.transform.scale(pygame.image.load("Art/HB16_275.png"), (30, 30))
        self.HB16_280 = pygame.transform.scale(pygame.image.load("Art/HB16_280.png"), (30, 30))
        self.HB16_285 = pygame.transform.scale(pygame.image.load("Art/HB16_285.png"), (30, 30))
        self.HB16_290 = pygame.transform.scale(pygame.image.load("Art/HB16_290.png"), (30, 30))
        self.HB16_295 = pygame.transform.scale(pygame.image.load("Art/HB16_295.png"), (30, 30))
        self.HB16_300 = pygame.transform.scale(pygame.image.load("Art/HB16_300.png"), (30, 30))
        self.HB16_305 = pygame.transform.scale(pygame.image.load("Art/HB16_305.png"), (30, 30))
        self.HB16_310 = pygame.transform.scale(pygame.image.load("Art/HB16_310.png"), (30, 30))
        self.HB16_315 = pygame.transform.scale(pygame.image.load("Art/HB16_315.png"), (30, 30))
        self.HB16_320 = pygame.transform.scale(pygame.image.load("Art/HB16_320.png"), (30, 30))
        self.HB16_325 = pygame.transform.scale(pygame.image.load("Art/HB16_325.png"), (30, 30))
        self.HB16_330 = pygame.transform.scale(pygame.image.load("Art/HB16_330.png"), (30, 30))
        self.HB16_335 = pygame.transform.scale(pygame.image.load("Art/HB16_335.png"), (30, 30))
        self.HB16_340 = pygame.transform.scale(pygame.image.load("Art/HB16_340.png"), (30, 30))
        self.HB16_345 = pygame.transform.scale(pygame.image.load("Art/HB16_345.png"), (30, 30))
        self.HB16_350 = pygame.transform.scale(pygame.image.load("Art/HB16_350.png"), (30, 30))
        self.HB16_355 = pygame.transform.scale(pygame.image.load("Art/HB16_355.png"), (30, 30))
        self.SEA      = pygame.image.load("Art/sea.png") #Image of the sea for the background        
        
        self.angle = start_angle  #Starting angle of the boat
        self.pos_x = start_x - 19.25 #Starting x coords of the center of the boat
        self.pos_y = start_y - 19.25 #Starting y coords of the center of the boat
        self.direction = [0, -1]
        self.speed = 1
        self.sail_trim = 5 #1 is in, 5 is out
        self.boat_img = self.HB16_0
        
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
            self.boat_img = self.HB16_0
        elif self.angle == 5:
            self.boat_img =self.HB16_5
        elif self.angle == 10:
            self.boat_img = self.HB16_10
        elif self.angle == 15:
            self.boat_img = self.HB16_15
        elif self.angle == 20:
            self.boat_img = self.HB16_20
        elif self.angle == 25:
            self.boat_img = self.HB16_25
        elif self.angle == 30:
            self.boat_img = self.HB16_30
        elif self.angle == 35:
            self.boat_img = self.HB16_35
        elif self.angle == 40:
            self.boat_img = self.HB16_40
        elif self.angle == 45:
            self.boat_img =  self.HB16_45
        elif self.angle == 50:
            self.boat_img =  self.HB16_50
        elif self.angle == 55:
            self.boat_img =  self.HB16_55
        elif self.angle == 60:
            self.boat_img =  self.HB16_60
        elif self.angle == 65:
            self.boat_img =  self.HB16_65
        elif self.angle == 70:
            self.boat_img =  self.HB16_70
        elif self.angle == 75:
            self.boat_img =  self.HB16_75
        elif self.angle == 80:
            self.boat_img =  self.HB16_80
        elif self.angle == 85:
            self.boat_img =  self.HB16_85
        elif self.angle == 90:
            self.boat_img =  self.HB16_90
        elif self.angle == 95:
            self.boat_img =  self.HB16_95
        elif self.angle == 100:
            self.boat_img =  self.HB16_100
        elif self.angle == 105:
            self.boat_img =  self.HB16_105
        elif self.angle == 110:
            self.boat_img =  self.HB16_110
        elif self.angle == 115:
            self.boat_img =  self.HB16_115
        elif self.angle == 120:
            self.boat_img =  self.HB16_120
        elif self.angle == 125:
            self.boat_img =  self.HB16_125
        elif self.angle == 130:
            self.boat_img =  self.HB16_130
        elif self.angle == 135:
            self.boat_img =  self.HB16_135
        elif self.angle == 140:
            self.boat_img =  self.HB16_140
        elif self.angle == 145:
            self.boat_img =  self.HB16_145
        elif self.angle == 150:
            self.boat_img =  self.HB16_150
        elif self.angle == 155:
            self.boat_img =  self.HB16_155
        elif self.angle == 160:
            self.boat_img =  self.HB16_160
        elif self.angle == 165:
            self.boat_img =  self.HB16_165
        elif self.angle == 170:
            self.boat_img =  self.HB16_170
        elif self.angle == 175:
            self.boat_img =  self.HB16_175
        elif self.angle == 180:
            self.boat_img =  self.HB16_180
        elif self.angle == 185:
            self.boat_img =  self.HB16_185
        elif self.angle == 190:
            self.boat_img =  self.HB16_190
        elif self.angle == 195:
            self.boat_img =  self.HB16_195
        elif self.angle == 200:
            self.boat_img =  self.HB16_200
        elif self.angle == 205:
            self.boat_img =  self.HB16_205
        elif self.angle == 210:
            self.boat_img =  self.HB16_210
        elif self.angle == 215:
            self.boat_img =  self.HB16_215
        elif self.angle == 220:
            self.boat_img =  self.HB16_220
        elif self.angle == 225:
            self.boat_img =  self.HB16_225
        elif self.angle == 230:
            self.boat_img =  self.HB16_230
        elif self.angle == 235:
            self.boat_img =  self.HB16_235
        elif self.angle == 240:
            self.boat_img =  self.HB16_240
        elif self.angle == 245:
            self.boat_img =  self.HB16_245
        elif self.angle == 250:
            self.boat_img =  self.HB16_250
        elif self.angle == 255:
            self.boat_img =  self.HB16_255
        elif self.angle == 260:
            self.boat_img =  self.HB16_260
        elif self.angle == 265:
            self.boat_img =  self.HB16_265
        elif self.angle == 270:
            self.boat_img =  self.HB16_270
        elif self.angle == 275:
            self.boat_img =  self.HB16_275
        elif self.angle == 280:
            self.boat_img =  self.HB16_280
        elif self.angle == 285:
            self.boat_img =  self.HB16_285
        elif self.angle == 290:
            self.boat_img =  self.HB16_290
        elif self.angle == 295:
            self.boat_img =  self.HB16_295
        elif self.angle == 300:
            self.boat_img =  self.HB16_300
        elif self.angle == 305:
            self.boat_img =  self.HB16_305
        elif self.angle == 310:
            self.boat_img =  self.HB16_310
        elif self.angle == 315:
            self.boat_img =  self.HB16_315
        elif self.angle == 320:
            self.boat_img =  self.HB16_320
        elif self.angle == 325:
            self.boat_img =  self.HB16_325
        elif self.angle == 330:
            self.boat_img =  self.HB16_330
        elif self.angle == 335:
            self.boat_img =  self.HB16_335
        elif self.angle == 340:
            self.boat_img =  self.HB16_340
        elif self.angle == 345:
            self.boat_img =  self.HB16_345
        elif self.angle == 350:
            self.boat_img =  self.HB16_350
        elif self.angle == 355:
            self.boat_img =  self.HB16_355
    def sail_in(self):
        if self.sail_trim > 1:
            self.sail_trim -= 1
    
    def sail_out(self):
        if self.sail_trim < 5:
            self.sail_trim += 1
        
class Wind():        
    def __init__(self, wind_speed):
        self.wind_speed = wind_speed  #Multiples of 2 only !
    def get_allures(self, boat_angle, sail_trim):
        self.boat_angle = boat_angle
        self.sail_trim = sail_trim #I just put this here for convenience instead of having to get it in the get_speed method.
        if self.boat_angle > 320 or self.boat_angle < 40:
            self.allure = "vent de face"
        elif self.boat_angle > 40 and self.boat_angle < 80 or self.boat_angle > 280 and self.boat_angle < 320:
            self.allure = "pres"
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
                return 0.20
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
            elif self.sail_trim == 4:  #Best
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
            elif self.sail_trim == 5:  #Best
                return 2.9
          
class Buoys():
    def __init__(self):
        self.YELLOW = (255, 255, 0)
        self.RED    = (255, 0, 0)
        self.GREEN  = (0, 255, 0)
        self.possible_buoys_coords_x = range(RESOLUTION[0] / 6                                 , RESOLUTION[0] - 100)
        self.possible_buoys_coords_y = range(RESOLUTION[1] / 6                                 , RESOLUTION[1] - 60)
        self.BUOYS = [(
            random.choice(self.possible_buoys_coords_x), random.choice(self.possible_buoys_coords_y))]
        self.slalom_buoys = [(RESOLUTION[0] / 10, RESOLUTION[1] / 2), (RESOLUTION[0] / 2, RESOLUTION[1] / 2), (RESOLUTION[0] - 120, RESOLUTION[1] / 2)]
        #self.triangle_buoys = [(RESOLUTION[0] / 6, RESOLUTION[1] - RESOLUTION[1] / 6) ]
        self.triangle_buoys = [(RESOLUTION[0] / 8, RESOLUTION[1] - RESOLUTION[1] / 8), (RESOLUTION[0] - RESOLUTION[0] / 6, RESOLUTION[1] - RESOLUTION[1] / 8), (RESOLUTION[0] - RESOLUTION[0] / 6, RESOLUTION[1] / 6)]
        
    def distance_between_points(self, point1, point2):
        """Point1 and point2 are tuples of the point's coords"""
        return math.sqrt((point2[0] - point1[0])** 2 + (point2[1] - point1[1])**2)
        
    def generate_buoy_coords(self):
        """Generates a buoy coord."""
        return (
            random.choice(self.possible_buoys_coords_x),     random.choice(self.possible_buoys_coords_y)
               )
    
    def make_buoys_list(self, preset="random"):
        """Append the buoys to the BUOYS list if they are not too close to one another or if preset true, used an already existing map."""
        if preset != "random":
            if preset == "slalom":
                self.BUOYS = self.slalom_buoys
            if preset == "triangle":
                self.BUOYS = self.triangle_buoys
            return

        while len(self.BUOYS) < 3:
            random_buoy = self.generate_buoy_coords()
            for i in self.BUOYS:
                if self.distance_between_points(i, random_buoy) > RESOLUTION[1] / 3.5:
                    self.BUOYS.append(random_buoy)

    def draw_buoys(self):
        for i in range(0, len(self.BUOYS)):
            pygame.draw.circle(screen, self.YELLOW, self.BUOYS[i], 5)

            secondary_buoy = (self.BUOYS[i][0] + 100, self.BUOYS[i][1])
            pygame.draw.circle(screen, self.RED, secondary_buoy, 5)
           
    def draw_checkpoints(self):
        i = 0
        while i < 3:
            if i == 0:  #First buoy
                self.first_checkpoint = pygame.draw.rect(screen, self.YELLOW, Rect((self.BUOYS[i][0] + 4, self.BUOYS[i][1], 93, 2)))
            if i == 1: #2nd buoy
                self.second_checkpoint = pygame.draw.rect(screen, self.GREEN, (self.BUOYS[i][0] + 4, self.BUOYS[i][1], 93, 2))
            if i == 2: #3rd buoy
                self.third_checkpoint = pygame.draw.rect(screen, self.RED, (self.BUOYS[i][0] + 4, self.BUOYS[i][1], 93, 2))
            i += 1   
    def all_pixels_in_checkpoint(self, checkpoint_rect):
        #This returns in a list all the coords of all the pixels in a checkpoint.
        pixels_list = []
        for x in range(checkpoint_rect.x - 20, checkpoint_rect.x + 115):
            for y in range(checkpoint_rect.y, checkpoint_rect.y + 1):
                pixels_list.append((x, y))
        return pixels_list   
   
            
class InGameText():
    def __init__(self):
        self.PURPLE = (128, 0, 128)
        self.WHITE  = (255, 255, 255)
        self.GREY            = (128, 128, 128)
        self.font8 = pygame.font.Font("freesansbold.ttf", 8)
        self.font16 = pygame.font.Font("freesansbold.ttf", 16)
        self.CORNER_OF_HUD = (RESOLUTION[0] - 350, RESOLUTION[1] - 30)
        
    def draw(self, sail_trim, laps, total_laps, checkpoint):
        pygame.draw.rect(screen, self.PURPLE, (self.CORNER_OF_HUD[0], self.CORNER_OF_HUD[1], 350, 30))
        text_surface = self.font16.render("Sail Trim:{0}/5    Checkpoint = {3}/3    Laps:{1}/{2}".format(sail_trim, laps, total_laps, checkpoint), True, self.WHITE)
        text_rect = (self.CORNER_OF_HUD[0] + 5, self.CORNER_OF_HUD[1] + 5)  #+'s are to center the text.
        screen.blit(text_surface, text_rect)
    
    def display_username(self, username, pos_x, pos_y):
        text_surface = self.font8.render(username, True, self.GREY)
        screen.blit(text_surface, (pos_x, pos_y))
    
class Network(self):
    """Create a socket when called, this handles all the networking and so serializing."""
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    def serialize(self, data):
        return pickle.dumps(data)
    
    def unserialize(self, data):
        return pickle.loads(data)
    
    def connect(self):
        self.socket.connect((self.host, self.port))
    
    def send(self, data):
        self.socket.sendall(data)
        
    def receive(self):
        self.socket.recv(4096)
    
    def close_socket(self):
        self.socket.close()

          
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
        self.GREENY          = (137, 212, 102)
        self.font = pygame.font.Font("freesansbold.ttf", 32)
        
        self.fps_clock = pygame.time.Clock()
        
        self.laps = 0
        self.checkpoint_counter = 0  #How many checkpoints have been passed.
        self.total_laps = 3  #Default is 3; amount of laps to be completed.
        self.level = "random"  #random course is default
        
        self.windspeed = 0.8  #Default is 0.8
        
        self.wins_coords = []  #Coords all the things to be blitted when the game is won.
        
    def cliMenu(self):
        """Command line based menu for PySail."""
        
        print "   --=PySail=--"
        print "Welcome to PySail, the arcade sailing game written in Python."
        while True:  #While username is not too short nor too big.
            self.username = raw_input("What do you want your username to be ?:")
            self.username = str(self.username)
            if len(self.username) < 1 or len(self.username) > 20:
                print "This is too short or too long (min:1, max:20) !"
            else:
                break
        print "\n These are the resolutions you can play at:"
        print "(1) 640x480"
        print "(2) 1024x720"
        print "(3) 1024x768"
        print "(4) 1280x768"
        print "(5) 1366x768"
        print "(6) 1920x1080"
        while True:  #While the input is incorrect.
            user_resolution = raw_input("Enter the number of the resolution you want:")
            if user_resolution in str(range(1,7)):  #One of the offered resolutions.
                if user_resolution == "1":
                    set_resolution(640, 480)
                elif user_resolution == "2":
                    set_resolution(1024, 720)
                elif user_resolution == "3":
                    set_resolution(1024, 768)
                elif user_resolution == "4":
                    set_resolution(1280, 768)
                elif user_resolution == "5":
                    set_resolution(1366, 768)
                elif user_resolution == "6":
                    set_resolution(1920, 1080)
                break  #Gathered the right input, get ouf of the loop.
            else:
                print "Incorrect input !!!"
                
        print "\n-=-LEVELS-=-"
        print "(1) Slalom"
        print "(2) Triangle"
        print "(3) Random"        
        while True:  #While the input is incorrect.
            user_level = raw_input("Which level do you want to play ?:")
            if user_level in str(range(1,4)):  #Check if input is one of the levels.
                if user_level == "1":
                    self.level = "slalom"
                elif user_level == "2":
                    self.level = "triangle"
                elif user_level == "3":
                    self.level == "random"
                break  #Gathered the right input, get ouf of the loop.
            else:
                "Incorrect input !!!"
        print "Great choice !\n"
        while True:            
            try:  
                user_wind = input("Choose the speed of the wind (recommended is in between 0.5 and 3, the higher your resolution, the higher it should be, default is 0.8):")
                self.windspeed = user_wind
                break
            except NameError:
                print "Oops, invalid input !!!"
            except EOFError:
                print "You didn't type in a something."
        
    def winningAnimation(self):
        """Draw random win str's all over the string when laps done."""
        text_surface = self.font.render("WON", True, self.GREENY)
        self.wins_coords.append((random.randint(0, RESOLUTION[0]), random.randint(0, RESOLUTION[1])))  #+'s are to center the text.
        for i in self.wins_coords:
            screen.blit(text_surface, i)            
    
        
    def run_singleplayer(self):
        self.cliMenu()
        HUD = InGameText()
        boat = Boat(0,320, 240)
        buoys = Buoys()
        buoys.make_buoys_list(preset=self.level)
        buoys.draw_checkpoints()
        wind = Wind(self.windspeed)
        
        while True:
            screen.blit(boat.SEA, (0, 0))  #Blits the background
            screen.blit(boat.boat_img, (boat.pos_x, boat.pos_y)) #Blit the boat image.
            boat.draw_boat()
            HUD.display_username(self.username, boat.pos_x, boat.pos_y + 30)  #+30 so the username is right below the boat.
            wind.get_allures(boat.angle, boat.sail_trim)
            boat.speed = wind.get_speed() * wind.wind_speed
            buoys.draw_buoys()
            buoys.draw_checkpoints()
            
            if boat.pos_x <= -30 or boat.pos_x > RESOLUTION[0] - 30 or boat.pos_y <= - 30 or boat.pos_y > RESOLUTION[1] - 30:  #If boat is getting out of the window.
                boat.turn_180()
            else:
                boat.forward()  #Always make the boat go forward, it's a sailboat, it ain't gonna stop.
            
            #Check if the point has passed the checkpoint, which one and updates the lap count.
            if self.checkpoint_counter == 0:  #no checkpoints passed.
                if (int(boat.pos_x) + 19, int(boat.pos_y) + 19) in buoys.all_pixels_in_checkpoint(buoys.first_checkpoint):
                    self.checkpoint_counter += 1
                    
                    
            elif self.checkpoint_counter == 1:
                if (int(boat.pos_x) + 19, int(boat.pos_y) + 19) in buoys.all_pixels_in_checkpoint(buoys.second_checkpoint):
                    self.checkpoint_counter += 1
                             
            elif self.checkpoint_counter == 2:
                if (int(boat.pos_x), int(boat.pos_y)) in buoys.all_pixels_in_checkpoint(buoys.third_checkpoint):
                    self.checkpoint_counter = 0
                    self.laps += 1
            
            if self.laps >= self.total_laps:  #All the laps have been completed.
                self.winningAnimation()
            
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
                        
            HUD.draw(boat.sail_trim, self.laps, self.total_laps, self.checkpoint_counter)
            pygame.display.update()
            self.fps_clock.tick(FPS)
            
    def run_multiplayer(self):
        network = Network("127.0.0.1", 2269)
        network.connect("127.0.0.1", 2269)
        #First let's get all the settings from the server
         
        


Game = Main()

if __name__ == "__main__":
    Game.run_multiplayer()


###TODO
#Finish the graphicalMenu

