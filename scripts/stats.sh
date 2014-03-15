#!/bin/bash
DATADIR=../data
INPUTFILE1=$DATADIR/g09_lab05data_01.csv
OUTPUTFILE=$DATADIR/temp1.csv
if test -e $OUTPUTFILE
then rm $OUTPUTFILE
fi

STEP_SUM=0
COLL_SUM=0
VEL_SUM=0
POS_SUM=0
LOOP_SUM=0
STEP_MAX=0
STEP_MIN=100
ITER_VAL=0
SUM_SQUARES=0
i=0
while IFS=',' read iter rerun step coll vel pos loop
do 
	i=$(($i+1));
	STEP_SUM=`echo "$STEP_SUM + $step" | bc`;
	COLL_SUM=`echo "$COLL_SUM + $coll" | bc`;
	VEL_SUM=`echo "$VEL_SUM + $vel" | bc`;
	POS_SUM=`echo "$POS_SUM + $pos" | bc`;
	LOOP_SUM=`echo "$LOOP_SUM + $loop" | bc`;
#	echo "$SUM_SQUARES + $step *$step";
	SUM_SQUARES=`echo "$SUM_SQUARES + $step * $step" | bc`;
	ITER_VAL=$iter;
#	STEP_SUM=`echo "$STEP_SUM + $var3" | bc`
#	STEP_SUM=`echo "$STEP_SUM + $var3" | bc`

##echo $i
	if [ $(($i%150)) == 0 ] 
	then	echo -n $ITER_VAL >> $OUTPUTFILE;
	    	echo -n "," >> $OUTPUTFILE;
		echo -n `echo "scale=5; $STEP_SUM/150.0" | bc` >> $OUTPUTFILE;
		echo -n "," >> $OUTPUTFILE;
		echo -n `echo "scale=5; $COLL_SUM/150.0" | bc` >> $OUTPUTFILE;
		echo -n "," >> $OUTPUTFILE;
		echo -n `echo "scale=5; $VEL_SUM/150.0" | bc` >> $OUTPUTFILE;
		echo -n "," >> $OUTPUTFILE;
		echo -n `echo "scale=5; sqrt(($SUM_SQUARES/150.0) - (($STEP_SUM/150.0) * ($STEP_SUM/150.0)))" | bc` >> $OUTPUTFILE;
		echo -n "," >> $OUTPUTFILE;
		echo -n `echo "scale=5; $LOOP_SUM/150.0" | bc` >> $OUTPUTFILE;
		echo -n "," >> $OUTPUTFILE;
		echo `echo "scale=5; $POS_SUM/150.0" | bc` >> $OUTPUTFILE;
		STEP_SUM=0; COLL_SUM=0; VEL_SUM=0; POS_SUM=0; LOOP_SUM=0; SUM_SQUARES=0;
	fi
		
done <$INPUTFILE1

## the OUTPUTFILE CONTAINTS DATA IN FORMAT: iter_val,avg_step,avg_coll,avg_vel,std_dev,avg_loop,avg_pos
