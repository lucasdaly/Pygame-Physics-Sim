class Dropper:

    def __init__(self, x, y, tick, tick_interval):
        self.x = x
        self.y = y
        self.tick = tick
        self.tick_interval = tick_interval

    def update(self):
        self.tick