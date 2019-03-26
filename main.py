import os, sys, shutil, fnmatch
#from os import listdir
#from os.path import isfile, join
def modify_name(pname, liist, w_dot):
    num = 0
    print("Extracting filename...")
    base = os.path.basename(pname)
    liist = os.path.splitext(base)
    no_ext = liist[num]
    s1 = no_ext.split(".")
    s2 = "".join(s1)
    w_dot.append(s2)
    w_dot.append(liist[num])
    num += 2
    
def remove_text_inside_brackets(text, brackets="()[]"):
    print("Removing brackets...")
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

def remove2(x, lost, altar):
    nume = 1
    altar.append((x[1:-1] + lost[nume]))
    nume += 2


    
print("Program start")
list = []

no_dot = []

alter = []

#ask for input in which the files are located

ask = input("File path:")
x = []
for file in os.listdir(ask):
    if fnmatch.fnmatch(file, '*.m4a'):
        x.append(file)
print(x)
for f in x:
    if 1 == 1:
        num = 0
        try:
            f_base = os.path.basename(f)
            modify_name(f, list, no_dot)
            print("modify_name() executed" + f)
            e = repr(remove_text_inside_brackets(no_dot[0]))
            remove2(e, no_dot, alter)
            print("remove2 executed" + f)
            os.rename(f_base, alter[num])
            print("osrename executed" + f)
            except
                continue
        num += 1
        print("Rename successful!" + f)

