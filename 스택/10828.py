import sys

SIZE = int(input())
stack = []
where = -1

for i in range(SIZE) :
  instruction = sys.stdin.readline().split()
  if instruction[0] == 'top' :
    if (where == -1) :
      print("-1")
    else :
      print(stack[where])
  elif instruction[0] == 'size' :
    print(len(stack))
  elif instruction[0] == 'empty' :
    if (where == -1) :
      print("1")
    else :
      print("0")
  elif instruction[0] == 'pop' :
    if (where == -1) :
      print("-1")
    else :
      data = stack[where]
      stack.pop()
      where -= 1
      print(data)
  elif instruction[0] == 'push' :
    where += 1
    stack.append(instruction[1])
