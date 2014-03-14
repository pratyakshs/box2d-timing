import math
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import csv
avg_step=0
STEP_SUM=0
COLL_SUM=0
VEL_SUM=0
POS_SUM=0
LOOP_SUM=0
STEP_MAX=0
STEP_MIN=100
ITER_VAL=0
SUM_SQUARES=0
iter_count=15
STEP_AVG=[]
COLL_AVG=[]
VEL_AVG=[]
POS_AVG=[]
LOOP_AVG=[]
ERR_AVG=[]
reruns=10
i=0
with open('./data/first.csv', 'r') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=',')		
	for s in spamreader:  
		STEP_SUM= STEP_SUM + float(s[2])
		COLL_SUM= COLL_SUM + float(s[3])
		VEL_SUM= VEL_SUM + float(s[4])
		POS_SUM= POS_SUM + float(s[5])
		LOOP_SUM=LOOP_SUM + float(s[6])
		STEP_MAX=max(STEP_MAX,float(s[2]))
		STEP_MIN=min(STEP_MIN,float(s[2])) 
		SUM_SQUARES=SUM_SQUARES + float(s[2])*float(s[2])
		i=i+1
		if i==reruns:
			STEP_AVG.append(STEP_SUM/reruns)
			COLL_AVG.append(COLL_SUM/reruns)
			VEL_AVG.append(VEL_SUM/reruns)
			POS_AVG.append(POS_SUM/reruns)
			LOOP_AVG.append(LOOP_SUM/reruns)
			ERR_AVG.append(math.sqrt((SUM_SQUARES/reruns)-(STEP_SUM/reruns)*(STEP_SUM/reruns)))
			i=0
			STEP_SUM=0
			COLL_SUM=0		
			VEL_SUM=0
			POS_SUM=0
			LOOP_SUM=0
			SUM_SQUARES=0

a=[]
for i in (0,iter_count):
	a.append(i+1)
#ind = np.arange(len(OY))
index = np.arange(iter_count)
plt.bar(index,STEP_AVG,label="Step time average")
plt.plot(index,LOOP_AVG,label="Loop time average")
plt.xlabel("Iteration count")
plt.ylabel("Step-time and loop-time average in ms")
loop_max=max(LOOP_AVG)
loop_min=min(LOOP_AVG)
plt.annotate('minimum', xy=(0, loop_min), xytext=(1, loop_min+2),
            arrowprops=dict(facecolor='black', shrink=0.05),
            )
plt.annotate('maximum', xy=(iter_count - 1, loop_max), xytext=(iter_count -2, loop_max-2),
            arrowprops=dict(facecolor='black', shrink=0.05),
            )
plt.legend()
plt.savefig("figure.png")
plt.clf()
plt.plot(index,COLL_AVG,label="collision time average")
plt.plot(index,VEL_AVG,label="velocity  time average")
plt.plot(index,POS_AVG,label="position time average")
plt.plot(index,[i+j+k for i, j, k in zip(COLL_AVG,VEL_AVG,POS_AVG)],label="vel+pos+coll times average")
plt.legend()
plt.xlabel("Iteration count")
plt.ylabel("vel,pos,coll and total sum times in ms")
plt.savefig("figure2.png")
plt.clf()
plt.errorbar(index, STEP_AVG, yerr=ERR_AVG,label="error in step_time ")
plt.plot(index,STEP_AVG,label="step-time average")
plt.xlabel("Iteration count")
plt.ylabel("Step-time average in ms")
plt.legend()
plt.savefig("figure3.png")
#fig.autofmt_xdate()
#plt.barh(y_pos, performance, xerr=error, align='center', alpha=0.4)
#plt.yticks(y_pos, people)
#plt.xlabel('Performance')
#plt.title('How fast do you want to go today?')
#plt.savefig("test.png")
#plt.show()

