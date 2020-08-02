#!/bin/bash
# This is a program that allows the user to climb up the directory tree.
# commands "climb" and "climb 1" take you one directory back.
# climb up the directory tree by calling the climb function followed by
# a number
function climb {
  local a=$1
  local FILEUP="../"
  if [[ "$a" -eq "0" || "$a" -eq "1" ]]; then
    cd "$FILEUP"
  else
    for (( i=0; i < $1; i++ ))
  	do
  		UP+=../
  	done
      	cd "$UP"
  fi
}
