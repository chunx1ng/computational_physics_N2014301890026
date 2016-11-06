#version1


import pylab as pl
import math
class pendulum:
    def __init__(self,forc=1.2,init_angle=0.2,footstep=0.04,init_w=0.):
        self.ang=[init_angle]
        self.w=[init_w]
        self.dt=footstep
        self.f=forc
        self.time=[0]
    def caculate(self):
        g=9.8
        l=9.8
        q=0.5
        time=0
        omigaD=0.66666
        for i in range(2000):
            angspeed=self.w[i]-(g/l*math.sin(self.ang[i])+q*self.w[i]-self.f\
            *math.sin(omigaD*self.time[i]))*self.dt
            ang=self.ang[i]+angspeed*self.dt
            if ang>math.pi:
                ang-=2*math.pi
            if ang<-math.pi:
                ang+=2*math.pi
            time=time+self.dt
            self.w.append(angspeed)
            self.ang.append(ang)
            self.time.append(time)       
    def show(self):
        pl.plot(self.time,self.ang)
        pl.title("The angle of the pendulums changes with time")
        pl.xlabel("time")
        pl.ylabel("angle")
        pl.axis('equal')
        pl.show()
p=pendulum()
p.caculate()
p.show()



#version2


import pylab as pl
import math
class pendulum:
    def __init__(self,forc=1.2,init_angle1=0.2,init_angle2=0.2,footstep=0.04,init_w1=0,init_w2=0,omigaD=0.66666,l=9.8,g=9.8,q1=0.5,q2=0.4999):
        self.ang1=[init_angle1]
        self.ang2=[init_angle2]
        self.w1=[init_w1]
        self.pi=math.pi        
        self.w2=[init_w2]
        self.dangle=[math.fabs(init_angle1-init_angle2)]
        self.dt=footstep
        self.f=forc
        self.time=[0]
        self.D=omigaD
        self.lg=g/l
        self.q1=q1
        self.q2=q2
    def caculate(self):
        time=0        
        while(self.time[-1]<=200):
            self.w1.append(self.w1[-1]-(self.lg*math.sin(self.ang1[-1])+self.q1*self.w1[-1]-self.f*math.sin(self.D*self.time[-1]))*self.dt)
            angspeed1=self.w1[-1]-(self.lg*math.sin(self.ang1[-1])+self.q1*self.w1[-1]-self.f*math.sin(self.D*self.time[-1]))*self.dt
            self.ang1.append(self.ang1[-1]+angspeed1*self.dt)
            self.w2.append(self.w2[-1]-(self.lg*math.sin(self.ang2[-1])+self.q2*self.w2[-1]-self.f*math.sin(self.D*self.time[-1]))*self.dt)            
            angspeed2=self.w2[-1]-(self.lg*math.sin(self.ang2[-1])+self.q2*self.w2[-1]-self.f*math.sin(self.D*self.time[-1]))*self.dt
            self.ang2.append((self.ang2[-1]+angspeed2*self.dt))
            self.dangle.append(math.log(math.fabs(self.ang1[-1]-self.ang2[-1])))
            if self.ang1[-1]>math.pi:
                self.ang1[-1]-=self.pi+math.pi
            if self.ang1[-1]<-math.pi:
                self.ang1[-1]+=self.pi+math.pi
            if self.ang2[-1]>math.pi:
                self.ang2[-1]-=self.pi+math.pi
            if self.ang2[-1]<-math.pi:
                self.ang2[-1]+=self.pi+math.pi
            time=time+self.dt
            self.time.append(time)
    def show(self):
        pl.plot(self.time,self.dangle)
        pl.title("log(dangle) changes with time")
        pl.xlabel("time ($s$)")
        pl.ylabel("log(dangle) ($radians$)")
        pl.show()
p=pendulum()
p.caculate()
p.show() 
