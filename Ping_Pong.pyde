import ping
import pong

width_ = 1366/2
height_ = 768/2

up = 0
down = 0
pongspeed = 6
pingspeed = 8
pong1 = None
ping1 = None
back = None




def boundary_handling(pong):
    if pong.x+pong.diameter >= width or pong.x <= 0:
        pong.vel.x *= -1
    if pong.y+pong.diameter >= height or pong.y <= 0:
        pong.vel.y *= -1

def collision_handling(ping, pong):
    if pong.y+pong.diameter >= ping.y and pong.y+pong.diameter <= ping.y+ping.h and pong.x > ping.x+ping.w-4 and pong.x < ping.x+ping.w+4:
        pong.vel.x *= -1


def setup():
    global pong1, ping1, back
    size(width_, height_)
    frameRate(30)
    pong1 = pong.Pong(width_/2, height_/2, "Assets\Ball1.png", "Assets\Ball1_shadow.png")
    ping1 = ping.Ping(65/2, 50, "Assets\Ping1.png", "Assets\Ping_shadow.png")
    back = loadImage("Assets\Background1.png")

    
def draw():
    background(0)
    boundary_handling(pong1)
    collision_handling(ping1, pong1)
    pong1.x += pong1.vel.x * pongspeed
    pong1.y += pong1.vel.y * pongspeed
    ping1.y += (down - up) * pingspeed
    image(back, 0 ,0, back.width/2, back.height/2)
    ping1.draw()
    pong1.draw()

def keyPressed():
    global up, down
    if key == CODED:
        if keyCode == UP:
            up = 1
        if keyCode == DOWN:
            down = 1

def keyReleased():
    global up, down
    if key == CODED:
        if keyCode == UP:
            up = 0
        if keyCode == DOWN:
            down = 0
