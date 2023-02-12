class Player:
    def __init__(self, x, y, y_accel):
        self.x = x
        self.y = y
        self.x_vel = 0
        self.x_accel = 0
        self.y_vel = 90
        self.y_accel = y_accel

    def player_move(self, delta_t, left, right):
        self.y_vel += self.y_accel*delta_t*30
        self.x_vel+=self.x_accel*delta_t*30
        if(not (left^right)):
            self.x_vel*=.95

        if self.x <= 30 and not right:
            self.x = 30
            self.x_vel *= -.5
        if left:
            self.x_vel -= 1

        if self.x >= 1480 and not left:
            self.x = 1480
            self.x_vel *= -.5
        if right:
            self.x_vel += 1

        self.x+=self.x_vel

        return self.y_vel
    def get_pos(self):
        return (self.x, self.y)
