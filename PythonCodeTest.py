from draw import box

class mage_tower:
    def __init__(self, x, y):
        self.d_min    = 8
        self.d_max    = 12
        self.cooldown = 40
        self.x        = x
        self.y        = y

        self.w        = 50
        self.h        = 80

    def draw(self):
        #pygame.draw.rect(screen,Lilac,[x,y,w,h],0)
        pass

class projectile:
    def __init__(self):
        self.coords = []
        self.start_pos = ()
        self.end_pos   = ()
        self.mid_point = ()

    def calc_positions(self,(x1,y1),(x2,y2)):


    def calc_porabola(self, x1, y1, x2, y2, x3, y3):

        if self.coords != []:
            pass
        else:
            self.coords = []
        
        self.start_pos = (x1,y1)
        self.end_pos   = (x2,y2)
        
        if y2 > y1:
            self.t_point = [int(x1+((x2-x1)/2)),int()]
        else:
            self.t_point = [int(x1+((x2-x1)/2)),int()]

        ((self.y1*(self.x−self.x2)*(self.x−self.x3))/((self.x1−self.x2)*(self.x1−self.x3)))
        +
        ((self.y2*(self.x−self.x1)*(self.x−self.x3))/((self.x2−self.x1)*(self.x2−self.x3)))
        +
        ((self.y3*(self.x−self.x1)*(self.x−self.x2))/((self.x3−self.x1)*(self.x3−self.x2)))
    
    def draw(self):
        pass
