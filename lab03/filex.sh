#!/bin/sh   
for p in * ; do
   if [ -f $p ] ; then 
       lsout=`ls -lt $p | awk '{print $5}'`
       per=`ls -lt $p | awk '{print $1}'`
	echo file: $p permissions: $per size: $lsout
   fi  
done
