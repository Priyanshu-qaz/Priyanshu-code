# easy python code to make a menu card using python programming language
# menu card of bihari gujrati and chinese 
print("1=GUJRATI")
print("2=BIHARI")
print("3=chinese")

a=int(input("WHICH TYPE OF FOOD DO YOU WANT to eat"))
if a==1:
  print("how many plate do you want eat write in the front of list")
  b=int(input("dhokla = rs 100:: "))
  c=int(input("fafda jalebi = rs 200::"))
  d=int(input("poha = rs 100::"))
  x=(b*100)
  y=(c*200)
  z=(d*100)
  bill=x+y+z
  print("total bill is ",bill)
  if bill>=400:
    w=int(input("congratulation you got 10 % discount press 1 for get it or if you dont want press any other key"))
    print(w)
    if w==1:
      print("your discount bill is ::",(bill-(10*100)/100))
    else:
      print("ok your food will be ready in 5 minute")
  else:
    print("ok your food will be ready in 5 minute")

# now here i start for bihar food

elif a==2:
  print("how many plate do you want eat write in the front of list")
  b=int(input("rice dal = rs 50:: "))
  c=int(input("litti chokha = rs 200::"))
  d=int(input("pakaudi = rs 100::"))
  x=(b*100)
  y=(c*200)
  z=(d*100)
  bill=x+y+z
  print("total bill is ",bill)
  if bill>=400:
    w=int(input("congratulation you got 10 % discount press 1 for get it"))
    print(w)
    if w==1:
      print("your discount bill is ::",(bill-(10*100)/100))
    else:
      print("ok your food will be ready in 5 minute")
  else:
    print("ok your food will be ready in 5 minute")

# now here i start for chinese food
elif a==2:
  print("how many plate do you want eat write in the front of list")
  b=int(input("chowmin= rs 50:: "))
  c=int(input("dosha = rs 200::"))
  d=int(input("paka = rs 100::"))
  x=(b*100)
  y=(c*200)
  z=(d*100)
  bill=x+y+z
  print("total bill is ",bill)
  if bill>=400:
    w=int(input("congratulation you got 10 % discount press 1 for get it"))
    print(w)
    if w==1:
      print("your discount bill is ::",(bill-(10*100)/100))
    else:
      print("ok your food will be ready in 5 minute")
  else:
    print("ok your food will be ready in 5 minute")
