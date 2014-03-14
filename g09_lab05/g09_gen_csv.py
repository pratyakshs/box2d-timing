import re
import subprocess
import random

num_iters = 500
num_reruns = 50
exe_path = "./mybins/cs296_09_exe"
csv1 = open("/data/g09_lab09data_01.csv",'w+')
csv2 = open("/data/g09_lab09data_random.csv",'w+')

for i in range(0,num_iters):
	for j in range(0,num_reruns):
		out = subprocess.Popen([exe_path,str(i+1)], stdout = subprocess.PIPE)
		val = str(out.stdout.read())
		s = re.findall('[0-9]+(?:\.[0-9]+)?', val)
#		print(s)
		csv1.write(s[0]+","+str(j+1)+","+s[1]+","+s[2]+","+s[3]+","+s[4]+","+s[5]+'\n')



csv1.close()

INPUT = open("./data/g09_lab09data_01.csv",'r')
LINES = INPUT.read().splitlines()
j_rand = 15
for i in range(0, num_iters):
	for j in random.sample(LINES[i * num_reruns : (i+1) * num_reruns], j_rand):
		print(j, end = '\n', file = csv2)

