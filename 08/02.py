import pylab as pl
k=1

class harmonic():
    def __init__(self, _alpha = 0, _x0 = 0, _v0 = 0, _dt = 0, _t = 0):
        self.alpha = _alpha
        self.x0 = _x0
        self.v0 = _v0
        self.dt= _dt
        self.time = _t
        
            
    def calculate(self):
        global k
        self.x=[]
        self.v=[]
        self.t=[]        
        self.x.append(self.x0)
        self.v.append(self.v0)
        self.t.append(0)
        n = int(self.time / self.dt)
        for i in range(1, n):
            self.v.append(self.v[i - 1] - k * self.x[i - 1] ** self.alpha * self.dt)
            self.x.append(self.x[i - 1] + self.v[i] * self.dt)
            self.t.append(self.t[i - 1] + self.dt)
        return 0
        
       
    def plot(self,color):
        pl.plot(self.t, self.x,color,label="$v0 = %d m/s, \\alpha = %d$" %(self.v0,self.alpha))
        pl.title("Harmonic motion")
        pl.xlabel("t / s")
        pl.ylabel("x / m")
        
        
a = harmonic(1, 0, 5, 0.1, 10)
a.calculate()
a.plot("red")
b = harmonic(1, 0, 10, 0.1, 10)
b.calculate()
b.plot("green")
c = harmonic(1, 0, 15, 0.1, 10)
c.calculate()
c.plot("blue")
d = harmonic(1, 0, 20, 0.1, 10)
d.calculate()
d.plot("yellow")
pl.legend()
pl.show()

#a_2 = harmonic(0.8, 0, 10, 0.1, 10)
#a_2.calculate()
#a_2.plot()
#show()

a_3 = harmonic(3, 0, 5, 0.01, 10)
a_3.calculate()
a_3.plot("red")
b_3 = harmonic(3, 0, 10, 0.01, 10)
b_3.calculate()
b_3.plot("green")
c_3 = harmonic(3, 0, 15, 0.01, 10)
c_3.calculate()
c_3.plot("blue")
d_3 = harmonic(3, 0, 20, 0.01, 10)
d_3.calculate()
d_3.plot("yellow")
pl.legend()
pl.show()
