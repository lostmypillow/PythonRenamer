import os, sys, subsystem
def modify_name(pname):
    base = os.path.basename(pname)
    list = os.path.splitext(base)
    no_ext = list[0]
    no_ext.replace(" ", "/")
    no_ext.replace("(", " ")
    print (no_ext)
    
def renaming(dict, entry):
    var = dict[entry]
    splitvar = var.split(".")
    split.append(splitvar)
ask = input("Directory in which the files are in:")
os.chdir(ask)

split =[]
ask = input("Directory in which the files are in:")
os.chdir(ask)
filenames = [f for f in listdir(mypath) if isfile(join(mypath, f))]
#for x in filenames:
modify_name(ask)
renaming(queue, 1)


#test path: usr/local/bin(128AAC).aac

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

input_func = None 
try: input_func = raw_input 
except NameError: input_func = input 
  while True: parameters = input_func("enter symbol to be replaced:") 
    p_cmd.replace("'x'", parameters) 
    print(p_cmd) 
    if parameters == "Stop": 
        break 
subprocess.call('C:\Windows\System32\powershell.exe', 'Get-ChildItem | Rename-Item -NewName {$_.name -replace ‘.’,’’ }', shell=True) subprocess.call('C:\Windows\System32\powershell.exe', 'Get-ChildItem | Rename-Item -NewName {$_.name -replace ‘mkv’,x }', shell=True) subprocess.call('C:\Windows\System32\powershell.exe', 'Get-ChildItem | Rename-Item -NewName {$_.name -replace ‘(’,’’ }', shell=True) 
subprocess.call('C:\Windows\System32\powershell.exe', 'Get-ChildItem | Rename-Item -NewName {$_.name -replace ‘)’,’’ }', shell=True)

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
