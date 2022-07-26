#!/bin/sh
sum=0
for x in $* ; do
    sum=`echo $sum + $x | bc`
done
echo $sum
