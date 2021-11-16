#!/usr/bin/env python
# coding: utf-8

# %%
import sys

opts = [opt for opt in sys.argv[1:] if opt.startswith("-")]
args = [arg for arg in sys.argv[1:] if not arg.startswith("-")]
fileLoc= ""
file=""
wiseOption = False

if "-w" in opts:
  wiseOption = True  

if "-f" in opts:
  fileLoc = args
else:
    #raise SystemExit(f"Usage: {sys.argv[0]} (-f) <arguments>...")
    print("welcome to tmdw\n => Please Enter File location (e.g \".file/the_movie.srt\")")
    fileLoc = input()



# import regular expression
import re 
# res.index

#import numpy
import numpy as np

#import matplotlib 
import matplotlib.pyplot as plt

xpoints = np.array([])
ypoints = np.array([])



#fileLoc  = input("Please Enter .srt or txt file Location")
for char in fileLoc:
    if char != "\"":
        file += char


wise = ["get","was","she","he","with","all","your","don't","do","down","up","my","me","I","i","that","the","to","you","number","can","will","should","going","on","who","what","it","the","and","or","a","an","of","so","am","is","are","to","so","So","that","be","you","we","have","in","this","for","as"]

wMarks = [",",":",".","\n",";"]

  

string =""
f = open(file, "r")
    
for c in f: 
  string += c


if ".srt" in file:
    x = re.sub("\d.*?\n\d.*?--> \d.*?\n","",string)
    string = x
#str = "hello from erfan say hello to  your familly"
       

mem = ""
thisdict = {}

for c in string:
    
   # from every char you read, chnage ban items to space
   if c in wMarks:
     c = " "
    
   # from every char you read, if char is not space, store it 
   if c != " ":
     mem += c
    
   # final stage, save mem to array with space trigger
   if c == " ":    
        if mem in thisdict.keys():
            thisdict[mem]+= 1
            
        else:
          if wiseOption == True:
            if mem!= "" and mem not in wise :  
             thisdict[mem]= 1
          else:
            if mem!= "" :
              thisdict[mem]= 1

                
        #whether it's the world we have in array or not, clear mem        
        mem =""
    
    


f = open("result.txt","a")

f.write(file)
f.write("\n ----------------------------------------- \n")

res = list(thisdict.items())
res.sort(key= lambda x : x[1], reverse=True)
res = dict(res)



k = list(res.keys())[0:6]
v = list(res.values())[0:6]
x_axis = np.append(xpoints,k)
y_axis = np.append(ypoints,v)
plt.plot(x_axis,y_axis)
plt.xlabel('word')
plt.ylabel('count')
plt.show()




fres=""
for k,v in res.items():
    fres = str(k) + " : " + str(v) + " \n"
    f.write(fres)


f.write("\n")
f.close()
print("done! check the result on result.txt")






