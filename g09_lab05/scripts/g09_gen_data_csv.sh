#!/bin/bash
DATADIR=../data
OUTPUTFILE=$DATADIR/g09_lab05data_02.csv
if test -e $OUTPUTFILE
then rm $OUTPUTFILE
fi

for i in {1..1500} #should be 1500
do
	for j in {1..150} #should be 150
	do	
		echo $i | ../mybins/cs296_09_exe | sed -e 's/[^0-9. ]*//g' -e 's/ \+//' | awk -v iter=$j ' { if (NR == 2) {printf("%s,", iter);}if (NR == 6)  {} else{ printf("%s",$1); if (NR % 7 == 0) {printf("\n")} else {printf(",")}}}' >> $OUTPUTFILE
	done
done
