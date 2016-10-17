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
        v0x=self.vel*math.cos(self.ang[0])
        v0y=self.vel*math.sin(self.ang[0])
        vx=[v0x]
        vy=[v0y]
        v=[self.vel]
        Bchum=4*10**(-5)
        g=9.8
        valuex=0
        valuey=0        
        velx=0
        vely=0
        vel=0
        a=6.5*10**(-3)
        T0=20+273.15
        alpha=2.5
        while self.y[-1]>=0:
            i=0
            valuex=self.x[i]+vx[i]*self.dt
            velx=vx[i]-(1-a*self.y[i]/T0)**alpha*Bchum*v[i]*vx[i]*self.dt
            valuey=self.y[i]+vy[i]*self.dt
            vely=vy[i]-g*self.dt-(1-a*self.y[i]/T0)**alpha*Bchum*v[i]*vy[i]*self.dt
            self.x.append(valuex)
            self.y.append(valuey)
            vx.append(velx)
            vy.append(vely)
            vel=math.sqrt(velx**2+vely**2)
            v.append(vel)
            self.time.append(self.time[i]+self.dt)
            i=i+1
        yplus=self.y[i]+vy[i]*self.dt
        r=-self.y[i]/yplus
        yend=(self.y[i]+yplus*r)/(r+1)
        return yend
    def show(self):
        pl.plot(self.x,self.y,'r')
        pl.title("The trajectory of the cannon shell")
        pl.xlabel("x")
        pl.ylabel("y")
yvalue=[0]
yendvalue=0
for j in range(89):
    cann=cannon(700,(1+j)/180*math.pi,1000)
    yendvalue=cann.caculate()
    yvalue.append(yendvalue)
ymax=max(yvalue)
print ("最大的射程为",str(ymax))
location=yvalue.index(ymax)
print ("最佳的发射角为",str(location))
cannonbest=cannon(700,location/180*math.pi,1000)
cannonbest.show()
