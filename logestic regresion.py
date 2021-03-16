import math
import matplotlib.pyplot as plt

x1 = [.5, 1.5, 1, 1.5]
x2 = [1.5, 1, 1.5, 2]
y = [0, 1, 1, 1]
m = len(y)
alpha = 0.01
theta = [1, 0.5, 1]

def sigmoid(x):
  return 1/(1+math.exp(-x))
for i in range(2):
  print("\nitration:",i+1)  
  h = []
  for i in range(m):
    temp = sigmoid(theta[0] + theta[1]*x1[i] + theta[2]*x2[i])
    h.append(temp)

  print("\nHypothesis function value is: ",h,end="\n\n")

  ht = []

  for j in range(m):
    if h[j]>=0.5:
      ht.append(1)
    else:
      ht.append(0)

  print("Hypothesis prediction value with threshold is: ",ht)

  temp = 0
  for i in range(m):
    temp = temp + (y[i]*math.log(h[i]) + (1 - y[i])*math.log(1 - h[i]))

  J = (-1/m)*temp

  print("Cost function value is: ",J)

  temp0 = 0

  for i in range(m):
    temp0 = temp0 + (h[i] - y[i])

  theta[0] = theta[0] - (alpha/m)*temp0

  temp1 = 0

  for i in range(m):
    temp1 = temp1 + (h[i] - y[i])*x1[i]

  theta[1] = theta[1] - (alpha/m)*temp1

  temp2 = 0

  for i in range(m):
    temp2 = temp2 + (h[i] - y[i])*x2[i]

  theta[2] = theta[2] - (alpha/m)*temp2

  print("New parameter value is: ",theta)

print("Final value: ",h)

