from turtle import *

setup(1000, 1000)

goto(-150,0)

def kochA(l, n):
   if n == 2:
       speed(0)

       forward(l)
       left(90)
       forward(l)
       right(90)
       forward(l)
       right(90)
       forward(l)
       left(90)
       forward(l)
   else:
       kochA(l, n-1)
       left(90)
       kochA(l, n-1)
       right(90) 
       kochA(l, n-1)
       right(90) 
       kochA(l, n-1)
       left(90) 
       kochA(l, n-1)
 

def kochB(l, n):
   if n == 2:
       speed(10)
       forward(l)
       left(90)
       forward(l)
       right(90)
       forward(l)
       right(90)
       forward(2*l)
       left(90)
       forward(l)
       left(90)
       forward(l)
       right(90)
       forward(l)

   else:
       kochB(l, n-1)
       left(90)
       kochB(l, n-1)
       right(90) 
       kochB(l, n-1)
       right(90) 
       kochB(l, n-1)
       left(90) 
       kochB(l, n-1)
       left(90) 
       kochB(l, n-1)
       right(90) 
       kochB(l, n-1)
       


def kochC(l, n):
   if n == 2:
      speed(0)
      forward(l)
      right(120)
      forward(l)
      left(120)
      forward(l)

   else:
      kochC(l, n-1)
      right(120)
      kochC(l, n-1)
      left(120)
      kochC(l, n-1)



kochC(5, 7)
kochA(5, 5)
kochB(5, 4)












exitonclick()
