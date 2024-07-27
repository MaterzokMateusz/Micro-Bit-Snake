# Imports go at the top
import random
import music
from microbit import *
from Joypad import *


class Fruit():
    position = []
    eaten = True
    
    def drawPosition(self,snakePositions):
        fruitX = random.randint(0,4)
        fruitY = random.randint(0,4)
        for x in snakePositions:
            if x[0] == fruitX and x[1] == fruitY:
                self.drawPosition(snakePositions)
            else:
                self.position = [fruitX,fruitY]
                self.eaten = False

    def drawFruit(self):
        for x in range(0,4):
            display.set_pixel(self.position[0],self.position[1],9)
            sleep(20)
            display.set_pixel(self.position[0],self.position[1],0)
            sleep(50)
            display.set_pixel(self.position[0],self.position[1],9)

    def clearFruit(self):
        display.set_pixel(self.position[0],self.position[1],0)

class Snake():
    segments = [[2,2,9]]
    numberOfSegments = 1
    segmentState = 0
    moved = False

    def drawSnake(self):
        for x in self.segments:
            display.set_pixel(x[0],x[1],x[2])
            self.moved = False

    def movingSound(self):
        if self.moved == True:
            music.pitch(170,100)
            
    def clearSnake(self):
        for x in self.segments:
            display.set_pixel(x[0],x[1],0)

    def eatFruit(self, fruit):
        if fruit.position[0] == self.segments[0][0] and fruit.position[1] == self.segments[0][1]:
            fruit.eaten = True
            self.segmentState += 1

    def changeHeadPosition(self,direction):
        if (direction == DIR['R']) and (self.segments[0][0] < 4) and (display.get_pixel(self.segments[0][0]+1,self.segments[0][1]) != 5):
            self.clearSnake()
            self.segments[0][0] += 1
            self.moved = True
        elif (direction == DIR['L']) and (self.segments[0][0] > 0) and (display.get_pixel(self.segments[0][0]-1,self.segments[0][1]) != 5):
            self.clearSnake()
            self.segments[0][0] -= 1
            self.moved = True
        elif direction == DIR['U'] and (self.segments[0][1] > 0) and (display.get_pixel(self.segments[0][0],self.segments[0][1]-1) != 5):
            self.clearSnake()
            self.segments[0][1] -= 1
            self.moved = True
        elif (direction == DIR['D']) and (self.segments[0][1] < 4) and (display.get_pixel(self.segments[0][0],self.segments[0][1]+1) != 5):
            self.clearSnake()
            self.segments[0][1] += 1
            self.moved = True
        else:
            pass

class Game():
    snake = Snake()
    joystick = JOYSTICK()
    fruit = Fruit()

    def respFruit(self):
        if self.fruit.eaten == True:
            self.fruit.drawPosition(self.snake.segments)
        else:
            pass

    def drawFruit(self):
        self.fruit.drawFruit()


game = Game()

# Code in a 'while True:' loop repeats forever
while True:
    direction = game.joystick.Listen_Dir()
    game.respFruit()
    game.drawFruit()
    game.snake.changeHeadPosition(direction)
    game.snake.movingSound()
    game.snake.drawSnake()
    game.snake.eatFruit(game.fruit)
    sleep(800)
