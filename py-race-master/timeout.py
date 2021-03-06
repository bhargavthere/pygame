#The MIT License (MIT)

#Copyright (c) 2012 Robin Duda, (chilimannen)

#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in
#all copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#THE SOFTWARE.

#Camera module will keep track of sprite offset.

#Show a dialog when time is out.
from loader import load_image
import pygame
from pygame.locals import *


NOTE_HALF_X = 212
NOTE_HALF_Y = 112

#Alert body.
class Alert(pygame.sprite.Sprite):
    curr_id = 1
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image('slide1.png')
        self.rect = self.image.get_rect()
        #self.x =  int(pygame.display.Info().current_w /2) - NOTE_HALF_X
        #self.y =  int(pygame.display.Info().current_h /2) - NOTE_HALF_Y
        self.x = 100
        self.y = 100
        self.rect.topleft = self.x, self.y


#Update the timer and reposition the flag by offset.
    def update(self):
        if(type(self).curr_id >= 120):
          filename = "slide12.png" 
        elif(type(self).curr_id >= 10):
          filename = "slide"+str(type(self).curr_id//10)+".png"
        else:
          filename = "slide1.png"
        self.image = load_image(filename)
        type(self).curr_id = type(self).curr_id + 1
        if(type(self).curr_id == 150):
            type(self).curr_id = 1
        
        
    
