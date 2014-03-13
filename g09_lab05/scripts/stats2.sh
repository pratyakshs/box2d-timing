#!/bin/bash
DATADIR=../data
INPUTFILER=$DATADIR/g09_lab05data_random.csv
INPUTFILE2=$DATADIR/g09_lab05data_02.csv
OUTPUTFILER=$DATADIR/tempr.csv
OUTPUTFILE2=$DATADIR/temp2.csv
if test -e $OUTPUTFILE2
then rm $OUTPUTFILE2
fi
if test -e $OUTPUTFILER
then rm $OUTPUTFILER
fi

STEP_SUM_R=0
STEP_SUM_2=0
ITER_VAL=0
i=0
while IFS=',' read iter rerun step coll vel pos loop
do 
	i=$(($i+1));
	STEP_SUM_R=`echo "$STEP_SUM_R + $step" | bc`;
	ITER_VAL=$iter;

	if [ $(($i%15)) == 0 ] 
	then	echo -n $ITER_VAL >> $OUTPUTFILER;
	    	echo -n "," >> $OUTPUTFILER;
	    	echo `echo "scale=5; $STEP_SUM_R/15.0" | bc` >> $OUTPUTFILER;
			STEP_SUM_R=0;
	fi
done <$INPUTFILER

ITER_VAL=0
i=0
while IFS=',' read iter rerun step coll vel pos loop
do 
	i=$(($i+1));
	STEP_SUM_2=`echo "$STEP_SUM_2 + $step" | bc`;
	ITER_VAL=$iter;

	if [ $(($i%150)) == 0 ] 
	then	echo -n $ITER_VAL >> $OUTPUTFILE2;
			echo -n "," >> $OUTPUTFILE2;
			echo `echo "scale=5; $STEP_SUM_2/150.0" | bc` >> $OUTPUTFILE2;
			STEP_SUM_2=0;
	fi
done <$INPUTFILE2

## the OUTPUTFILE CONTAINTS DATA IN FORMAT: iter_val,avg_step,avg_coll,avg_vel,std_dev,avg_loop,avg_pos
