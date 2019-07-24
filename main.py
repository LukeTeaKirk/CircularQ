import re
from array import array 
Queue = array('i')
Start = 1
End = 1
def add(value):
  global End
  global Queue
  if End < 7:
    Queue[End] = value
    End = End + 1
  else:
    print("Can not add data")
  return
  
def remove():
  global Queue
  global End
  if(End > 0):
    Queue[End] = None
    
    End = End - 1
  return

def PrintQueue():
  global Queue
  string = ""
  for x in Queue:
    string = string + Queue[x] + ","
  print(string)
  return

def EnterCommand():
  x = input("Enter Command: ")
  if (re.match(r"REMOVE", x)):
    print("remove")
    remove()
    EnterCommand()
  elif (x == "EXIT"):
    print("exit")
    PrintQueue()
  elif (re.match(r"ADD[^@]", x)): 
    print("add")
    add(int(re.search(r'\d+', x).group()))
    EnterCommand()
  
  return
EnterCommand()
   
   
