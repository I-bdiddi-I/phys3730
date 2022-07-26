#!/bin/sh
exefil=SMBH_Code
for Mbh in 1 2 ; do
    for spin in 0 0.998 ; do
	logfil=SMBH_Mbh_${Mbh}_spin_${spin}.log
	echo nohup $exefil $Mbh $spin '>'$logfil '&'
	# nohup $exefil $Mbh $spin > $logfil &
    done
done
