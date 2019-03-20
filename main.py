import os
def modify_name(pname):
    base = os.path.basename(pname)
    list = os.path.splitext(base)
    modifier = list[0]
    print(modifier)
ask = input("hi:")
modify_name(ask)



#Renaming process
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



#invoking FFMpeg
#import os
#import subprocess
#os.chdir('C://Users/Alex/')
#subprocess.call(['ffmpeg', '-i', 'picture%d0.png', 'output.avi'])
#subprocess.call(['ffmpeg', '-i', 'output.avi', '-t', '5', 'out.gif'])
