import math
import turtle
import numpy
import numpy as np




P1=np.array([[0,-10,0,0],[-10,0,0,0],[0,0,-8,0],[0,0,0,-1]])
P2=np.array([[-10,0,0,0],[0,-10,0,0],[0,0,-1,0],[0,0,0,-4]])
# P1=np.array([[8,2],[12,-5]])
# P2=np.array([[9,11],[1,-5]])

def Draw_Ext_Form2(P1:numpy.ndarray,P2:numpy.ndarray,WhichFirst:str):
   assert P1.shape == P2.shape, "arrays dimensions not same "
   r, c = P1.shape

   if WhichFirst == "P2":
      P1_T = P2.T
      P2_T = P1.T
      P1_str='P2'
      P2_str='P1'
   else:
      P1_T = P1
      P2_T = P2
      P1_str = 'P1'
      P2_str = 'P2'




   # Creating Extensive for graphices

   wn = turtle.Screen()



   p1 = turtle.Turtle('circle')
   p1.pen(pencolor='red',pensize=5)
   p1.color('red')
   p1.shapesize(0.1,0.1,0.1)
   p1.penup()
   p1.goto(0,200)
   p1.pendown()
   p1.write(P1_str)

   # legends
   p3=p1.clone()
   p3.pen(pencolor='green', pensize=5)
   p3.color('green')
   p3.shapesize(0.1, 0.1, 0.1)
   p3.penup()
   p3.goto(-300, 200)
   p3.pendown()
   p3.forward(10)
   p3.write('nash equilibrium')




   def clones(p1, n, l):
      if (n == 0):
         return l
      else:
         p = p1.clone()
         l.append(p)
         clones(p,n-1,l)


   #if player 1 start first n=r-1 else n=c-1

   n=r-1
   p1_clones=[p1]
   clones(p1,n,p1_clones)

   p2 = p1.clone()
   p2.pen(pencolor='blue', pensize=5)
   p2.color('red')
   p2.shapesize(0.1, 0.1, 0.1)
   n=c -1
   p2_clones = [p2]
   clones(p1, n, p1_clones)





   dx=200;
   b=-50;

   n=c-1

   p1_x_coord=np.linspace(-dx/2-100,100+dx/2,r)

   p2_max_row = []

   p1_max_when_p2_max=[]


   # P1,P2 max payoff's on each stratgy

   for i in range(r):
      P2_row_Max = np.max(P2_T[i])
      max_payoff_index = np.where(P2_T[i] == P2_row_Max)
      max_payoff_index = max_payoff_index[0]
      p2_max_row.append(max_payoff_index)

      P1_row_Max = np.max(P1_T[i][p2_max_row[i]])
      P1_max_payoff_index = np.where(P1_T[i] == P1_row_Max)
      P1_max_payoff_index = P1_max_payoff_index[0]
      P1_max_duplicate_index = np.intersect1d(p2_max_row[i], P1_max_payoff_index)
      p1_max_when_p2_max.append(P1_max_duplicate_index)

   #finding best response between whole stratgy for P1
   dump = 0
   for i in range(len(p1_max_when_p2_max)):
      b1 = np.max(P1_T[i][p1_max_when_p2_max[i]])
      if (b1 >= dump):
         P1_max = b1
         dump = b1

   p1_max_duplicates={}
   #Nash eq's
   for i in range(r):
      b = np.where(P1_T[i] == P1_max)
      b = b[0]
      if b.size!=0:
         p1_max_duplicates[i] = np.intersect1d(b, p1_max_when_p2_max[i])


   for i in range(r):
      p1_clones[i].goto(p1_x_coord[i],200-50)
      p2=p1_clones[i].clone()
      p2.pen(pencolor='blue', pensize=5)
      p2.color('blue')
      p2.shapesize(0.1, 0.1, 0.1)
      p2.write(P2_str)
      x_curr=p1_clones[i].xcor()
      n=c-1
      p2_clones = [p2]
      clones(p2, n, p2_clones)
      # p2_x_coord =x_curr+ np.linspace(-dx / 2, dx / 2, c)
      p2_angles=np.linspace(90+45,90-45,c)




      for j in range(c):

         p2_clones[j].right(p2_angles[j])
         p2_clones[j].forward(50)
         p2_clones[j].penup()
         p2_clones[j].ht()
         p2_clones[j].forward(20)
         payoff_1 = P1_T[i, j]
         payoff_2 = P2_T[i, j]
         p2_clones[j].color('black')
         payoff_str = "(" + str(payoff_1) + ',' + str(payoff_2) + ")"
         p2_clones[j].write(payoff_str, False, align='right')

   nash_clone = turtle.Turtle('circle')
   nash_clone.pen(pencolor="green",pensize=6)
   nash_clone.color('green')
   nash_clone.shapesize(0.1, 0.1, 0.1)

   nash_clone.penup()
   nash_clone.goto(0, 200)
   nash_clone.pendown()
   nash_clones=[]


   clones(nash_clone,len(p1_max_duplicates),nash_clones)

   p1_nash_coords = list(p1_max_duplicates.keys())

   for i in range(len(nash_clones)):

      nash_clones[i].goto(p1_x_coord[p1_nash_coords[i]], 200 - 50)
      x_curr = p1_clones[i].xcor()

      nash_clone_2 = nash_clones[i].clone()
      x_curr = p1_clones[i].xcor()
      n = len(p1_max_duplicates[p1_nash_coords[i]])
      nash_clones_2 = []
      clones(nash_clone_2, n, nash_clones_2)
      nash_angles = np.linspace(90 + 45, 90 - 45, c)

      for j in range(len(nash_clones_2)):

         nash_clones_2[j].right(nash_angles[p1_max_duplicates[p1_nash_coords[i]][j]])
         nash_clones_2[j].forward(50)
         nash_clones_2[j].penup()



   turtle.exitonclick()




    # turtle.color('black')
    # style = ('Arial', 30, 'italic')
    # turtle.write('Hello!', font=style, align='center')
    # turtle.hideturtle()
    # turtle.forward(100)
    # turtle.write('Hello!', font=style, align='center')
    # turtle.exitonclick()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
   Draw_Ext_Form2(P1,P2,'P1')


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
