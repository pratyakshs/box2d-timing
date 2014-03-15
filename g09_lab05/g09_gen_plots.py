from pylab import *
from collections import defaultdict
import math
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import csv
avg_step = 0
STEP_SUM = 0
COLL_SUM = 0
VEL_SUM = 0
POS_SUM = 0
LOOP_SUM = 0
STEP_MAX = 0
STEP_MIN = 100
ITER_VAL = 0
SUM_SQUARES = 0
iter_count = 500
STEP_AVG = []
COLL_AVG = []
VEL_AVG = []
POS_AVG = []
LOOP_AVG = []
ERR_AVG = []
reruns = 50
i = 0
with open('./data/g09_lab09data_01.csv', 'r') as csvfile:
	csvdata = csv.reader(csvfile, delimiter = ',')		
	for s in csvdata: 
		STEP_SUM = STEP_SUM + float(s[2])
		COLL_SUM = COLL_SUM + float(s[3])
		VEL_SUM = VEL_SUM + float(s[4])
		POS_SUM = POS_SUM + float(s[5])
		LOOP_SUM = LOOP_SUM + float(s[6])
		STEP_MAX = max(STEP_MAX,float(s[2]))
		STEP_MIN = min(STEP_MIN,float(s[2])) 
		SUM_SQUARES = SUM_SQUARES + float(s[2])*float(s[2])
		i = i+1
		if i == reruns:
			STEP_AVG.append(STEP_SUM/reruns)
			COLL_AVG.append(COLL_SUM/reruns)
			VEL_AVG.append(VEL_SUM/reruns)
			POS_AVG.append(POS_SUM/reruns)
			LOOP_AVG.append(LOOP_SUM/reruns)
			ERR_AVG.append(math.sqrt((SUM_SQUARES/reruns)-(STEP_SUM/reruns)*(STEP_SUM/reruns)))
			i = 0
			STEP_SUM = 0
			COLL_SUM = 0		
			VEL_SUM = 0
			POS_SUM = 0
			LOOP_SUM = 0
			SUM_SQUARES = 0

a = []
for i in (0,iter_count):
	a.append(i+1)
#ind = np.arange(len(OY))
index = range(1, iter_count + 1)

plt.bar(index,STEP_AVG,label = "Step time average")
plt.plot(index,LOOP_AVG,label = "Loop time average")
plt.xlabel("Iteration count")
plt.ylabel("Step-time and loop-time average in ms")
loop_max = max(LOOP_AVG)
loop_min = min(LOOP_AVG)
plt.annotate('minimum', xy = (0, loop_min), xytext = (1, loop_min+2),
      arrowprops = dict(facecolor = 'black', shrink = 0.05),
      )
plt.annotate('maximum', xy = (iter_count - 1, loop_max), xytext = (iter_count -2, loop_max-2),
      arrowprops = dict(facecolor = 'black', shrink = 0.05),
      )
plt.legend()
plt.savefig("figure.png")


plt.clf()
plt.plot(index,COLL_AVG,label = "collision time average")
plt.plot(index,VEL_AVG,label = "velocity time average")
plt.plot(index,POS_AVG,label = "position time average")
plt.plot(index,[i+j+k for i, j, k in zip(COLL_AVG,VEL_AVG,POS_AVG)],label = "vel+pos+coll times average")
plt.legend()
plt.xlabel("Iteration count")
plt.ylabel("vel,pos,coll and total sum times in ms")
plt.savefig("figure2.png")


plt.clf()
plt.errorbar(index, STEP_AVG, yerr = ERR_AVG,label = "error in step_time ")
plt.plot(index,STEP_AVG,label = "step-time average")
plt.xlabel("Iteration count")
plt.ylabel("Step-time average in ms")
plt.legend()
plt.savefig("figure3.png")


rollno = 40
with open('./data/g09_lab09data_01.csv', 'r') as csvfile:
	csvdata = csv.reader(csvfile, delimiter = ',')
	sel_rows = [row for row in csvdata if int(row[0]) == rollno]
sel_step_avg = [float(i[2]) for i in sel_rows]
plt.clf()
plt.hist(array(sel_step_avg), bins = 10, label = "Frequency bar chart")
hist, bins = np.histogram(sel_step_avg, bins = 10)
offset = bins[1:] - bins[:-1]
plt.plot(bins[:-1] + offset, np.cumsum(hist), label = "Cumulative frequency")
plt.xlabel("Step time intervals (in ms)")
plt.ylabel("Step time frequency")
plt.legend()
plt.savefig('figure4.png')


csvr = open('./data/g09_lab09data_random.csv', 'r')
datar = csv.reader(csvr, delimiter = ',')
step_avgr = []
step_sumr = 0
rand_rows = 15
for i, j in enumerate(datar):
	step_sumr += float(j[2])
	if (i + 1) % rand_rows == 0:
		step_avgr.append(step_sumr)
		step_sumr = 0
step_avgr = [i/rand_rows  for i in step_avgr]

plt.clf()
plt.plot(index, STEP_AVG, 'yx', label = "data from g09_lab09data_01.csv")
#plt.plot(index, step_avgr, 'ro', ms = 3)

fitr = polyfit(index, step_avgr, 1)
fit_fnr = poly1d(fitr)
plt.plot(index, step_avgr, 'ko', ms = 3, label = "data from g09_lab09data_random.csv")
plt.plot(index, fit_fnr(index), '--k', label = "best fit line of data of random sampled reruns.csv")

fit = polyfit(index, STEP_AVG, 1)
fit_fn = poly1d(fit)
plt.plot(index, fit_fn(index), 'y', label = "best fit line of data for all reruns")
plt.xlabel("Iteration count")
plt.ylabel("Step time (Averaged over reruns)")
plt.ylim([0,0.5])
plt.legend()
plt.savefig('fig5.png')
