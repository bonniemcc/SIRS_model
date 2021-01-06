#!/bin/sh

#$ -N BONNIE_MVP
#$ -cwd
#$ -q cm.7.day
#$ -l h_vmem=1G
#$ -l h_rt=4:00:00

# Send mail at submission and completion of script
#$ -m be
#$ -M s1534750@sms.ed.ac.uk

#export MYHOME=`pwd`
#export MYSCRATCH=/scratch/`pwd`

#mkdir -p $MYSCRATCH

#cp  $MYHOME/*  $MYSCRATCH/

#cd $MYSCRATCH

echo -e "\n#############################################################"
date
hostname
echo -e "#############################################################\n"

# TYPE COMMAND LINE HERE -----------------------------------------------------------


#counter=0
#while [ $counter -le 10 ]
#do
#echo $counter
#((counter++))

python3 cp2sirs_copy.py 50 10000 0.3 0.3 0.3 n

echo "Job ran on $( hostname ) " > $MYHOME/mylog

#done
#echo All done


#cp  $MYSCRATCH/*  $MYHOME/
#rm -r $MYSCRATCH
