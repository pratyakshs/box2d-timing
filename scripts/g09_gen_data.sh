#!/bin/bash
for i in {1..1500}
do
	for j in {1..150}
	do
		echo $i | ../mybins/cs296_09_exe > ../data/g09out-$i-$j.txt
	done
done	
