from SmellDetector import Constants as CONSTS
import os, time, datetime

def myPrint(msg):
    if(CONSTS.DEBUG_ON):
        print(msg)

def reportSmell(outputFile, fileName, smellName, reason):
    outputFile.write(smellName + " at " + reason + " in file " + fileName + "\n")
    myPrint(smellName + " at " + reason + " in file " + fileName + "\n")

def intersection(list1, list2):
    return list(set(list1) & set(list2))

def summation(list1, list2):
    return list(set(list1) | set(list2))
    
    
    
def dumpStrToFile(fileParam, strToDump):
   fileToWrite = open( fileParam, 'w')
   fileToWrite.write(strToDump )
   fileToWrite.close()
   return str(os.stat(fileParam).st_size)    
    


def giveTimeStamp():
  tsObj = time.time()
  strToret = datetime.datetime.fromtimestamp(tsObj).strftime('%Y-%m-%d %H:%M:%S')
  return strToret

    