import matplotlib.pyplot as plt

# dataset 
x = [95, 85, 80, 70,60]
y = [85, 95,70, 65, 70]

print(len(x),"     ",len(y))

m = len(x)
alpha = 0.01

#para meter initia initialization
theta = [1, 2]


J = 100
n = 0 
for i in range(3):
  print("Iteration number: ",n+1)
  n = n+1
  # hypothesis function
  h = []
  print("Hypothesis function value is: h0(x)=theta_0+theta_1 * x")
  for i in range(m):
    temp = theta[0] + theta[1]*x[i]
    h.append(temp)
    print("h0(",i,")(x)=",theta[0],"+",theta[1],"*",x[i],"=",temp)
 

  # cost function
  error_sum = 0 
  print("Cost function is: j(theta)=1/(2*m) * i=1_samtionSign_m (h_theta_(x)-y)**2")
  print("j(theta)=1/(2*m) { (", end=" ")
  for i in range(m):
    error_sum = error_sum + (h[i] - y[i])**2
    print(h[i] ,"-", y[i],")**2 +(", end=" ")
  J = (1/(2*m))*error_sum

  print("\nCost function is:",J)
    # gradient descent
  print(" gradient decent:")
  temp0 = 0
  for i in range(m):
    temp0 = temp0 + (h[i] - y[i])

  theta[0] = theta[0] - (alpha/m)*temp0

  temp1 = 0
  for i in range(m):
    temp1 = temp1 + (h[i] - y[i])*x[i]

  theta[1] = theta[1] - (alpha/m)*temp1

  print("New parameter value is: ",theta)
  plt.plot(x, h, marker = "o")
  plt.show

print("predicted hypothesis is:",h)