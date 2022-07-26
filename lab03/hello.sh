#!/bin/sh
echo 'Hello, world'

if [ $# != 0 ] ; then
    echo And hello $*.
fi
