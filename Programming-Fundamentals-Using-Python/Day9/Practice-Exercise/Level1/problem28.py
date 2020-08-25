#PF-Tryout
def sing_99_bottles():
   for i in range(99,0,-1):
       print("{a} bottles of beer on the wall, {a} bottles of beer.\nTake one down, pass it around, {b} bottles of beer on the wall.\n".format(a=i,b=i-1))

sing_99_bottles()
