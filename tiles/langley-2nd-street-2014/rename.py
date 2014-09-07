import re, os
rx = re.compile('^\./([0-9]*)/([0-9]*)/([0-9]*)\.([aA-zZ]*)$')
for r,d,f in os.walk("."):
    for files in f:
        oriPath = os.path.join(r,files)  
        reMatch = rx.match(oriPath)
        if reMatch:
            z = reMatch.group(1)
            x = reMatch.group(2)
            y = reMatch.group(3)
            fileExt = reMatch.group(4)
            newY = (1<<int(z)) - int(y) - 1
            print "rename: "+oriPath+" -> " + "./"+z+"/"+x+"/"+str(newY)+"."+fileExt
            os.rename(oriPath,"./"+z+"/"+x+"/"+str(newY)+"."+fileExt)
