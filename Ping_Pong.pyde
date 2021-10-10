import ping
import pong

width_ = 1366/2
height_ = 768/2

up = 0
down = 0
speed = 8
pong1 = None
ping1 = None
back = None


def setup():
    global pong1, ping1, back
    size(width_, height_)
    frameRate(30)
    pong1 = pong.Pong(width_/2, height_/2, "Assets\Ball1.png", "Assets\Ball1_shadow.png")
    ping1 = ping.Ping(65/2, 50, "Assets\Ping1.png", "Assets\Ping_shadow.png")
    back = loadImage("Assets\Background1.png")

    
def draw():
    background(0)
    pong1.x += pong1.vel.x
    pong1.y += pong1.vel.y
    ping1.y += (down - up) * speed
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

def boundary_handling():
    pass
