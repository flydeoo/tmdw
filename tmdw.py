

# %%
#-*- coding: utf-8 -*-

#import sys to get args and opts from user
import os
# from readline import insert_text
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
i_flag = False
wise = []
inTextList = []
wise_dict = open("dictEn.txt","r")

def chkFile(file):
    return os.path.isfile(file)


def getInput():

  global wiseOption, g_flag, fileLoc, i_flag

  opts = [opt for opt in sys.argv[1:] if opt.startswith("-")]
  args = [arg for arg in sys.argv[1:] if not arg.startswith("-")]



  if "-f" in opts:
    fileIndex = sys.argv.index("-f") + 1
    fileLoc = sys.argv[fileIndex]
    fileStat = chkFile(fileLoc)
    if fileStat == False:
            print("=> tmdw : Error in loading file")
            quit()

    if "-g" in opts:
      g_flag = True

    if "-v" in opts:
      i_flag = True

    
    if "-w" in opts:
      wiseOption = True    

  elif "-f" not in opts:
      #raise SystemExit(f"Usage: {sys.argv[0]} (-f) <arguments>...")
      print("=> tmdw : Seems like to forget -f \"path/to/fileLocation\" switch")
      quit()

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
    # print(line)



wMarks = [",",":",".","\n",";","?","-","!","\"","[","]","(",")","…","■"]

for n in range(0,10):
  wMarks.append(str(n))

  


  
def counter(string):
  global wMarks
  
  lineList = string.splitlines()
  thisdict = {}
  global inTextList

  for line in lineList:

    # space is tigger to do some function, so we add space to last word
    # to proccess the last item too
    string = line
    typestr = type(string)
    string += ' '

    mem = ""

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
              if i_flag:
                
                sp_line = line
                sp_mem = "\"" + mem + "\""
                sp_line = sp_line.lower()
                sp_line = sp_line.replace(mem,sp_mem)
                inTextList.append(sp_line)
               
                
            else:
              if wiseOption == True:
                if mem!= "" and mem not in wise :  
                  thisdict[mem]= 1
                  if i_flag:
                    
                    sp_line = line
                    sp_mem = "\"" + mem + "\""
                    # sp_mem = " wow "
                    sp_line = sp_line.lower()
                    sp_line = sp_line.replace(mem,sp_mem)
                    inTextList.append(sp_line)                  


              elif wiseOption == False:
                if mem!= "" :
                  thisdict[mem]= 1

                  if i_flag:
                    
                    sp_line = line
                    sp_line = sp_line.lower()
                    sp_mem = "\"" + mem + "\""
                    sp_line = sp_line.replace(mem,sp_mem)
                    inTextList.append(sp_line)
                        
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
  
  if i_flag:
    for item in inTextList:
      f.write(item)
      f.write("\n")

  f.close()
  print("=> tmdw : done! check the result on result.txt")





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

