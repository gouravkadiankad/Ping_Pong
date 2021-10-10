

class Ping(object):
    def __init__(self, x, y, img, shadow):
        self.x = x #65/2
        self.y = y
        self.w = 30/2
        self.h = 140/2
        self.img = loadImage(img)
        self.shadow = loadImage(shadow)
        self.shadow_w = 150/2
        self.shadow_h = 260/2
        self.shadow_offset_x = -30/2
        self.shadow_offset_y = 0
    
    def draw(self, shadow = True):

        if shadow:
            image(self.shadow, self.x+self.w/2-self.shadow_w/2+self.shadow_offset_x,
                  self.y+self.h/2-self.shadow_h/2+self.shadow_offset_y,
                  self.shadow.width/2, self.shadow.height/2)

        image(self.img, self.x, self.y, self.img.width/2, self.img.height/2)
