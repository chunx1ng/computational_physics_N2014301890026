import pylab as pl
import math
class cannon:
    def __init__(self,init_velocity,init_angle,footstep,init_x=0,init_y=0):
        self.x=[init_x]
        self.y=[init_y]
        self.ang=[init_angle]
        self.vel=init_velocity
        self.dt=footstep
        self.time=[0]
    def caculate(self):
        vox=self.vel*math.cos(self.ang[0])
        voy=self.vel*math.sin(self.ang[0])
        vx=[vox]
        vy=[voy]
        v=[self.vel]
        Bchum=4*10**(-5)
        g=9.8
        valuex=0
        valuey=0        
        velx=0
        vely=0
        vel=0
        a=6.5*10**(-3)
        To=20+273.15
        alpha=2.5
        for i in range(1000):
            if self.y[i]>=0:            
                valuex=self.x[i]+vx[i]*self.dt
                velx=vx[i]-(1-a*self.y[i]/To)**alpha*Bchum*v[i]*vx[i]*self.dt
                valuey=self.y[i]+vy[i]*self.dt
                vely=vy[i]-g*self.dt-(1-a*self.y[i]/To)**alpha*Bchum*v[i]*vy[i]*self.dt
                self.x.append(valuex)
                self.y.append(valuey)
                vx.append(velx)
                vy.append(vely)
                vel=math.sqrt(velx**2+vely**2)
                v.append(vel)
                self.time.append(self.time[i]+self.dt)
            else:
                break
    def show(self):
        pl.plot(self.x,self.y,'r')
        pl.title("The trajectory of the cannon shell")
        pl.xlabel("x")
        pl.ylabel("y")
xvalue=[0]
xendvalue=0
for j in range(89):
    cann=cannon(700,math.radians(1+j),0.1)
    cann.caculate()
    r=-cann.y[-2]/cann.y[-1]
    xendvalue=(cann.x[-2]+r*cann.x[-1])/(r+1)
    xvalue.append(xendvalue)
xmax=max(xvalue)
print "最大的射程为",xmax
location=xvalue.index(xmax)
print "最佳的发射角为",location
cannonbest=cannon(700,math.radians(location),0.1)
cannonbest.caculate()
cannonbest.show()
