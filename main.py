from turtle import Shape, Screen, Turtle, Vec2D as Vec
from datetime import datetime

# User input
G = 8
NUM_LOOPS = 4100
Ro_X = 0
Ro_Y = -85
Vo_X = 485
Vo_Y = 0

class Truck(Turtle):
    """Truck that delivers concrete"""
    def __init__(self, id, start_loc, vel, shape):
        super().__init__(shape=shape)
        self.penup()
        self.id = id
        self.setpos(start_loc)
        self.vel = vel
        # self.resizemode("user")
        # self.pendown() # Uncomment to draw the path behind the object.
        
# class GravSys():
#     "Runs a gravity simulation on n-bodies"
#     def __init__(self):
#         self.bodies = []
#         self.t = 0
#         self.dt = 0.001
        
#     def sim_loop(self):
#         "Loop trucks in a list through time steps"
#         for _ in range(NUM_LOOPS):
#             self.t += self.dt
#             for truck in self.trucks:
#                 truck.step()

class TimeSys():
    """Runs a time system for start to finish of cycle"""
    def __init__(self, start_time, end_time):
        self.start_time = start_time
        self.end_time = end_time
        self.duration = end_time - start_time
        
        
        
def main():
    screen = Screen()
    screen.setup(width=800, height=900, startx=100, starty=0) # For full screen
    screen.bgcolor('white')
    screen.title("Concrete Truck Delivery Cycle")
    
    image_truck = 'concrete_truck.gif'
    screen.register_shape(image_truck)
    truck = Truck(1, (0, -25), Vec(0, -2.5), image_truck)
    truck.pencolor('black')
    truck.getscreen().tracer(n=0, delay=0)
    
if __name__ == '__main__':
    main()
    
    