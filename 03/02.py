from pylab import *
from math import *

g = 9.8
b2m = 4e-5

class flight_state:
	def __init__(self, _x = 0, _y = 0, _vx = 0, _vy = 0, _t = 0):
		self.x = _x
		self.y = _y
		self.vx = _vx
		self.vy = _vy
		self.t = _t
        
class cannon:
    def __init__(self, _fs = flight_state(0, 0, 0, 0, 0), _dt = 0.1):
        self.cannon_flight_state = []
        self.cannon_flight_state.append(_fs)
        self.dt = _dt
        #print self.cannon_flight_state[-1].x, self.cannon_flight_state[-1].y, self.cannon_flight_state[-1].vx, self.cannon_flight_state[-1].vy

    def next_state(self, current_state):
        global g
        next_x = current_state.x + current_state.vx * self.dt
        next_vx = current_state.vx
        next_y = current_state.y + current_state.vy * self.dt
        next_vy = current_state.vy - g * self.dt
        #print next_x, next_y
        return flight_state(next_x, next_y, next_vx, next_vy, current_state.t + self.dt)

    def shoot(self):
        while not(self.cannon_flight_state[-1].y < 0):
            self.cannon_flight_state.append(self.next_state(self.cannon_flight_state[-1]))
            #print self.cannon_flight_state[-1].x, self.cannon_flight_state[-1].y, self.cannon_flight_state[-1].vx, self.cannon_flight_state[-1].vy

        r = - self.cannon_flight_state[-2].y / self.cannon_flight_state[-1].y
        self.cannon_flight_state[-1].x = (self.cannon_flight_state[-2].x + r * self.cannon_flight_state[-1].x) / (r + 1)
        self.cannon_flight_state[-1].y = 0

    def show_trajectory(self):
        x = []
        y = []
        for fs in self.cannon_flight_state:
            x.append(fs.x)
            y.append(fs.y)
        
        plt.xlabel("x/m")
        plt.ylabel("y/m")
        plt.title("cannon_trajectory")
        plot(x,y,label="v=500m/s")
        #show()

class drag_cannon(cannon):
    def next_state(self, current_state):
        global g, b2m
        v = sqrt(current_state.x * current_state.x + current_state.y * current_state.y)
        next_x = current_state.x + current_state.vx * self.dt
        next_vx = current_state.vx - b2m * v * current_state.vx * self.dt
        next_y = current_state.y + current_state.vy * self.dt
        next_vy = current_state.vy - g * self.dt - b2m * v * current_state.vy * self.dt
        #print next_x, next_y
        return flight_state(next_x, next_y, next_vx, next_vy, current_state.t + self.dt)

class adiabatic_drag_cannon(cannon):
    def next_state(self, current_state):
        pass


a = cannon(flight_state(0, 0, 500 * cos(pi / 6), 500 * sin(pi / 6), 0), _dt = 0.1)
a.shoot()
a_d = drag_cannon(flight_state(0, 0, 500 * cos(pi / 6), 500 * sin(pi / 6), 0), _dt = 0.1)
a_d.shoot()

b = cannon(flight_state(0, 0, 500 * cos(pi / 4), 500 * sin(pi / 4) ,0), _dt = 0.1)
b.shoot()
b_d = drag_cannon(flight_state(0, 0, 500 * cos(pi / 4 ), 500 * sin(pi /4), 0), _dt = 0.1)
b_d.shoot()


c = cannon(flight_state(0, 0, 500 * cos(pi / 3), 500 * sin(pi / 3), 0), _dt = 0.1)
c.shoot()
c_d = drag_cannon(flight_state(0, 0, 500 * cos(pi / 3), 500 * sin(pi / 3), 0), _dt = 0.1)
c_d.shoot()

a.show_trajectory()
a_d.show_trajectory()
b.show_trajectory()
b_d.show_trajectory()
c.show_trajectory()
c_d.show_trajectory()

legend()
show()

