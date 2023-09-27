from fractions import Fraction
import matplotlib.pyplot as plt
import math


def Range(start,end,step):
  #range() function float number k step hisebe use kora jai na. Tai eikhane
  #customized Range() function create kora hoiche
  list=[]
  i=start
  while i<=end:
    list.append(i)
    i+=step
  return list


def gamma(get_num):
  #calculate gamma function for fractions
  #gamma(x/2) = ((x/2)-1)*gamma((x/2)-1)
  #gamma(1/2) = sqrt(pi)
  #recursive function used in this function

  #base condition
  if Fraction(get_num)==Fraction(1/2):
    return math.sqrt(math.pi)
  elif Fraction(get_num)==1:
    return 1
  #recursive condition
  else:
    return (Fraction(get_num)-1)*gamma(Fraction(get_num)-1)

  
  
def generate_F_and_x():
  values_of_k=[]    #k er value gulo k ekta list nea nichhi karon ei value gulo k graph er legend hisebe use korbo
  
  for k in range(1,10,3):
    values_of_k.append(k)
    #x er value 0 theke start kora jabe na, karon x = 0 hole f(0) calculate korar
    #somoy 0^-(1/2) asbe which arise error.
    values_of_x=Range(.25,30,.25)
    F_of_x=[]
    for x in values_of_x:
      F_of_x.append(((x**((k/2)-1))*math.exp(-x/2))/((2**(k/2))*gamma(Fraction(k/2))))

    plt.plot(values_of_x, F_of_x)

  plt.title("pdf of chi-squre distribution for different k")
  plt.xlabel("x")
  plt.ylabel("f(x)")
  plt.legend(values_of_k)
  plt.axis(xmax=20)
  plt.show()


generate_F_and_x()
