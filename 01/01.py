from pylab import *
import pickle

v = [] 
t = []
dt = 0
n = 0

def initialize(v, t, _dt, _n):
    global dt, n
    print "initial velocity -> ",
    v.append(float(raw_input()))
    print "time step -> ",
    dt = float(raw_input())
    print "total time -> ",
    time = float(raw_input())
    t.append(0)
    n = int(time / dt)
    return 0

def calculate(v, t, dt, n):
    print v
    print t
    print dt
    print n
    for i in range(1, n):
        v.append(v[i - 1] - 9.8 * dt)
        t.append(t[i - 1] + dt)
    return 0

def store(v, t, n):
    gfile = open("01.txt", "a")
    gfile.truncate()
    for i in range(n):
        print >> gfile, t[i], v[i]
    gfile.close()

    pickle_file = open("pickled_data.pkl", "w")
    pickle.dump(t, pickle_file)
    pickle.dump(v, pickle_file)

    return 0

def read():
    pickle_file = open("pickled_data.pkl", "r")
    t = pickle.load(pickle_file)
    v = pickle.load(pickle_file)
    print t
    print v

initialize(v, t, dt, n)
calculate(v, t, dt, n)
store(v, t, n)

plot(t, v, "-.b")
plt.title("01_v-t")
plt.xlabel("t/s")
plt.ylabel("v/m/s")
show()

read()

