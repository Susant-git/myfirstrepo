import matplotlib.pyplot as plt
x = ["D-1","D-2","D-3","D-4","D-5"]
y = [100,250,300,400,480]
plt.plot(x,y,marker="o",ls=":")
plt.xlabel("days",color='r',fontsize=17)
plt.ylabel("No. of People",color="red",fontsize=17)
plt.title("No. of customers vs days",fontsize=25,color="violet")
#plt.legend()
plt.show()