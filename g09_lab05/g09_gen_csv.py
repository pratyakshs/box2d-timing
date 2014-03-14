import re
import subprocess
import random
i_max=15
j_max=10
file_path = "./mybins/cs296_09_exe"
output_file = open("./data/g09_lab09data_01.csv",'w')
output_file2 = open("./data/g09_lab09data_02.csv",'w')
STEP_SUM=0
COLL_SUM=0
VEL_SUM=0
POS_SUM=0
LOOP_SUM=0
STEP_MAX=0
STEP_MIN=100
ITER_VAL=0
SUM_SQUARES=0
for i in range(0,i_max):
	for j in range(0,j_max):
		out=subprocess.Popen([file_path,str(i+1)],stdout=subprocess.PIPE)
		val=str(out.stdout.read())
		s = re.findall('[0-9]+(?:\.[0-9]+)?', val)
		print(s)
#		while IFS=',' read iter rerun step coll vel pos loop 
#		STEP_SUM= STEP_SUM + float(s[1])
#		COLL_SUM= COLL_SUM + float(s[2])
#		VEL_SUM= VEL_SUM + float(s[3])
#		POS_SUM= POS_SUM + float(s[4])
#		LOOP_SUM=LOOP_SUM + float(s[5])
#		STEP_MAX=max(STEP_MAX,float(s[1]))
#		STEP_MIN=min(STEP_MIN,float(s[1])) 
#		SUM_SQUARES=SUM_SQUARES + float(s[1])*float(s[1])
		output_file.write(s[0]+","+str(j+1)+","+s[1]+","+s[2]+","+s[3]+","+s[4]+","+s[5]+'\n')#+","+STEP_SUM/#j_max+","+STEP_MAX+","+STEP_MIN+","+COLL_SUM/j_max+","+VEL_SUM/j_max+","+POS_SUM/j_max+","LOOP_SUM/j_max+"\n")
output_file.close()
INPUT=open("./data/g09_lab09data_01.csv",'r')
reader=INPUT.read()
LINES=reader.splitlines()
j_rand=5
for i in range(0,i_max):
	for j in range(0,j_rand):
		output_file2.write(LINES[i + random.randint(0,j_max)]+'\n')

