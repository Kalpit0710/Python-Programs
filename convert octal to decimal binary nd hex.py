def oct2others(n):
      print("Passed octal number:",n)
      numstring=str(n)
      decnum=int(numstring,8)
      print("number in decimal:",decnum)
      print("Number in binary:",bin(decnum))
      print("Number in hexadecimal:",hex(decnum))

num=int(input("Enter an octal number:"))
oct2others(num)