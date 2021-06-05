#pip3 install cython
#python3.9 setup.py build_ext --inplace

cython --embed helloworld.pyx
gcc -Os -I "/usr/local/homebrew/Cellar/python@3.9/3.9.5/Frameworks/Python.framework/Versions/3.9/include/python3.9" -L "/usr/local/homebrew/Cellar/python@3.9/3.9.5/Frameworks/Python.framework/Versions/3.9/lib/"  helloworld.c -lpython3.9 -o helloworld