def same(a, b):
  if not (len(a) == len(b)):
    return False
  for i in range(len(a)):
    if not (a[i] == b[i]):
      return False
  return True

def invert(arr):
  lenf = len(arr) -1
  pop = []
  a = lenf
  for i in range(len(arr)):
    pop.append(arr[a])
    a = a -1
  return pop
# main
a = []
run = 1
b = ""
while run == 1:
  b = input("(hint type end to end) word :")
  if b == "end":
    run = 0
  else:
    a.append(b)
c = a
c = invert(c)
rlt = same(a, c)
if (rlt):
  print("same !")
else:
  print("not same")
#main
