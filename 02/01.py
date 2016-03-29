import pylab as pl
import pickle
import visual as vs
import easygui


class Uranium:
    def __init__(self, v = 40, dt = 0.1, time = 3.0):
        self.dt = dt
        self.v = v
        self.time = time

    def calculate(self):
        self.x = []
        self.T = []
        self.x.append(0)
        self.T.append(0)
        nsteps = int(self.time / self.dt)
        for i in range(1, nsteps):
            self.x.append(self.x[i - 1] + self.v * self.dt)
            self.T.append(self.T[i - 1] + self.dt)
        return 0

    def plot2D(self):
        pl.plot(self.T, self.x, '-*')
        pl.title("Moving horizontally with a constant velocity")
        pl.xlabel("Time/s")
        pl.ylabel("Displacement/m")
        pl.show()

    def plot3D(self):
		axis_length = 10.0
		xaxis = vs.arrow(pos = (-5, -5, 0), axis = (axis_length, 0, 0), shaftwidth = 0.01)
		yaxis = vs.arrow(pos = (-5, -5, 0), axis = (0, axis_length, 0), shaftwidth = 0.01)
		balls = []
		for (i, j) in zip(self.x, self.T):
			balls.append(vs.sphere(pos = ((j / self.time) * axis_length * 0.9- 4.9, (i / self.v) * axis_length * 0.9 - 4.9, 0), radius = 0.2, color = vs.color.red))
		xlabel = vs.label(text = "Time/s", pos = (5, -5, 0))
		ylabel = vs.label(text = "Displacement/m", pos = (-5, 5, 0))
    
    def set_parameters(self):
        self.N = float(easygui.enterbox("How much is the initial velocity?"))
        self.dt = float(easygui.enterbox("How much is the timestep?"))
        self.time = float(easygui.enterbox("How much time will go thorgh?"))

A = Uranium(40, 0.1, 3.0)

A.set_parameters()

A.calculate()
A.plot2D()
#A.plot3D()
