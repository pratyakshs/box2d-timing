"""
Simple demo of a horizontal bar chart.
"""
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
with open('./data/first.csv', 'r') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=',')
	for i in range(0,iter_count):		
		for s in spamreader:  
			STEP_SUM= STEP_SUM + float(s[1])
			COLL_SUM= COLL_SUM + float(s[2])
			VEL_SUM= VEL_SUM + float(s[3])
			POS_SUM= POS_SUM + float(s[4])
			LOOP_SUM=LOOP_SUM + float(s[5])
			STEP_MAX=max(STEP_MAX,float(s[1]))
			STEP_MIN=min(STEP_MIN,float(s[1])) 
			SUM_SQUARES=SUM_SQUARES + float(s[1])*float(s[1])
		STEP_AVG.append(STEP_SUM/iter_count)
		COLL_AVG.append(COLL_SUM/iter_count)
		VEL_AVG.append(VEL_SUM/iter_count)
		POS_AVG.append(POS_SUM/iter_count)
		LOOP_AVG.append(LOOP_SUM/iter_count)
		ERR_AVG.append(SUM_SQUARES/iter_count)

# Example data
#people = ('Tom', 'Dick', 'Harry', 'Slim', 'Jim')
#y_pos = np.arange(len(people))
#performance = 3 + 10 * np.random.rand(len(people))
#error = np.random.rand(len(people))

fig = plt.figure()

width = .35
a=[]
for i in (0,iter_count):
	a.append(i+1)
#ind = np.arange(len(OY))
index = np.arange(iter_count)
plt.bar(index,STEP_AVG, width)
#plt.bar(a,STEP_AVG)
#plt.xticks(ind + width / 2, OX)

#fig.autofmt_xdate()

plt.savefig("figure.png")
#plt.barh(y_pos, performance, xerr=error, align='center', alpha=0.4)
#plt.yticks(y_pos, people)
#plt.xlabel('Performance')
#plt.title('How fast do you want to go today?')
#plt.savefig("test.png")
#plt.show()

