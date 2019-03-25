import os, sys
def modify_name(pname):
    base = os.path.basename(pname)
    list = os.path.splitext(base)
    no_ext = list[0]
    s1 = no_ext.split(".")
    s2 = "".join(s1)
    s3 = s2.split("(")
    print(s3)
    if "128AAC)" in s3:
        s3.remove("128AAC)")
        print(s3)
    join = "".join(s3)
    print(join + list[1])
#ask for input in which the files are located
ask = input("Directory in which the files are in:")
modify_name(ask)

#test path: usr/local/b.i.n(128AAC).aac
os.chdir(ask)

split =[]

os.chdir(ask)
filenames = [f for f in listdir(mypath) if isfile(join(mypath, f))]
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
