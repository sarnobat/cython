#pip3 install cython
cython --embed gedcom_helloworld.pyx
gcc -Os -I "/usr/local/homebrew/Cellar/python@3.9/3.9.5/Frameworks/Python.framework/Versions/3.9/include/python3.9" -L "/usr/local/homebrew/Cellar/python@3.9/3.9.5/Frameworks/Python.framework/Versions/3.9/lib/"  gedcom_helloworld.c -lpython3.9 -o gedcom_helloworld