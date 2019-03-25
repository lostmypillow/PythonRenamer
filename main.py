import os, sys, shutil
#from os import listdir
#from os.path import isfile, join
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

def remove2(x, lost, altar):
    altar.append(x[1:-1] + lost[1])

def main(filenamee, newname):
	# make a duplicate of an existing file
    if path.exists(filenamee):
	# get the path to the file in the current directory
        src = path.realpath(filenamee);
		
	# rename the original file
        os.rename(filenamee,newname)
    

list = []

no_dot = []

alter = []

#ask for input in which the files are located
ask = input("File path")
ask_base = os.path.basename(ask)

#onlyfiles = [f for f in listdir(ask) if isfile(join(ask, f))]
#print(onlyfiles)

modify_name(ask, list, no_dot)
e =repr(remove_text_inside_brackets(no_dot[0]))
remove2(e, no_dot, alter)

		
if __name__ == "__main__":
    main(ask_base, alter[0])



#test path: usr/local/b.i.n(128AAC).aac

