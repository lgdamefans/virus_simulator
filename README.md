# virus_simulator
本仿真程序是通过模拟在一定区域内随机行走的人群，来模拟新冠病毒在人群中传播的。

所有人群的个体都有四种状态：健康，感染，免疫，死亡。

在不同的防疫措施下，人们的移动不一样，在没有进行封锁的情况下，人们的移动方向和距离是完全随机且服从高斯分布的，在封锁的情况下，大部分的行动被限制，但仍有少部分人保持移动，这代表了一些从事不可或缺工作的人。
封锁从人数第一次达到临界开始，一直持续到疫情结束。

感染的模式也有两种，在人群中感染人数偏少的时候，在感染人群周围的人有小概率被感染，而在感染人数超过半数时，一个健康人被感染的概率取决于周边患病人的个数。而死亡和痊愈，全部取决于概率。对于死亡，不同的年龄有着不同的死亡率，这也符合新冠病毒对高龄人死亡率较高的事实，而得到治疗的患者致死率将为原来的一半。

同时，还引入了经济因素，根据参考文献，我设置了三种主要经济成分，一部分来自于人，主要取决于健康人的个数，而一部分为商业，我将商业分为了两部分，一部分会受到封锁的冲击而关闭，另一部分为一些必需品如饮食等，还有一部分为政府收入，来自于另外两个所缴纳的税金。

根据不同的防疫措施，我进行了实验，以下分别为什么都不做，封锁，封锁+洗手+戴口罩的结果

Do no work：

total timesteps taken: 3384

total dead: 94

total recovered: 1815

total unaffected: 81

deathrate 94/2000 = 4.7%
![Image text](https://github.com/lgdamefans/virus_simulator/blob/master/img-folder/%E5%9B%BE%E7%89%871.png)

Lockdown:

total timesteps taken: 4335

total dead: 55

total recovered: 1568

total unaffected: 377

deathrate = 2.75%

![Image text](https://github.com/lgdamefans/virus_simulator/blob/master/img-folder/图片2.png)

Lockdown(wash hands+wear masks)

total timesteps taken: 4413

total dead: 24

total recovered: 1306

total unaffected: 670

deathrate = 1.2%

![Image text](https://github.com/lgdamefans/virus_simulator/blob/master/img-folder/图片3.png)

此外，针对不同的人群密度，我也进行了一次实验，用来考察人群聚集度对病毒传播的影响，分别考察在高密度、中密度、低密度情况下疫情的传播状况

High density(population = 5000)

total timesteps taken: 1806

total dead: 398

total recovered: 4568

total unaffected: 34

deathrate = 7.96%

![Image text](https://github.com/lgdamefans/virus_simulator/blob/master/img-folder/图片4.png)

Mid density(population = 2000)

total timesteps taken: 3384

total dead: 94

total recovered: 1815

total unaffected: 81

deathrate 94/2000 = 4.7%

![Image text](https://github.com/lgdamefans/virus_simulator/blob/master/img-folder/图片1.png)

Low density

total timesteps taken: 1071

total dead: 0

total recovered: 10

total unaffected: 990

![Image text](https://github.com/lgdamefans/virus_simulator/blob/master/img-folder/图片5.png)
