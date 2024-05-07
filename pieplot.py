import matplotlib.pyplot as plt
brands = ["Apple", "Redmi", "Oneplus", "Nokia", "Vivo"]
x = [600, 1000, 700, 100, 500]
c = ["b","orange","r","g","y"]
plt.pie(x,labels=brands,colors=c,explode=[0,0,0,0.2,0],shadow=True,autopct="%0.2f",
        startangle=180,rotatelabels=True)
plt.show()