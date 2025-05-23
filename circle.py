import random

class Ball:
    def __init__(self,x,y,vx,vy,radius,color):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.radius = radius
        self.color = color

    def update_position(self, dt, w, h, min_vel, max_vel):
        new_x = self.x + self.vx*dt
        new_y = self.y + self.vy*dt

        # Check for collision with vertical walls
        if new_x + self.radius > w:
            self.vx = -random.randint(1, max_vel) # New random speed, moving left
            self.vy = random.randint(min_vel, max_vel) # New random vertical speed
            self.x = w - self.radius # Adjust position to be at the edge
        elif new_x - self.radius < 0:
            self.vx = random.randint(1, max_vel) # New random speed, moving right
            self.vy = random.randint(min_vel, max_vel) # New random vertical speed
            self.x = self.radius # Adjust position to be at the edge
        else:
            self.x = new_x

        # Check for collision with horizontal walls
        if new_y + self.radius > h:
            self.vy = -random.randint(1, max_vel) # New random speed, moving up
            self.vx = random.randint(min_vel, max_vel) # New random horizontal speed
            self.y = h - self.radius # Adjust position to be at the edge
        elif new_y - self.radius < 0:
            self.vy = random.randint(1, max_vel) # New random speed, moving down
            self.vx = random.randint(min_vel, max_vel) # New random horizontal speed
            self.y = self.radius # Adjust position to be at the edge
        else:
            self.y = new_y
