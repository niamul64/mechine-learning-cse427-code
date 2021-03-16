

x = [(1,1),(1,2),(2,2),(3,1),(4,4),(4,5),(5,6),(6,7)]

lenth=len(x)

cent1=(3,2)
cent2=(5,5)
d1 = []
d2 = []
for i in range(lenth):
  print(" distance from centroied 1 to point",i+1 )
  # distance
  
  pointX,pointY=x[i]
  cenx,ceny=cent1
  
  
  temp1 = (cenx - pointX)**2 + (ceny - pointY)**2
  d1.append(temp1)
  print("(",cenx, "-", pointX,")**2 +(", ceny, "-", pointY,")**2 =",temp1)

  print("distance from centroied 2")
  cenx,ceny=cent2

  temp2 = (cenx - pointX)**2 + (ceny - pointY)**2
  d2.append(temp2)
  print("(",cenx, "-", pointX,")**2  +(", ceny, "-", pointY,")**2 =",temp2)
  print()


print("distencess from centroid1: ",cent1," : " ,d1)
print("distencess from centroid2: ",cent2," : " ,d2)


color1=[]
color2=[]

for i in range(lenth):
    if d1[i]>d2[i]:
        color2.append(x[i])
    else:
        color1.append(x[i])

print("color1 points",color1)
print("color2 points",color2)
xavg=0
yavg=0
for i in range(len(color1)):
    pointx,pointy=color1[i]
    xavg=xavg+pointx
    yavg=yavg+pointy
newCen1=(xavg/len(color1),yavg/len(color1))



print("\n new centroid 1 : ",newCen1)


xavg=0
yavg=0
for i in range(len(color2)):
    pointx,pointy=color2[i]
    xavg=xavg+pointx
    yavg=yavg+pointy
newCen2=(xavg/len(color2),yavg/len(color2))
print(" new centroid 2 : ",newCen2)