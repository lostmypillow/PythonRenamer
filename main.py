import os, sys
def modify_name(pname, liist, w_dot):
    base = os.path.basename(pname)
    liist = os.path.splitext(base)
    no_ext = liist[0]
    s1 = no_ext.split(".")
    s2 = "".join(s1)
    w_dot.append(s2)
    w_dot.append(liist[1])
def remove_text_inside_brackets(text, brackets="()[]"):
    count = [0] * (len(brackets) // 2) # count open/close brackets
    saved_chars = []
    for character in text:
        for i, b in enumerate(brackets):
            if character == b: # found bracket
                kind, is_close = divmod(i, 2)
                count[kind] += (-1)**is_close # `+1`: open, `-1`: close
                if count[kind] < 0: # unbalanced bracket
                    count[kind] = 0  # keep it
                else:  # found bracket to remove
                    break
        else: # character is not a [balanced] bracket
            if not any(count): # outside brackets
                saved_chars.append(character)
    return ''.join(saved_chars)
def remove2(x, lost):
    print(x[1:-1] + lost[1])
   

list = []
no_dot = []
#ask for input in which the files are located
ask = input("Directory in which the files are in:")
modify_name(ask, list, no_dot)
e =repr(remove_text_inside_brackets(no_dot[0]))
remove2(e, no_dot)


#test path: usr/local/b.i.n(128AAC).aac
os.chdir(ask)

split =[]

os.chdir(ask)
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
