import math
import pylab as pl
from visual import *


g=9.8
S0m=0.00041
omega=209
a=0.0039
b=0.0058
c=1
vd=35
deltav=5
class flight_state:
    def __init__(self, _x = 0, _y = 0,_z = 0, _vx = 0, _vy = 0,_vz = 0, _t = 0):
        self.x = _x
        self.y = _y
        self.z = _z
        self.vx = _vx
        self.vy = _vy
        self.vz = _vz
        self.t = _t
class baseball:
    def __init__(self, _fs = flight_state(0, 0, 0, 0, 0, 0, 0), _dt = 0.01):
        self.baseball_flight_state = []
        self.baseball_flight_state.append(_fs)
        self.dt = _dt
        print self.baseball_flight_state[-1].x, self.baseball_flight_state[-1].y,self.baseball_flight_state[-1].z,self.baseball_flight_state[-1].vx, self.baseball_flight_state[-1].vy,self.baseball_flight_state[-1].vz
    def next_state(self, current_state):
        g=9.8
        S0m=0.00041
        a=0.0039
        b=0.0058
        c=1
        vd=35
        deltav=5
        v=math.sqrt(current_state.x**2+current_state.vy**2+current_state.vz**2)
        B2m=a+b/(c+math.exp((v-vd)/deltav))
        next_x = current_state.x + current_state.vx * self.dt
        next_vx = current_state.vx-B2m*v*current_state.vx*self.dt
        next_y = current_state.y + current_state.vy * self.dt
        next_vy = current_state.vy - g * self.dt-S0m*current_state.vx*omega*self.dt
        next_z = current_state.z + current_state.vz * self.dt
        next_vz = current_state.vz-S0m*current_state.vx*omega*self.dt
        #print next_x, next_y
        return flight_state(next_x, next_y,next_z, next_vx, next_vy,next_vz, current_state.t + self.dt)
    def shoot(self):
        while not(self.baseball_flight_state[-1].y < 0):
            self.baseball_flight_state.append(self.next_state(self.baseball_flight_state[-1]))
            #print self.baseball_flight_state[-1].x, self.baseball_flight_state[-1].y,self.baseball_flight_state[-1].z, self.baseball_flight_state[-1].vx, self.baseball_flight_state[-1].vy,self.baseball_flight_state[-1].vz

        r = - self.baseball_flight_state[-2].y / self.baseball_flight_state[-1].y
        self.baseball_flight_state[-1].x = (self.baseball_flight_state[-2].x + r * self.baseball_flight_state[-1].x) / (r + 1)
    def show_trajectory(self,color):
        x = []
        y = []
        z=  []
        for fs in self.baseball_flight_state:
            x.append(fs.x)
            y.append(fs.y)
            z.append(fs.z)
        pl.plot(x,y,color,label="$vx=%dm/s$,$vy=%dm/s$,$\omega=2000$"%(self.baseball_flight_state[0].vx,self.baseball_flight_state[0].vy))
           
        
a = baseball(flight_state(0,0,0,100 * cos(pi/10),100 * sin(pi/10),0,0), _dt = 0.01)
a.shoot()
a.show_trajectory("red")
b = baseball(flight_state(0,0,0,100 * cos(pi/9),100 * sin(pi/9),0,0), _dt = 0.01)
b.shoot()
b.show_trajectory("blue")
c = baseball(flight_state(0,0,0,100 * cos(pi/8),100 * sin(pi/8),0,0), _dt = 0.01)
c.shoot()
c.show_trajectory("yellow")
d = baseball(flight_state(0,0,0,100 * cos(pi/7),100 * sin(pi/7),0,0), _dt = 0.01)
d.shoot()
d.show_trajectory("cyan")
e = baseball(flight_state(0,0,0,100 * cos(pi/6),100 * sin(pi/6),0,0), _dt = 0.01)
e.shoot()
e.show_trajectory("orange")
f = baseball(flight_state(0,0,0,100 * cos(pi/5),100 * sin(pi/5),0,0), _dt = 0.01)
f.shoot()
f.show_trajectory("pink")
g = baseball(flight_state(0,0,0,100 * cos(pi/4),100 * sin(pi/4),0,0), _dt = 0.01)
g.shoot()
g.show_trajectory("green")
h = baseball(flight_state(0,0,0,100 * cos(pi/3),100 * sin(pi/3),0,0), _dt = 0.01)
h.shoot()
h.show_trajectory("violet")
#pl.legend()
pl.show()

    

