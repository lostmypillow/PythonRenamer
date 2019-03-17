import os
def modify_name(pname):
    base = os.path.basename(pname)
    list = os.path.splitext(base)
    modifier = list[0]
    print(modifier)
ask = input("hi:")
modify_name(ask)
#$ ls
#$ python
#>>> import os
#>>> for filename in os.listdir("."):
#...  if filename.startswith("cheese_"):
#...    os.rename(filename, filename[7:])
#...
#>>>
#$ ls
#cheese_type.bar  cheese_type.foo