myDict={
      "keys":"values",
      "name":"akash sharma",
      "email":"akash8923@gmail.com"
}
print(type(myDict))
print(myDict)

for keys in myDict:
       print(myDict[keys])
       
print(myDict.get("email"))
myDict["name"]="abhishek"
print(myDict)