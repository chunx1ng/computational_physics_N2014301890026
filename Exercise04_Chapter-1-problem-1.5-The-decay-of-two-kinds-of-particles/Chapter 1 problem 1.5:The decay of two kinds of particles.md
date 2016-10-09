#第四次作业

##作业要求
* 习题1.5

##摘要
* 系统存在两个粒子，同时发生衰变，每种粒子衰变可变成另一种粒子。可以近似模拟做作粒子在A和B两种状态之间震荡，由以下微分方程描述：
* ![查看图片](http://a2.qpic.cn/psb?/V14dvOL90MQVdu/f55dapEdpZfSS2D*V9trDIde5nMIPzex6x4JoxoWglI!/b/dAkBAAAAAAAA&bo=2wFbANsBWwADByI!&rf=viewer_4)
* 尝试模拟当Na=100，Nb=0，t步长为1s时系统的演变情况

##背景介绍
* 采用欧拉法进行数值模拟

##源代码
```

import pylab as pl
class db_decay:
    def __init__(self,number_of_Na,number_of_Nb,footstep):
        self.Na=[number_of_Na]
        self.Nb=[number_of_Nb]
        self.t=footstep
        self.total_time=footstep*70
        self.time=[0]
        self.time_constant=1
    def caculate(self):
        for i in range(70):
            numberA=self.Na[i]+(self.Nb[i]-self.Na[i])/self.time_constant*self.t
            numberB=self.Nb[i]+(self.Na[i]-self.Nb[i])/self.time_constant*self.t
            self.Na.append(numberA)
            self.Nb.append(numberB)
            self.time.append(self.time[i]+self.t)
    def draw(self):
        pl.plot(self.time,self.Na,'r',label='number of nuclei A')
        pl.plot(self.time,self.Nb,'b',label='number of nuclei B')
        pl.title('The change of number of two different nuclei A and B in double decay')
        pl.xlabel('time')
        pl.ylabel('number of nuclei')
        pl.legend(loc='best')

sys=db_decay(100,0,0.05)
sys.caculate()
sys.draw()

```

##结果展示
* ![查看图片](http://a3.qpic.cn/psb?/V14dvOL90MQVdu/4sidSs1pTVRuOUjiCBKrXO2Sxair*GSDwiihJRCKE2s!/b/dNoAAAAAAAAA&bo=IgOIAQAAAAADB4o!&rf=viewer_4)

##致谢
* 在数组的使用上遇到问题，参考了倪世杰同学的程序
