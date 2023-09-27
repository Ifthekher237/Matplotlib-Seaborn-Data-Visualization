import matplotlib.pyplot as plt

def draw_graph(f,r):
  plt.plot(r,f,marker="o")
  plt.title("Newton's law of Gravitation")
  plt.xlabel("distance")
  plt.ylabel("Gravitational force")
  plt.show()


def generate_F_r():
  m1=.5
  m2=1.5
  G=6.674*(10**-11)   #gravitational constant

  r=range(100,1001,50)
  F=[]

  for dist in r:
    f=(G*m1*m2)/(dist**2)
    F.append(f)
  
  draw_graph(F,r)


generate_F_r()