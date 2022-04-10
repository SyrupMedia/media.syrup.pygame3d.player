#!/usr/bin/sh

if [ ! -d '../../Build' ]; then
	mkdir '../../Build'
fi

cd ../ 

python Setup.py build_ext --inplace # Convert Python to C

# Cleaning
mv Main.cpython-310-x86_64-linux-gnu.so ../Build/PyGame3D.so
rm -r -f build/
rm -f Main.c