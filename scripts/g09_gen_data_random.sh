#!/bin/bash
DATADIR=../data
INPUTFILE=$DATADIR/g09_lab05data_02.csv
#inputfile should be lab05data_02

OUTPUTFILE=$DATADIR/g09_lab05data_random.csv
if test -e $OUTPUTFILE
then rm $OUTPUTFILE
fi

for i in {1..1500} # limit should be 1500
do
	for j in {1..15} # limit should be 15
	do
		k=$(($RANDOM%150+1))
		line_num=$((150*($i-1)+$k))
		# echo $k
		sed -n "$line_num p" <$INPUTFILE >> $OUTPUTFILE 
	done
done

