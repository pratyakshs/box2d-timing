import re
import subprocess
i_max=15
j_max=10
file_path = "./mybins/cs296_09_exe"
output_file = open("./data/g09_lab09data_01.csv",'w')
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
		out=subprocess.Popen(file_path,stdout=subprocess.PIPE)
		val=str(out.stdout.read())
#print(val)
		s = re.findall('[0-9]+(?:\.[0-9]+)?', val)
#print(s)
		output_file.write(s[0]+","+ str(j+1) + s[1] +"," + s[2] + "," + s[3] + "," + s[4] + "\n")
