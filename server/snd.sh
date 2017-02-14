#!/bin/bash

ot='out.txt'
z=$(cat ot.txt|sed -e 's/#/\n/g')
sendmail -t $z
