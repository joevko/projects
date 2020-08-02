#!/bin/bash
# time tracker
# commands:
# * track start "label"
# * track stop
# * track status
# * log

export LOGFILE1="logfile.txt"
export LOGFILE2="log.txt"
ongoing=0
label=""


function track() {
    task=$1
    #label=$2
    if [ $task == "start" ];
	then
        if [ $ongoing -eq 0 ];
        then
            START_TIME=$SECONDS;
            label=$2
            ongoing=1
            echo "START " $(date) >> $LOGFILE1
            echo "LABEL " $label >> $LOGFILE1
            echo "START " $(date)
            echo "LABEL " $label

        else
            echo "Already running."
        fi
    elif [ $task == "stop" ];
    then
        if [ $ongoing -eq 1 ];
        then
            ELAPSED_TIME=$(($SECONDS - $START_TIME))
            ongoing=0
            echo "END " $(date) >> $LOGFILE1
            echo "END " $(date)
            TZ=UTC0 printf '%s: %(%H:%M:%S)T\n' $label "$ELAPSED_TIME" >> $LOGFILE2
        else
            echo "Task is not running. Nothing to stop."
        fi
    elif [ $task == "status" ];
    then
        if [ $ongoing -eq 1 ];
        then
            echo LABEL $label is currently running.
        else
            echo "No tasks running."
        fi
    fi
}
# the elapsed time is saved in log txt file
# use command log to check all the logged times for the tasks
function log() {
if [ ! -f "$LOGFILE2" ]
then
  echo "No tasks recorded"
else
while IFS= read -r line
do
  echo "$line"
done < "$LOGFILE2"
fi
}
