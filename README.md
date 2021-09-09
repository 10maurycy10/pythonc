# Pythonc

Pythonc is a fast python compiler.

## Building

### Required programs

Pythonc requires a working python3.

    sudo apt install python

You can build pythonc with this command:

    python3 pythonc.py pythonc.py pythonc 3

## Usage

    /path/to/pythonc inputfile.py outputfile [python version]

## Features

1. Very fast compilation of python programs.

2. JIT optimization

### Features that will not be implemented

1. Windows support (I do not have a windows box with a _working_ python install)

2. static linking with modules

### Features that might be implemented soon™

1. Removing requirement for python3 on target
