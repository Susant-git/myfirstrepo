import matplotlib.pyplot as plt
x = [1,2,3,4,5,7]
y =  [9,8,7,1,6,15]
c=["r","g","pink","b","g","y","b"]
plt.bar(x,y,width=0.3,color=c,alpha=0.8,align="center",edgecolor="r",linewidth=2,linestyle=':'
        ,label=["myword","here","there","hii","jio","air"])
plt.legend()
plt.title("temperture")
plt.xlabel("Time",fontsize=20,color='r')
plt.ylabel("Temp")

x1 =[1,2,3,4,5,7]
y1=[15,20,15,18,25,6]
plt.bar(x,y1,color="r",label="day-2",width =0.3,alpha=0.1)
plt.legend()
plt.show()