from turtle import * 

setup(500, 500)

def koch2(l):
   forward(l)
   left(60)
   forward(l)
   right(120)
   forward(l)
   left(60)
   forward(l)
   
   
def koch3(l):
   koch2(l)
   left(60)
   koch2(l)
   right(120)
   koch2(l)
   left(60)
   koch2(l)
   
def koch4(l):
   koch3(l)
   left(60)
   koch3(l)
   right(120)
   koch3(l)
   left(60)
   koch3(l)

def kochX(l, n):
   if n == 2: 
      forward(l)
      left(60)
      forward(l)
      right(120)
      forward(l)
      left(60)
      forward(l)
      speed(10)   
   else:
      kochX(l, n-1)
      left(60)
      kochX(l, n-1)
      right(120)
      kochX(l, n-1)
      left(60)
      kochX(l, n-1)


kochX(5, 5)

exitonclick()




