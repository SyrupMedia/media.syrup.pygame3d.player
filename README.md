# PyGame 3D Player Controller
### media.syrup.pygame3d.player

[![Ko-Fi](https://img.shields.io/badge/donate-kofi-blue?style=for-the-badge&logo=ko-fi&color=E35B57&logoColor=FFFFFF&labelColor=232323)](https://ko-fi.com/molasses)
[![Patreon](https://img.shields.io/badge/donate-patreon-blue?style=for-the-badge&logo=patreon&color=E35B57&logoColor=FFFFFF&labelColor=232323)](https://www.patreon.com/molasseslover)
![GitHub Downloads](https://img.shields.io/github/downloads/SyrupMedia/media.syrup.pygame3D.player/total?color=E35B57&logo=github&logoColor=FFFFFF&style=for-the-badge&labelColor=232323)

## About
This is a free and open-source game framework and player controller using the [PyGame](https://www.pygame.org) module for the Python programming language.

This is not intended for professional use; it is really primitive all things considered. This was made in a single sitting in hopes of making
PyGame game development more accesible. 

![Preview](Assets/Preview.svg)

## Building
You can build this project using [Cython](https://cython.org) in order to turn it into a library file.

In order to build, simply run the [`Build.sh`](Source/Building/Build.sh) script with your Shell of choice.

```zsh
cd Source/Building/
chmod +x Build.sh
sh Build.sh # `./Build.sh` works too!
```

## Dependencies
[![Cython](https://img.shields.io/badge/cython-pip-blue?style=for-the-badge&logo=python&color=E35B57&logoColor=FFFFFF&labelColor=232323)](https://pypi.org/project/Cython)
[![PyGame](https://img.shields.io/badge/pygame-pip-blue?style=for-the-badge&logo=python&color=E35B57&logoColor=FFFFFF&labelColor=232323)](https://pypi.org/project/pygame)
[![PyOpenGL](https://img.shields.io/badge/pyopengl-pip-blue?style=for-the-badge&logo=python&color=E35B57&logoColor=FFFFFF&labelColor=232323)](https://pypi.org/project/PyOpenGL)

This project depends on the [PyGame](https://www.pygame.org) and [PyOpenGL](http://pyopengl.sourceforge.net/) modules for Python.

Here is the installation command:
```sh
pip install pygame pyopengl
```

If you are looking to build this project using [Cython](https://cython.org), 
you might have to install that as well.

Here is its installation command:
```sh
pip install cython
```