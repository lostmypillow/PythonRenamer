import os, sys
def modify_name(pname):
    base = os.path.basename(pname)
    list = os.path.splitext(base)
    modifier = list[0]
    queue[1] = modifier
    print(queue)
def renaming(dict, entry):
    var = dict[entry]
    print(var.find("128"), var.find("wool"))
queue = {}
ask = input("hi:")
modify_name(ask)
renaming(queue, 1)

# First go to the directory
os.chdir(ask)

# Print current working directory
print ("Current working dir : %s" % os.getcwd())

# Now open a directory "/tmp"
fd = os.open( "/tmp", os.O_RDONLY )

# Use os.fchdir() method to change the dir
os.fchdir(fd)

# Print current working directory
print ("Current working dir : %s" % os.getcwd())



#Renaming process
#$ ls
#$ python
#>>> import os
#>>> for filename in os.listdir("."):
#...  if filename.endswith("cheese_"):
#...    os.rename(filename, filename[7:])
#...
#>>>
#$ ls
#cheese_type.bar  cheese_type.foo



#invoking FFMpeg
#import os
#import subprocess
#os.chdir('C://Users/Alex/')
#subprocess.call(['ffmpeg', '-i', 'picture%d0.png', 'output.avi'])
#subprocess.call(['ffmpeg', '-i', 'output.avi', '-t', '5', 'out.gif'])
