

# dataset 
x = [.5,.7,1.2]


print("len:",len(x))

m = len(x)

ui=0
print("ui= ",end="")
for i in range(m):
    ui=ui+x[i]
    print(x[i],end=" ")
ui=ui/len(x)
print('=',ui)

si=max(x)-min(x)
print("si=",max(x),"-",min(x),"=",si)

newX=[]
for i in range(m):
    print("x1(",(i+1),")",end="=")
    temp=x[i]-ui
    print(x[i],"-",ui,end="/")
    temp=temp/si
    print(si)
    newX.append(temp)
    
print(newX)