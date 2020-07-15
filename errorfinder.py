import os
import re

errorfiles = []

def recursiveWalk(path,parent):
    #is a path
    if(os.path.isdir(os.path.join(parent,path))):
        subs = os.listdir(os.path.join(parent,path))
        #empty folder
        if(len(subs)==0):
            print("empty "+parent+"/"+path)
        else:
            print("in")
            for s in subs:
                recursiveWalk(s,os.path.join(parent,path))
    #is a file
    else:
        global files
        errorfiles.append(os.path.join(parent,path))

recursiveWalk("tutorial/indigits/logdir","")

errors = []

for file in errorfiles:
    f = open(file,"r")
    lines = f.read().split("\n")
    for l in lines:
        if(l!=""):
            r = re.match("ERROR: \"baum_welch.c\", line (.*): (.*)/(.*) ignored",l)
            if(r!=None):
                errors.append(r.group(3))            


errors = list(set(errors))
print(errors)




