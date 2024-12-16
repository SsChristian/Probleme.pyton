import matplotlib.pyplot as plt
import pandas as pd 

df = pd.read_csv(r"C:\Users\crist\Desktop\ex2\data.csv")

df.plot(color=['red','blue','yellow','green'])
plt.title("Toate valorile")
plt.xlabel("Index")
plt.ylabel("Valori")
plt.legend(title="Parametrii")
plt.show()

df[:5].plot(color=['red','blue','yellow','green'])
plt.title("Primele 5 valori")
plt.xlabel("Index")
plt.ylabel("Valori")
plt.legend(title="Parametrii")
plt.show()

df1 = df[['Durata' , 'Puls']].head(13)
df1.plot(color=['green','red'])
plt.title("Ultimele 13 valori")
plt.xlabel("Index")
plt.ylabel("Valori")
plt.legend(title="Parametrii")
plt.show()