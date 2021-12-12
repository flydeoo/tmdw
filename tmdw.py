#!/usr/bin/env python
# coding: utf-8

# %%
#import sys to get args and opts from user
from os import makedirs
import sys

# import regular expression
import re 

#import numpy
import numpy as np

#import matplotlib 
import matplotlib.pyplot as plt

# init 
fileLoc= ""
wiseOption = False
g_flag = False
wise = []
wise_dict = open("dictEn.txt","r")

def getInput():

  global wiseOption, g_flag, fileLoc

  opts = [opt for opt in sys.argv[1:] if opt.startswith("-")]
  args = [arg for arg in sys.argv[1:] if not arg.startswith("-")]


  if "-w" in opts:
    wiseOption = True  

  if "-f" in opts:
    fileLoc = args

  if "-g" in opts:
    g_flag = True

  elif "-f" not in opts:
      #raise SystemExit(f"Usage: {sys.argv[0]} (-f) <arguments>...")
      print("welcome to tmdw\n => Please Enter File location (e.g \".file/the_movie.srt\")")
      fileLoc = input()

  return fileLoc


def file_reader(fileaddr):

  file=""
  # filter " from file location
  for char in fileaddr:
      if char != "\"":
          file += char

  
  string =""
  f = open(file, "r")
      
  for line in f: 
    string += line


  if ".srt" in file:
      x = re.sub("\d.*?\n\d.*?--> \d.*?\n","",string)
      string = x

  return string, file





for line in wise_dict:
  if '/' not in line:
    l = len(line) - 1
    line = line[0:l]
    wise.append(line)



wMarks = [",",":",".","\n",";"]

  


  
def counter(string):
  # space is tigger to do some function, so we add space to last word
  # to proccess the last item too
  string += ' '

  mem = ""
  thisdict = {}

  for c in string:
    # change every char to lower one, so we don't check The,THe and THE
    c = c.lower() 

    # from every char you read, change ban items to space
    if c in wMarks:
      c = " "
      
    # from every char you read, if char is not space, store it 
    if c != " ":
      mem+= c
      
    # final stage, save mem to array with space trigger
    if c == " ":    
          if mem in thisdict.keys():
              thisdict[mem]+= 1
              
          else:
            if wiseOption == True:
              if mem!= "" and mem not in wise :  
                thisdict[mem]= 1
            elif wiseOption == False:
              if mem!= "" :
                thisdict[mem]= 1

                  
          #whether it's the world we have in array or not, clear mem        
          mem =""
      
  return thisdict    



# make inverse dict 
def DictInv(resDict):
  res = list(resDict.items())
  res.sort(key= lambda x : x[1], reverse=True)
  res = dict(res)
  
  return res




def output(file,res):

  f = open("result.txt","a")

  f.write(file)
  f.write("\n ----------------------------------------- \n")

  fres=""
  for k,v in res.items():
      fres = str(k) + " : " + str(v) + " \n"
      f.write(fres)

  f.write("\n")
  f.close()
  print("done! check the result on result.txt")





def gPlot(res):
  
  k = list(res.keys())[0:6]
  v = list(res.values())[0:6]
  # x,y points for plot
  xpoints = np.array([])
  ypoints = np.array([])

  x_axis = np.append(xpoints,k)
  y_axis = np.append(ypoints,v)
  plt.plot(x_axis,y_axis)
  plt.xlabel('word')
  plt.ylabel('count')
  plt.show()







def main():
  global g_flag, fileLoc

  fileLoc = getInput()

  # string : the whole text  
  string, file_address = file_reader(fileLoc)

  # resDict : counter make a dictionary of words and it's counts
  resDict = counter(string)

  # invD : DictInv make a H to L sort dictionary
  invD = DictInv(resDict)

  output(file_address,invD)
  
  if g_flag == True:
    gPlot(invD)


if __name__ == "__main__":
  main()

