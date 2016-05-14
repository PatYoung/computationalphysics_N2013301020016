from pylab import *
import math

v = []
v_x = []
v_y = []
x = []
y = []
t = []
dt = 0
n = 0

def initialize(v_x, v_y, x, y, t, _dt, _n):
	global dt, n
	print "v_x ->"
	v_x.append(float(raw_input()))
	print "v_y ->"
	v_y.append(float(raw_input()))
	print "time step ->"
	dt = float(raw_input())
	print "total time ->"
	time = float(raw_input())
	t.append(0)
	n = int(time / dt )
	x.append(0)
	y.append(0)
	return 0

def calculate(v_x, v_y, x, y, t, dt, n):
	for i in range(1, n):
		v = sqrt(v_x[i-1] * v_x[i-1] + v_y[i-1] * v_y[i-1])
		x.append(x[i-1] + v_x[i-1] * dt)
		v_x.append(v_x[i-1] - 4 * 10 ** (- 5) * v * v_x[i-1] * dt)
		y.append(y[i-1] + v_y[i-1] * dt)
		v_y.append(v_y[i-1] - 9.8 * dt - 4 * 10 ** (- 5) * v * v_y[i-1] * dt)
		t.append(t[i-1] + dt)
	return 0
initialize (v_x, v_y, x, y, t, dt, n)
calculate (v_x,v_y, x, y, t, dt ,n)

plot(x, y, "-.b")
show()
