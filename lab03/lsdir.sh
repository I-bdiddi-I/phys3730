#!/bin/sh

for p in * ; do
    if [ -d $p ] ; then
       echo "sub-dir: $p"
    fi
done
