# Scale according to small window HALF

class Pong(object):
    def __init__(self, x, y, img, shadow):
        self.diameter = 40/2
        self.x = x
        self.y = y
        self.img = loadImage(img)
        self.shadow = loadImage(shadow)
        self.shadow_diameter = 160/2
        self.shadow_offset_x = -30/2
        self.shadow_offset_y = 0
        self.vel = PVector(1, 1)
    
    def draw(self, shadow = True):

        if shadow:
            image(self.shadow, self.x+self.diameter/2-self.shadow_diameter/2+self.shadow_offset_x,
                  self.y+self.diameter/2-self.shadow_diameter/2+self.shadow_offset_y,
                  self.shadow.width/2, self.shadow.height/2)

        image(self.img, self.x, self.y, self.img.width/2, self.img.height/2)
