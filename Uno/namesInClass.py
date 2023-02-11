currentName = ""
namesInClass = []
notTheLetterC = True
while notTheLetterC:
  currentName = input("Whats your name (c to exit): ")
  if currentName.lower() == "c":
    print(namesInClass)
    notTheLetterC = False
  else:
    namesInClass.append(currentName)
