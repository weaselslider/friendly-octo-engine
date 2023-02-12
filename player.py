class Player:
    def __init__(self,x,y,y_accel):
        self.x = x/2
        self.y = y-30
        self.x_vel = 0
        self.y_vel = 90
        self.y_accel = y_accel

    def player_move(self, delta_t):
        self.y_vel += y_
