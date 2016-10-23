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
        Bchum=4*10**(-5)
        g=9.8
        valuex=0
        valuey=0        
        velx=0
        vely=0
        a=6.5*10**(-3)
        To=20+273.15
        alpha=2.5
        wind=-10
        for i in range(1000):        
            valuex=self.x[i]+vx[i]*self.dt
            velx=vx[i]-(1-a*self.y[i]/To)**alpha*Bchum*math.sqrt((vx[i]-wind)**2\
            +vy[i]**2)*(vx[i]-wind)*self.dt
            valuey=self.y[i]+vy[i]*self.dt
            vely=vy[i]-g*self.dt-(1-a*self.y[i]/To)**alpha*Bchum*\
            math.sqrt((vx[i]-wind)**2+vy[i]**2)*vy[i]*self.dt
            self.x.append(valuex)
            self.y.append(valuey)
            vx.append(velx)
            vy.append(vely)
            self.time.append(self.time[i]+self.dt)
    def show(self):
        pl.plot(self.x,self.y,'r')
        pl.title("The trajectory of the cannon shell")
        pl.xlabel("x")
        pl.ylabel("y")
print "输入靶目标的坐标 ->"
(a,b)=input()
print a,b
if a>29561:
    print "超出炮弹最大水平出射距离"
elif b>5142:
    print "超出炮弹最大竖直出射距离"
elif b<-24433:
    print "超出炮弹最小竖直出射距离"
elif a<=0:
    print "输入数值无效"
else:
    targetx=a
    targety=b
    print targetx,targety
    cannonnumber=[]
    locat=[]
    for j in range(89):
        cann=cannon(700,math.radians(1+j),0.1)
        cann.caculate()
        for i in range(1000):
            for k in range(1000):
                if math.sqrt((cann.x[i]-targetx)**2+(cann.y[k]-targety)**2)<=10:
                    cannonnumber.append(j+1)
                    locat.append((cann.x[i],cann.y[k]))
                else:
                    continue
    minang=min(cannonnumber)
    print "要打击靶目标",(targetx,targety),"最小的角度为",minang,"度"
    print "用最小角度打击靶目标的图线为"
    cann=cannon(700,math.radians(minang),0.1)
    cann.caculate()
    cann.show()

