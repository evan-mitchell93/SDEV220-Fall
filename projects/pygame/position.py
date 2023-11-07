class Position:
    def __init__(self,x,y):
        self.pos_x = x
        self.pos_y = y
    
    @property
    def pos_x(self):
        print("Getting x position")
        return self._x 
    
    @pos_x.setter
    def pos_x(self,value):
        print("Updating x value")
        self._x = value

    @property
    def pos_y(self):
        print("Getting y position")
        return self._y 
    
    @pos_y.setter
    def pos_y(self,value):
        print("Updating y value")
        self._y = value
