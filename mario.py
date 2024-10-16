
def main():
    hight = get_positive()
    for i in range(hight):
          print("#")



def get_positive():
     while True:
          n = int(input("n: "))
          if n >0:
               break
     return n

for i in range(4):
     print("?",end="")

print("TOT " *2)
main()

for A in range(3):
     for R in range(3):
      print("?", end="")
     print()

for T in range(4):
     print("RADWA  " *4)
