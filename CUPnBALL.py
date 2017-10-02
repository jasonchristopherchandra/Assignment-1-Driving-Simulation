#Initial Position where Ball is 1 and located in first index
position = [1, 0, 0]

def moveA():
    temp = position[1]
    position[1] = position[0]
    position[0] = temp

def moveB():
    temp = position[2]
    position[2] = position[1]
    position[1] = temp

def moveC():
    temp = position[2]
    position[2] = position[0]
    position[0] = temp

def findBall():
    i = 0;
    while (i<3)  :
          if  (position[i]==1):
              return i+1
          else :
              i = i + 1

command = input("Enter command A, B, C : ")
segment = list(command.lower())

i = 0
while (i < len(segment)):
    if    segment[i]=='a':
          moveA()
    elif  segment[i]=='b':
          moveB()
    elif  segment[i]=='c':
          moveC()
    else  :
          print("Invalid Function. Program is stopping")
          break
    i = i + 1

if  i==(len(segment))  :
    print("Ball Position = " + str(findBall()))
