import os

class ArrayStack:

  def __init__(self):
    self._data = []

  def __len__(self):
    return len(self._data)

  def is_empty(self):
    return len(self._data) == 0

  def push(self, e):
    self._data.append(e)

  def top(self):
    if self.is_empty():
      return False
    return self._data[-1]

  def pop(self):
    if self.is_empty():
      return False
    return self._data.pop()

  def printStack(self):
    print(self._data)

S1 = ArrayStack()
source = open("source.c","r")
target = open("target.c","w")
sayac, text = 0, " ";
while(text != "}"):
    text = source.readline()
    if text == "{\n":
        S1.push("\t" * sayac + text)
        target.write(S1.top())
        sayac += 1
    elif text == "}\n":
        sayac -= 1
        S1.push("\t" * sayac + text)
        target.write(S1.top())
    elif text == "}":
        S1.push(text)
        target.write(S1.top())
    else:
        S1.push("\t" * sayac + text)
        target.write(S1.top())
source.close()
target.close()
S1.printStack()

#def duzenle(bosluk):
# list = []
# if os.path.exists("source.txt"):
#    source = open("source.txt", "r")
#    target = open("target.txt", "a")
#    for x in source:
#        list.append(x)
#    sayac, boslukSayac = 0, 0
#    while sayac != len(list) - 1:       
#        spaceCount1, spaceCount2 = 0, 0
#        while list[sayac][spaceCount1] == ' ':
#           spaceCount1 += 1
#        while list[sayac + 1][spaceCount2] == ' ':
#           spaceCount2 += 1
#        if spaceCount1 > spaceCount2:
#            temp = " " * spaceCount2 + list[sayac].lstrip()
#            list[sayac] = temp
#        elif spaceCount2 > spaceCount1:
#            temp = " " * spaceCount1 + list[sayac + 1].lstrip()
#            list[sayac + 1] = temp
#        if list[sayac][-2] == "{":          
#           for i in range(sayac, len(list) - 1):
#             temp = " " * bosluk + list[i + 1]
#             list[i + 1] = temp
#           target.write(list[sayac])
#           boslukSayac += bosluk
#        elif list[sayac][-2] == "}":                     
#            for k in range(sayac, len(list) - 1):
#             temp = " " * (boslukSayac - bosluk) + list[k].lstrip()
#             list[k] = temp
#            target.write(list[sayac])
#            boslukSayac -= bosluk
#        else:
#           target.write(list[sayac])
#        sayac += 1
#    target.write("}")
#    source.close()
#    target.close()
#    print("codes in the source have been put right")
# else:
#    print("the source file context does not exist")
#duzenle(2)



