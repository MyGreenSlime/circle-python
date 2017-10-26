import arcade
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
x = 300
y =300
vx = 2
vy = 1
def on_draw(delta_time):
    global x,y,vx,vy
    x+=vx
    y+=vy
    if(abs(SCREEN_HEIGHT-y)<=20 or abs(SCREEN_HEIGHT-y)>=580):
        vy*=-1
    if(abs(SCREEN_WIDTH-x)<=20 or abs(SCREEN_WIDTH-x)>=580):
        vx*=-1
    arcade.start_render()
    arcade.draw_circle_outline(x,y,20,arcade.color.BLACK)
def main():
    arcade.open_window(SCREEN_WIDTH,SCREEN_HEIGHT,"KUY")
    arcade.set_background_color(arcade.color.WHITE)
    arcade.schedule(on_draw,1/80)
    arcade.run()
if __name__=='__main__':
    main()