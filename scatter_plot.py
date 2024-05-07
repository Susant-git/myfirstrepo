import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv('E:/power bi/datasets/class datasets/tips.csv')

x = df.groupby('day')['total_bill'].sum()
print(x)
print(type(x))
x1 = x.index.tolist()
y1 = x.values.tolist()
print(x1,"\n",y1)
plt.scatter(x1,y1)
plt.title("Total_bills VS Days",fontsize=20,color='g')
plt.legend(loc=0)
plt.show()