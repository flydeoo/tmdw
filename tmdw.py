#!/usr/bin/env python
# coding: utf-8

# In[10]:

# import regular expression
import re 

#import numpy
import numpy as np

#import matplotlib 
import matplotlib.pyplot as plt

xpoints = np.array([])
ypoints = np.array([])

from collections import OrderedDict
file=""
fileLoc  = input("Please Enter .srt or txt file Location")
for char in fileLoc:
    if char != "\"":
        file += char
        
wiseOption = input("would you like to remove some known English words such as the, a, and ... ? (y|n)")
wise = ["number","can","will","should","going","on","who","what","it","the","and","or","a","an","of","so","am","is","are","to","so","So","that","be","you","we","have","in","this","for","as"]

wMarks = [",",":",".","\n",";"]

  

string =""
f = open(file, "r")
    
for c in f: 
  string += c


if ".srt" in file:
    x = re.sub("\d\n\d.*?--> \d.*?\n","",string)
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
          if wiseOption == 'y':
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
res = OrderedDict(sorted(thisdict.items(), key=lambda kv: kv[1], reverse=True))



k = list(res.keys())[0:6]
v = list(res.values())[0:6]
x_axis = np.append(xpoints,k)
y_axis = np.append(ypoints,v)
plt.plot(x_axis,y_axis)
plt.show()




fres=""
for k,v in res.items():
    fres = str(k) + " : " + str(v) + " \n"
    f.write(fres)


f.write("\n")
f.close()
print("done! check the result on result.txt")


# In[ ]:




