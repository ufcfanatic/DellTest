# Description - This program will use a class to find the largest element and then transpose the Element
# input - FileName
# output - Largest word and transposed word

class FindLarge():
 alist = []
 fname = ""
 temp = ""

 # description - constructor 
 # input - filename
 # output - none
 def __init__(self,file):
    # init our file in the class
    self.fname = file

 # description - creates in memory list 
 # input - none 
 # output - ret 0 for SUCCESS and -1 for FILE ERROR -2 for List ERROR
 def createList(self):
  try:
   with open(file, "r") as self.fname:
     for line in self.fname:
       #strip <CR> before adding to list
       self.temp = line.strip('\n')
       if self.temp !='' :
        self.alist.append(self.temp) 
   if not self.alist:
    return -2
   else:
    return 0
  except:
   print("IO error - file not found ", file)
   return -1
   
 # description - Finds largest string in list and transposes this string 
 # input - none 
 # output - word and transpose if ok else error
 def findAndTranspose(self):
    #print('alist is ', self.alist) 
    # find the largest word in our List
    self.aword = max(self.alist, key=len) 
    self.transpose = self.aword[::-1]
    return self.aword , self.transpose


file = input('Enter file name ')
t = FindLarge(file)
ret = t.createList()
# Validate the list was created successfully
if ret == 0:
 word, transpose = t.findAndTranspose()
 print ('largest word is ' , word)
 print('largest word transposed is ' , transpose)
elif ret == -1:
 print ("File ERROR - File not found " , file)
elif ret == -2:
 print ("List ERROR -  please check file data for " ,file)

