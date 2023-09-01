# this program run combinate divide and parted my/your main prog
# without from/import lines
# part files xxxxxx.part1.py naming rule and combine to part0

# part99 is max!

import os
import copy
import glob
import re
import subprocess


# file listup
dparts = glob.glob("*.part[0-9].py")
# :/
dparts.extend(glob.glob("*.part[0-9][0-9].py"))

print(dparts)


lc = []
for i in range(0,len(dparts),1):

    filename = dparts[i]

    with open(f'{filename}','r') as f:
        l = f.readlines()
        print(l)
    
    if i == 0:
        lc=copy.deepcopy(l)
    
    # find & remove [import] and [from] lines part1+
    elif i > 0:
        for i in range(len(l)):
            ptrn = re.compile(r"(^(?=.*(from\s\S|import\s\S))^(?!.*\"\"\").*$)")
            result = ptrn.search(l[i])
            lc.append(l[i])
            if result != None:
                pres = result.group()
                print("search = {}".format(pres))
                print("finder get line = {}".format(i))
                lc.pop()

print(lc)

mkdpath = "combedmain.py"
if os.path.exists(mkdpath) == True:
    os.remove(mkdpath)

if os.path.exists(mkdpath) == False:
    with open("combedmain.py", "w") as opfile:
        opfile.write("".join(lc))


print("program endline")

"""
# run created combinate file
subprocess.run(['python3', 'combedmain.py'])
"""
