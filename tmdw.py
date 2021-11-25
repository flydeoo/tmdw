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



wise = []
wise_dict = open("dictEn.txt","r")

for line in wise_dict:
  if '/' not in line:
    l = len(line) - 1
    line = line[0:l]
    wise.append(line)



wMarks = [",",":",".","\n",";"]

  
string =""
f = open(file, "r")
    
for line in f: 
  string += line


if ".srt" in file:
    x = re.sub("\d.*?\n\d.*?--> \d.*?\n","",string)
    string = x

       

mem = ""
thisdict = {}

for c in string:
   # change every char to lower one, so we don't check The,THe and THE
   c = c.lower() 

   # from every char you read, chanage ban items to space
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






