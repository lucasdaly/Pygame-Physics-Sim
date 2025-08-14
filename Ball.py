class Ball:

    def __init__(self, x, y, xv, yv, radius, color):
        self.x = x
        self.y = y
        self.xv = xv
        self.yv = yv
        self.radius = radius
        self.color = color

    def update(self):
        self.x += self.xv
        self.y += self.yv

    def get_x(self):
        return self.x

    def set_x(self, x):
        self.x = x

    def get_y(self):
        return self.y

    def set_y(self, y):
        self.y = y

    def get_xv(self):
        return self.xv

    def set_xv(self, xv):
        self.xv = xv

    def get_yv(self):
        return self.yv

    def set_yv(self, yv):
        self.yv = yv

    def get_radius(self):
        return self.radius

    def set_radius(self, radius):
        self.radius = radius

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color