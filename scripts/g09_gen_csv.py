import re
import subprocess
import random

num_iters = 500
num_reruns = 50
exe_path = "./mybins/cs296_09_exe"
csv1 = open("/data/g09_lab09data_01.csv",'w+')
csv2 = open("/data/g09_lab09data_02.csv",'w+')
csvr = open("/data/g09_lab09data_random.csv",'w+')


for i in range(0,num_iters):
	for j in range(0,num_reruns):
		out1 = subprocess.Popen([exe_path,str(i+1)], stdout = subprocess.PIPE)
		val1 = str(out1.stdout.read())
		s1 = re.findall('[0-9]+(?:\.[0-9]+)?', val1)
		
		out2 = subprocess.Popen([exe_path,str(i+1)], stdout = subprocess.PIPE)
		val2 = str(out2.stdout.read())
		s2 = re.findall('[0-9]+(?:\.[0-9]+)?', val2)	

		csv1.write(s1[0]+","+str(j+1)+","+s1[1]+","+s1[2]+","+s1[3]+","+s1[4]+","+s1[5]+'\n')
		csv2.write(s2[0]+","+str(j+1)+","+s2[1]+","+s2[2]+","+s2[3]+","+s2[4]+","+s2[5]+'\n')



csv1.close()
csv2.close()

INPUT = open("./data/g09_lab09data_01.csv",'r')
LINES = INPUT.read().splitlines()
j_rand = 15
for i in range(0, num_iters):
	for j in random.sample(LINES[i * num_reruns : (i+1) * num_reruns], j_rand):
		print(j, end = '\n', file = csvr)

