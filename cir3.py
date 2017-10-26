import arcade
from random import randint
class Circle:
    def __init__(self,x,y,vx,vy):
        self.x = x
        self.y = y
        self.vy = vy
        self.vx = vx
    def move(self):
        self.x+=self.vx
        self.y+= self.vy
        if(abs(SCREEN_HEIGHT-self.y)<=20 or abs(SCREEN_HEIGHT-self.y)>=580):
            self.vy*=-1
        if(abs(SCREEN_WIDTH-self.x)<=20 or abs(SCREEN_WIDTH-self.x)>=580):
            self.vx*=-1
    def draw(self):
        arcade.draw_circle_outline(self.x,self.y,20,arcade.color.BLACK)

circles=[]
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 600
n = 10
def initialize():
    for i in range(n):
        circle = Circle(randint(100,SCREEN_WIDTH-100),randint(100,SCREEN_HEIGHT-100),randint(-5,5),randint(-5,5))
        circles.append(circle)
def on_draw(delta_time):
    arcade.start_render()
    for c in circles:
        c.move()
        c.draw()
def main():
    initialize()
    arcade.open_window(SCREEN_HEIGHT,SCREEN_WIDTH,"KUY")
    arcade.set_background_color(arcade.color.WHITE)
    arcade.schedule(on_draw,1/80)
    arcade.run()
if __name__=='__main__':
    main()