import subprocess
import sys
import os

# The most important thing here is to add openblas to the PATH; 
# don't bother with using *.bc format; it doesn't work

cmd = "export LD_LIBRARY_PATH=/opt/OpenBLAS/lib && /tmp/inception/_build/default/classify.exe"
cmd = cmd + " /tmp/inception_img/" + sys.argv[1] # agree with Dockerfile
try:
    os.system(cmd)
except Exception, e:  
    print e

