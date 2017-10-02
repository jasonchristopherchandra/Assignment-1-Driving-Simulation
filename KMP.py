name = input("Enter Fullname Separated With '-'")

nameSegment = name.split('-', 3)

#TO PRINT FIRST INDEX FROM ARRAY STRING
#print(nameSegment[0][:1])

printString = ""
for i in range(0, len(nameSegment)) :
  printString = printString + nameSegment[i][:1]

print(printString)
