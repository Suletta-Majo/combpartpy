# this program run combinate divide and parted my/your main prog
# without from/import lines
# part files xxxxxx.part1.py naming and combine to part0

# part99 is max!

import glob
import re

dparts = glob.glob("*.part[0-9].py")
# :/
dparts.extend(glob.glob("*.part[0-9][0-9].py"))

print(dparts)

for i in range(1,len(dparts),1):

    filename = dparts[i]

    with open(f'{filename}','r') as f:
        l = f.readlines()
        print(l)

ptrn = re.compile(r"(^import\s\S)")

result = ptrn.search(l[2])
pres = result.group()

print("search = {}".format(pres))
